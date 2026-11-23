# Plan: Prediction API endpoint (L13-D)

- **Issue:** #31
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 13
- **Status:** done in this PR

## Goal
Serve the forecast behind the API (Lab 13 Part D, 25%).

## What gets built
- `api/app.py`: every path in `contracts/api.openapi.yaml`, not only predictions. The dashboard (#23), the mobile app (#24, #34) and the open-data page (#38) are all waiting on these reads.
- `GET /predictions/pm25` on a naive seasonal baseline (same hour yesterday) labelled `naive-seasonal-24h`, until #30 registers a model. Every point served is logged to `predictions` for the drift log (#32).
- `api/schema.sql`: `alerts`, `citizen_reports`, `predictions`.
- Unit tests for the forecast and report validation, added to CI.

## Depends on
- #30 for the real model. The endpoint shape doesn't wait for it.
- Stacked on #63 (#21), for the local stack.

## Done when
- GET /predictions/pm25 serves the registered model per contracts/api (now: the baseline; the model swaps in when #30 lands)
- Request/response evidence in evidence/lab13/

## Evidence to capture
- `evidence/lab13/31-*`: every endpoint and the error cases against ~50 h of simulated data, the rows logged to `predictions`, and a 503 with the DB stopped.

## Not doing
- Auth and rate limiting (undecided in the contract; needed before #35 makes it public).
- Paging on `/readings`. Hourly rollup tables are #22; until then aggregates are computed from raw readings.
- A web framework: six routes don't need one.
