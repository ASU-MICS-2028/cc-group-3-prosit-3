---
issue: 40
title: Privacy and data-ownership note
date: 2026-11-24
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `docs/privacy.md`, a note for residents and AMA covering:
  - who owns each kind of data and who can see it
  - what we never collect, and where in the code each point is enforced
  - how a neighbourhood switches its sensors off and has its data deleted
  - the gaps to close before going live
- `api/app.py`: `Handler.log_message` drops the caller's IP address, which Python's default puts at the start of every log line.
- Links from the README and `docs/README.md`. Plan `plans/40-community-privacy.md`.

## Why

Community engagement is 30% of the grade. A neighbourhood will want to know these answers before agreeing to sensors. The final report (#47) also needs this section.

## How to check
- Read `docs/privacy.md`. Each claim in "What we never collect" points at a contract, a file or a test.
- Start the API and request any path. The log line reads `[date] "GET /path HTTP/1.1" 404 -`, with no address.

## AI use
- **Tool:** Claude Code
- **What it did:**
  - Drafted the note, plan and this file from the issue, the storage and API contracts, `ingest/devices.py`, and decisions 13 and 54.
  - While checking the "never collect" list against the code, it noticed that the default HTTP log records IP addresses, and made the two-line fix.
- **Prompts / session summary:** "go ahead with #40".
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- none (the 12-month retention period for reports is a proposal inside the note)

## Not done
- Registering with the Data Protection Commission and a retention job for reports: listed in the note as gaps before going live.
