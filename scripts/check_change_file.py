"""Check that a PR adds exactly one change file, changes/<issue-number>-<slug>.md, linked from changes/README.md.

Usage: python3 scripts/check_change_file.py --base origin/main --labels "a,b"
Any decision file the PR adds must be decisions/<same issue number>-<slug>.md and listed in decisions/README.md.
A PR labelled skip-change-file (pure chores) is let through.
Files are named after the issue the PR closes, so two PRs never pick the same name,
and each issue has its own slot line in the index, so PRs don't conflict there either.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

PATTERN = re.compile(r"^changes/(\d+)-[a-z0-9-]+\.md$")
DECISION = re.compile(r"^decisions/(\d+)-[a-z0-9-]+\.md$")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--labels", default="")
    a = ap.parse_args()
    if "skip-change-file" in a.labels.split(","):
        print("skip-change-file label set: no change file needed")
        return 0
    diff = subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", f"{a.base}...HEAD"],
                          capture_output=True, text=True, check=True).stdout.split()
    added = [f for f in diff if PATTERN.match(f)]
    if len(added) != 1:
        print(f"This PR adds {len(added)} change files; it must add exactly one: changes/<issue-number>-<slug>.md "
              "(copy changes/TEMPLATE.md, and fill your issue's slot in changes/README.md). "
              "For a pure chore, add the label skip-change-file instead.")
        return 1
    name = Path(added[0]).name
    index = Path("changes/README.md").read_text() if Path("changes/README.md").exists() else ""
    if f"]({name})" not in index and f"](./{name})" not in index:
        n = PATTERN.match(added[0]).group(1)
        print(f"{added[0]} is not linked from changes/README.md. Replace the line <!-- #{n} --> with "
              f"\"- [#{n}]({name}) — <title> — <in charge>\".")
        return 1
    n = PATTERN.match(added[0]).group(1)
    decisions_index = Path("decisions/README.md").read_text() if Path("decisions/README.md").exists() else ""
    for f in diff:
        if not f.startswith("decisions/") or f.endswith("/README.md"):
            continue
        m = DECISION.match(f)
        if not m or m.group(1) != n:
            print(f"{f}: decision files in this PR must be named decisions/{n}-<slug>.md (the PR's issue number).")
            return 1
        if f"]({Path(f).name})" not in decisions_index and f"](./{Path(f).name})" not in decisions_index:
            print(f"{f} is not listed in decisions/README.md. Replace the line <!-- #{n} --> with "
                  f"\"- [#{n}: <decision>]({Path(f).name}) — <status>\".")
            return 1
    print(f"change file OK: {added[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
