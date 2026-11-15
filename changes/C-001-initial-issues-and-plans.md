---
id: C-001
title: Initial issues, labels, milestones and plan stubs
date: 2026-11-15
issue: "#1"
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- GitHub: labels (`area:*`, `lab:10`–`lab:14`, `week:1`–`week:4`, `type:*`, `blocked`, `skip-change-file`), one milestone per lab with its due date, and issues #1–#50 covering Labs 10–14, the brief's weeks 1–4, the five written course reports, community engagement, deploys and the GCP track. Each has one owner.
- `plans/`: one plan stub per issue (goal, depends on, done when from the lab rubric or the brief) and a row each in `plans/README.md`.

## Why

The setup design (`docs/specs/2026-11-14-setup-design.md`, section 11) says every task is an issue with a plan, so everyone can see their work, its due date and what it waits on.

## How to check
```bash
gh issue list -R ASU-MICS-2028/cc-group-3-prosit-3 --limit 100 --json number -q length   # 50
gh api repos/ASU-MICS-2028/cc-group-3-prosit-3/milestones -q 'length'                   # 5
ls plans/*-*.md | wc -l                                                                   # 50
python3 scripts/check_notes.py knowledge learnings
```

## AI use
- **Tool:** Claude Code
- **What it did:** turned the Lab 10–14 handouts, the Prosit 3 brief and the course schedule into issue titles, "done when" lines and plan stubs; created the labels, milestones and issues with `gh`.
- **What the person checked or changed:** Joseph set the scope (three sensor domains), the roles and the review rule, and approved the owner list in the design and plan reviews on 14–15 Nov.

## Decisions made
- None new. Owners for the five written reports and the capstone pieces are defaults from the plan; reassign on the issue if needed.

## Not done
- Each owner fills in "What gets built", "Evidence to capture" and "Not doing" in their plan before starting.
- Perfect has 7 issues, the others 12–17. Rebalance if Perfect has room.
