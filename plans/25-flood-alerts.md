# Plan: Flood early-warning alerts (API + app)

- **Issue:** #25
- **Owner:** Joseph (`josetseph`)
- **Status:** API half done in this PR. The app screen is with #24 (Pea).

## Goal
Warn residents when drain water levels rise.

## What gets built
- `api/alerts.py`: a checker that opens and closes rows in `alerts` from each drain gauge's latest reading. Flood warning at 60 cm (closes below 50 cm). Rising fast at +15 cm in 15 min (closes under +5 cm). Each `reason` is in plain words with the numbers.
- `alerts.closed_at` column; `GET /alerts?status=closed` gives history.
- Rule tests; a live 24-hour run as evidence.

## Depends on
- #2 (contract), #20 (bridge). Stacked on #65, for the API from #31.

## Done when
- A flood reading above threshold, or an anomaly, opens an alert via GET /alerts (done)
- The mobile app shows it; the threshold rule is explained in plain words (the rule text is in `api/README.md` and every `reason`; the screen is #24)

## Evidence to capture
- `evidence/lab12/25-*`: checker log, alerts table with open/close times, `GET /alerts` responses.

## Not doing
- The app screen (#24) and "flag this alert as wrong" (#41), both Pea's.
- Per-drain lines (one setting for all until real gauges), push notifications or SMS, bin-full alerts (#33).
- An ML anomaly model: the rate-of-rise rule is easy to explain to residents, and Elise's anomaly work can replace it.
