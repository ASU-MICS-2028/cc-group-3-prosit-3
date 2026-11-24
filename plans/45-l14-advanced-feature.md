# Plan: Advanced feature test: what-if replay of the flood warning line (L14-A)

- **Issue:** #45
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 14 / final
- **Status:** done

## Goal
Lab 14 Part A (15%): one advanced feature, scoped small, with an honest 300-word test report.

## What gets built
- `api/what_if.py`:
  - Generates 30 days of drain readings with the simulator (seed 45).
  - Replays each gauge's readings through `api/alerts.py`'s `decide()` at the current line and at lower lines.
  - Prints warnings, lead time over today's line, extra warnings, and hours under warning.
- `decide()` takes the warning and clear lines as optional arguments; the defaults are unchanged.
- `api/tests/test_what_if.py`: a 2 cm/min storm warns 10 minutes earlier at 40 cm than at 60 cm, and a storm that peaks at 50 cm is an extra warning.
- `docs/what-if-test-report.md`: the 300-word report.

## Depends on
- nothing. We switched from the multi-cloud test, which needed #16 and the AWS deploys; see decision 54.

## Done when
- 300-word test report: what we tried, what happened, what production would need
- Results honest even if it didn't work

## Evidence to capture
- `evidence/lab14/45-what-if-output.txt` (`python3 api/what_if.py`)

## Not doing
- The multi-cloud test. Neither cloud is running yet.
- Real drain data, which doesn't exist. The report says the readings are simulated.
