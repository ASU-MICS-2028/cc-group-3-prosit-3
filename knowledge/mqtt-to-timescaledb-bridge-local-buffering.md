---
title: The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down
tags: [lab, iot, time-series]
source: Lab 12 (week12_lab_Students) Part C
---

Starter bridge: subscribe to accra/#, on each message first try to flush the backlog file (JSON lines), then insert the reading into sensor_readings(sensor_id, value, recorded_at TIMESTAMPTZ); if the insert fails, append the reading to buffered_readings.jsonl. Flush rewrites the file with only the lines that still fail. DATABASE_URL comes from the environment.

Limits worth knowing: it opens a new connection per insert and only flushes when a new message arrives. InfluxDB is the alternative; the lab gives a Flux query. This is the offline-tolerance idea from the Week 4 PWA work applied to sensors.

## Related
- [Prove resilience by stopping the DB while the simulator keeps publishing](buffer-test-stop-database-mid-stream.md)
- [Slow time-series writes: batch inserts instead of one INSERT per reading](batched-inserts-for-time-series-writes.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
