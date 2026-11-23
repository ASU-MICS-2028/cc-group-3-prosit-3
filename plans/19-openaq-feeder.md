# Plan: OpenAQ feeder for real Accra PM2.5

- **Issue:** #19
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done in this PR

## Goal
Feed real air-quality data through the pipeline (Lab 12 extension).

## What gets built
- `sensors/openaq.py`: the last 24 h of PM2.5 for Madina Zongo Junction (OpenAQ 3025587), published as `aq-madina-001` with the same topic, schema and broker as the simulator (`source: "openaq"`).
- `ingest/devices.py` gives the feeder its own password and ACL.
- Tests: CSV rows to readings (window, dedupe, schema), and the feeder's ACL.
- Evidence script running real and simulated PM2.5 through the same broker, bridge and DB, with a variability comparison.

## Depends on
- #18. Stacked on #64, so the feeder gets credentials from #21.

## Done when
- Script pulls the last 24 h of PM2.5 for one Accra station and publishes it through the same topics and schema
- Two sentences comparing real variability with the simulator's (`sensors/README.md`)

## Evidence to capture
- `evidence/lab12/19-*`: feeder publish log, bridge log, per-device stats by source.

## Not doing
- The live v3 API (needs an API key we don't have; the archive is a few days behind but free and keyless).
- Recalibrating the simulator from one station-day.
- Running the feeder on a schedule.
