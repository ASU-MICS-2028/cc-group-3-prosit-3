---
title: Lab 12 overview: MQTT sensor to broker to time-series DB to live chart, with buffering and device security
tags: [lab, iot, mqtt]
source: Lab 12 (week12_lab_Students)
---

Week 12 lab (3 hours plus 90-120 minute extension): build the real pipeline for one SmartCity domain (traffic, air quality, waste, water, energy or flood). A simulator is fully acceptable; be explicit in the report about what is simulated.

Objectives: run an MQTT broker, publish structured readings, bridge MQTT to the broker/time-series DB, buffer locally through an outage, chart the live stream, apply per-device credentials with a revocation procedure.

Parts and deliverables:
- Part A (30 min): Mosquitto broker. Part B (60 min): sensor script. Deliverable A: terminal output of publish and mosquitto_sub.
- Part C (75 min): bridge into the time-series DB. Deliverable B: query output plus a demonstrated buffer-and-flush after stopping the broker/DB.
- Part D (30 min): live chart (polling page or Grafana). Deliverable C: screenshot.
- Part E (15 min): per-device credentials and a revocation plan.

Lab report (300 words, due before the Week 13 Monday lecture, so Mon of 1-5 Dec): domain and protocol reasoning (even if simulated), what the buffering test showed, one change before deploying 100+ devices. Submit PDF, sensor script, query output, chart screenshot.

Rubric: working end-to-end pipeline 35%; local buffering shown 20%; live visualization 20%; per-device security 10%; report reasoning on protocol and production readiness 15%. Optional extension: three domains at once, downsampling job, revocation drill, OpenAQ real data, read the MLOps paper.

## Related
- [Lab 12 Part A: install Mosquitto and subscribe to accra/# to see all sensor topics](mosquitto-local-mqtt-broker-setup.md)
- [A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware](sensor-simulator-mqtt-publisher.md)
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)
- [Each device gets its own MQTT credential so one can be revoked alone](per-device-mqtt-credentials-and-revocation.md)
