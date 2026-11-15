"""Check one-idea notes: front matter, a Related section, and a link from the folder's README.

Usage: python3 scripts/check_notes.py knowledge learnings
"""
import re
import sys
from pathlib import Path

REQUIRED = ("title", "tags", "source")
SKIP = {"README.md", "TEMPLATE.md"}


def problems(folder: Path):
    index = (folder / "README.md").read_text() if (folder / "README.md").exists() else ""
    linked = set(re.findall(r"\]\(([^)#\s]+\.md)", index))
    for note in sorted(folder.glob("*.md")):
        if note.name in SKIP:
            continue
        text = note.read_text()
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        keys = set(re.findall(r"^(\w+):", m.group(1), re.M)) if m else set()
        for k in REQUIRED:
            if k not in keys:
                yield f"{note}: front matter has no '{k}:' — copy the header from {folder}/TEMPLATE.md"
        if not re.search(r"^## Related", text, re.M):
            yield f"{note}: no '## Related' section — add one with links to related notes"
        if note.name not in linked:
            yield f"{note}: not linked from {folder}/README.md — add \"- [title]({note.name}) — hook\""


def main(folders):
    found = [p for f in folders for p in problems(Path(f))]
    print("\n".join(found) if found else "notes OK")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
