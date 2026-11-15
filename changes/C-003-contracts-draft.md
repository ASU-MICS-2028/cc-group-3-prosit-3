---
id: C-003
title: First draft of the shared contracts
date: 2026-11-15
issue: "#2"
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `contracts/`: sensor-reading JSON Schema with one example per domain and a bad example, MQTT topic layout, OpenAPI 3.1 draft of the app-facing API, logical storage layout.
- `contracts/tests/`: tests that the examples validate, the bad one and a wrong unit or unknown field are rejected, and the API lists the six agreed paths. CI job `contracts` runs them.
- `decisions/D-001` (proposed).

## Why

So every area can build against the same shapes with fake data from day one (setup design, section 7).

## How to check
```bash
pip install -r contracts/requirements.txt
python3 -m unittest discover contracts/tests -v   # 5 tests OK
```

## AI use
- **Tool:** Claude Code
- **What it did:** drafted the schema, examples, topic layout, OpenAPI file, storage layout and tests from the setup plan's values and the Lab 12–13 handouts.
- **What the person checked or changed:** _Joseph to complete_

## Review fixes
- Duplicates are dropped on `(device_id, ts)`, not `(device_id, seq)`: `seq` restarts when a device restarts, so keying on it would silently throw away real readings.
- The examples test no longer breaks when an example is added.
- `contracts` listed in CONTRIBUTING's checks table; issue #55 makes it a required check.

## Decisions made
- [D-001](../decisions/D-001-sensor-reading-and-topic-contract.md) (proposed)

## Not done
- API auth; physical DB layout (after the Lab 10 Part D decision).
- `contracts` is not yet a required check on `main`; add it to branch protection after this merges.
