---
title: Seed knowledge and learnings as one-idea notes
date: 2026-11-15
issue: 3
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
- **Prompts / session summary:** the brief given to every note writer is summarised in this file; the setup plan is `docs/specs/2026-11-15-setup-plan.md` (Task 3).
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- None.

## Not done / known limits
- Notes come from automatic transcripts, which are garbled in places; a note that looks wrong should be checked against the slides and corrected by PR.
- **AI use is allowed** (Joseph, 15 Nov), declared in every change file. The course description's stricter wording is recorded in `course-ai-use-policy.md` for reference.
- The course description's Week 11 dates (17–21 Nov) start on a Tuesday; the lecture is Monday 16 Nov.
