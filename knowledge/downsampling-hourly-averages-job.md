---
title: Scheduled job turns raw readings into an hourly-average table
tags: [lab, time-series, databases]
source: Lab 12 (week12_lab_Students) homework extension
---

Optional Lab 12 extension: a cron job or periodic script computes hourly averages from sensor_readings and stores them in sensor_readings_hourly, a concrete take on the lecture's downsampling idea. Useful for SmartCity retention and cost since raw data can be kept for a shorter period.

## Related
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)
- [Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security](lab-12-iot-sensor-pipeline.md)
