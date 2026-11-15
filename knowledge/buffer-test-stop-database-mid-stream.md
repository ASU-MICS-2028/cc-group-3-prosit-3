---
title: Prove resilience by stopping the DB while the simulator keeps publishing
tags: [lab, reliability, iot]
source: Lab 12 (week12_lab_Students) Part C
---

Deliverable B includes a demo: stop the database (docker stop of the DB container, or a security-group change) while the simulator publishes, confirm readings pile up in the buffer file, restart the DB, and confirm they flush on the next message. Troubleshooting: if the buffer grows but never flushes, check flush_buffer() runs on every message and that reconnection does not need a bridge restart. Report what happened and what it implies for production.

## Related
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
