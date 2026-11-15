"""Check that a PR adds exactly one new change file, changes/C-NNN-<slug>.md, with an unused number.

Usage: python3 scripts/check_change_file.py --base origin/main --labels "a,b"
A PR labelled skip-change-file (pure chores) is let through.
"""
import argparse
import re
import subprocess
import sys

PATTERN = re.compile(r"^changes/C-(\d{3})-[a-z0-9-]+\.md$")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout.split()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--labels", default="")
    a = ap.parse_args()
    if "skip-change-file" in a.labels.split(","):
        print("skip-change-file label set: no change file needed")
        return 0
    added = [f for f in git("diff", "--name-only", "--diff-filter=A", f"{a.base}...HEAD") if PATTERN.match(f)]
    if len(added) != 1:
        print(f"This PR adds {len(added)} change files; it must add exactly one: changes/C-NNN-<slug>.md "
              "(copy changes/TEMPLATE.md and add a line to changes/README.md). "
              "For a pure chore, add the label skip-change-file instead.")
        return 1
    num = PATTERN.match(added[0]).group(1)
    taken = [f for f in git("ls-tree", "-r", "--name-only", a.base, "changes/") if f.startswith(f"changes/C-{num}-")]
    if taken:
        print(f"C-{num} is already used on {a.base} ({taken[0]}). Rename {added[0]} to the next free number.")
        return 1
    print(f"change file OK: {added[0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
