---
issue: 45
title: "Lab 14 Part A: what-if replay of the flood warning line"
date: 2026-11-24
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `api/what_if.py`: replays 30 simulated days of drain readings through the production `decide()` at 60, 50 and 40 cm warning lines.
- `api/alerts.py`: `decide()` takes optional `warn`/`clear` arguments. The live checker still uses 60/50.
- `api/tests/test_what_if.py`: two tests.
- `docs/what-if-test-report.md`: the Lab 14 Part A report. Output in `evidence/lab14/45-what-if-output.txt`.
- `decisions/54-not-built.md`: the Lab 14 feature is now the what-if replay, with the reason.

## Why

Lab 14 Part A needs one advanced feature. The planned multi-cloud test had nothing to run on: the AWS deploys and the GCP rebuild are both still open. The replay was the fallback that decision 54 named.

## How to check
- `python3 api/what_if.py` prints the same table as the evidence file. The seed is fixed and it takes about 3 seconds, with no Docker needed.
- `python3 -m unittest discover api/tests`

## AI use
- **Tool:** Claude Code
- **What it did:** wrote the replay script, the tests and the report, and ran the replay. Every number in the report comes from the evidence file.
- **Prompts / session summary:** "go ahead with #45". Joseph chose the what-if replay over setting up GCP now.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- [What we are not building, and why](../decisions/54-not-built.md): the Lab 14 choice changed from multi-cloud to the what-if replay.

## Not done
- The multi-cloud test. It could still be added to the final presentation if the AWS deploys and #16 land in time.
