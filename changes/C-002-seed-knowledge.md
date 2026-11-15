---
id: C-002
title: Seed knowledge and learnings as one-idea notes
date: 2026-11-15
issue: "#3"
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `knowledge/`: 268 one-idea notes from lectures 1–11 and the study session, Labs 0–14, the Prosit 3 brief and launch deck, the course description and glossary, and the Prosit 1–2 repos; plus 11 topic maps (`map-*.md`, including one per lecture week) and the README index.
- `learnings/`: 42 notes on procedures and gotchas carried over from Prosits 1–2 (Terraform recovery, IAM, CI/CD, migrations, idempotent events, offline sync, cost and teardown, honest evidence, what slowed us down).

## Why

So everyone, and every coding assistant, starts Prosit 3 with what the course has taught so far, in a form that is quick to search and link (setup design, section 8).

## How to check
```bash
python3 scripts/check_notes.py knowledge learnings   # notes OK
ls knowledge/*.md learnings/*.md | wc -l
```

## AI use
- **Tool:** Claude Code (eight parallel sub-agents on Sonnet drafted the notes; the main session merged 27 duplicate notes, built the maps and indexes, and ran the checks)
- **What it did:** read the transcripts, handouts and old repos and wrote the notes in its own words with a source on each; left out other students' names, contact details and garbled passages; ran a privacy scan (phone numbers, emails, names) and a link check.
- **What the person checked or changed:** _Joseph to complete_

## Decisions made
- None.

## Not done / known limits
- Notes come from automatic transcripts, which are garbled in places; a note that looks wrong should be checked against the slides and corrected by PR.
- **Two AI rules conflict:** the course description prohibits AI-generated coursework unless authorised for a task, while the lecturer allowed declared, verified use in class. Both notes say so and link each other (`course-ai-use-policy.md`, `ai-use-rules-verify-never-fabricate.md`).
- The course description's Week 11 dates (17–21 Nov) start on a Tuesday; the lecture is Monday 16 Nov.
