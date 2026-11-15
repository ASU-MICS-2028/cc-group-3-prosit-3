# Storage layout (logical)

Draft v0 (D-001, proposed). Logical shape only: the physical form (tables in TimescaleDB, measurements in InfluxDB, etc.) follows the Lab 10 Part D decision.

## Raw readings: one table/measurement per domain

| Name | Tags / indexed | Fields | Kept |
|---|---|---|---|
| `air_quality` | `device_id`, `neighbourhood`, `source` | `ts`, `seq`, `pm25`, `battery_pct` | 90 days |
| `waste` | `device_id`, `neighbourhood`, `source` | `ts`, `seq`, `fill_pct`, `battery_pct` | 90 days |
| `flood` | `device_id`, `neighbourhood`, `source` | `ts`, `seq`, `water_level_cm`, `battery_pct` | 90 days |

`neighbourhood` comes from the topic. **`(device_id, ts)` is unique**: a repeat after buffering or QoS 1 redelivery has the same timestamp and is ignored, not stored twice. `seq` is **not** a key: it restarts at 0 when a device or the simulator restarts, so it is only used to spot gaps between restarts.

## Hourly rollups

`air_quality_hourly`, `waste_hourly`, `flood_hourly`: per `device_id` and `neighbourhood` per hour: `avg`, `min`, `max`, `count`. Kept for the life of the project. They feed the dashboards' long views, the ML training sets and `/open-data`.

## Other tables (shape set by their issues)

- `alerts`: matches `Alert` in [`api.openapi.yaml`](./api.openapi.yaml).
- `predictions`: every prediction served, with `model_version`, so the drift log can join it to the actual reading later (Lab 13 Part E).
- `citizen_reports`: matches `CitizenReport`; no names or phone numbers.
