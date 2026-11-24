"""Tests for scripts/check_notes.py and scripts/check_change_file.py.

Run: python3 -m unittest discover scripts/tests -v
"""
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
GOOD_NOTE = """---
title: Golden signals
tags: [monitoring]
source: Lecture 10
---

Latency, traffic, errors, saturation.

## Related
- [Auto-scaling](auto-scaling.md)
"""


def run(script, *args, cwd=None):
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                          cwd=cwd, capture_output=True, text=True)


class CheckNotes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name) / "knowledge"
        self.dir.mkdir()
        (self.dir / "TEMPLATE.md").write_text("template, ignored")

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, note, index_links=("golden-signals.md",)):
        (self.dir / "golden-signals.md").write_text(note)
        links = "\n".join(f"- [x]({l}) — hook" for l in index_links)
        (self.dir / "README.md").write_text(f"# Knowledge\n\n{links}\n")

    def test_good_indexed_note_passes(self):
        self.write(GOOD_NOTE)
        r = run("check_notes.py", str(self.dir))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_note_missing_source_fails(self):
        self.write(GOOD_NOTE.replace("source: Lecture 10\n", ""))
        r = run("check_notes.py", str(self.dir))
        self.assertEqual(r.returncode, 1)
        self.assertIn("source", r.stdout)

    def test_note_missing_related_fails(self):
        self.write(GOOD_NOTE.split("## Related")[0])
        r = run("check_notes.py", str(self.dir))
        self.assertEqual(r.returncode, 1)
        self.assertIn("## Related", r.stdout)

    def test_dot_slash_index_link_counts(self):
        (self.dir / "golden-signals.md").write_text(GOOD_NOTE)
        (self.dir / "README.md").write_text("- [x](./golden-signals.md) — hook\n")
        r = run("check_notes.py", str(self.dir))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_unindexed_note_fails(self):
        self.write(GOOD_NOTE, index_links=())
        r = run("check_notes.py", str(self.dir))
        self.assertEqual(r.returncode, 1)
        self.assertIn("not linked from", r.stdout)


class CheckChangeFile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        g = lambda *a: subprocess.run(["git", *a], cwd=self.repo, check=True, capture_output=True)
        self.git = g
        g("init", "-q", "-b", "main")
        g("config", "user.email", "t@example.com")
        g("config", "user.name", "t")
        (self.repo / "changes").mkdir()
        (self.repo / "changes" / "1-first.md").write_text("first")
        (self.repo / "changes" / "README.md").write_text("- [#1](1-first.md)\n\n<!-- #2 -->\n")
        g("add", "-A")
        g("commit", "-qm", "base")
        g("switch", "-qc", "feature")

    def tearDown(self):
        self.tmp.cleanup()

    def commit(self, *files, index_links=()):
        for f in files:
            p = self.repo / f
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("x")
        if index_links:
            idx = self.repo / "changes" / "README.md"
            idx.write_text(idx.read_text() + "".join(f"\n- [x]({l})\n" for l in index_links))
        self.git("add", "-A")
        self.git("commit", "-qm", "work")

    def check(self, labels=""):
        return run("check_change_file.py", "--base", "main", "--labels", labels, cwd=self.repo)

    def test_pr_without_change_file_fails(self):
        self.commit("README.md")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("skip-change-file", r.stdout)

    def test_indexed_change_file_named_after_issue_passes(self):
        self.commit("README.md", "changes/2-readme.md", index_links=["2-readme.md"])
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_unindexed_change_file_fails(self):
        self.commit("changes/2-readme.md")
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("changes/README.md", r.stdout)

    def test_old_c_number_name_fails(self):
        self.commit("changes/C-002-readme.md", index_links=["C-002-readme.md"])
        r = self.check()
        self.assertEqual(r.returncode, 1)

    def test_skip_label_passes(self):
        self.commit("README.md")
        r = self.check(labels="docs,skip-change-file")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_decision_with_wrong_number_fails(self):
        self.commit("changes/2-a.md", "decisions/7-x.md", index_links=["2-a.md"])
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("decisions/2-", r.stdout)

    def test_unlisted_decision_fails(self):
        self.commit("changes/2-a.md", "decisions/2-x.md", index_links=["2-a.md"])
        r = self.check()
        self.assertEqual(r.returncode, 1)
        self.assertIn("decisions/README.md", r.stdout)

    def test_listed_decision_with_matching_number_passes(self):
        (self.repo / "decisions").mkdir()
        (self.repo / "decisions" / "README.md").write_text("- [#2: x](2-x.md) — proposed\n")
        self.commit("changes/2-a.md", "decisions/2-x.md", index_links=["2-a.md"])
        r = self.check()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_two_change_files_fails(self):
        self.commit("changes/2-a.md", "changes/3-b.md", index_links=["2-a.md", "3-b.md"])
        r = self.check()
        self.assertEqual(r.returncode, 1)


if __name__ == "__main__":
    unittest.main()
