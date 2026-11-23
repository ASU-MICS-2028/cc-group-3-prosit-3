---
issue: 31
title: SmartCity API, every contract endpoint, PM2.5 forecast on a naive baseline (Lab 13 Part D)
date: 2026-11-23
pr: "(this PR)"
in_charge: Joseph Etse
reviewed_by: (whoever approves this PR)
---

## What changed

- `api/app.py`: the REST API in `contracts/api.openapi.yaml`, covering latest readings, history (raw or hourly), alerts, PM2.5 forecast, citizen reports and open data. Standard library HTTP server plus psycopg, JSON errors (400/404/503), CORS for the dashboard.
- `api/schema.sql`: `alerts`, `citizen_reports` (no names or phone numbers), `predictions` (one row per point served, for #32).
- `/predictions/pm25` serves a naive seasonal baseline (`naive-seasonal-24h`, same hour a day earlier) until #30 registers a model.
- `api/tests/test_app.py`, run in the `contracts` CI job.
- Evidence: `evidence/lab13/31-api-run.sh` and output. 35,813 simulated readings over ~50 h. Every endpoint answered in under 0.08 s locally, the five bad requests got 400/404, and 72 forecast points were logged. With the DB stopped the API answers 503.
- `api/README.md`.

## Why

Lab 13 Part D. The dashboard, the mobile app and the open-data page all read from this API, so it was blocking three people.

## How to check
```bash
python3 -m unittest discover api/tests -v
PY=python3 bash evidence/lab13/31-api-run.sh   # ~40 s; needs Docker and ingest/.env; then read evidence/lab13/31-api-calls.txt
```

## AI use
- **Tool:** Claude Code
- **What it did:** wrote `app.py`, the schema, tests, evidence script, docs and this file, and ran the evidence.
- **Prompts / session summary:** "go ahead with the API". The first evidence run returned 404 for `aq-nima-001` because it was still revoked from the #21 drill. The script now issues fresh credentials first.
- **What the person checked or changed:** Joseph skims every file produced.

## Decisions made
- The whole contract in one server, not only `/predictions`.
- No framework (stdlib `http.server`).
- Baseline forecast until the model exists.

## Not done
- Real model (#30), alert rules (#25), auth and rate limit (before #35), paging, reading the hourly rollup tables (#22).
