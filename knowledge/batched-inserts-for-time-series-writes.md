---
title: Slow time-series writes: batch inserts instead of one INSERT per reading
tags: [lab, time-series, databases]
source: Lab 12 (week12_lab_Students) Troubleshooting
---

Lab 12 troubleshooting: if writes are slow even at moderate volume, use batched inserts rather than one INSERT per reading. The lab ties this to the connection-pooling lesson from Week 10, applied to writes.

## Related
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)
