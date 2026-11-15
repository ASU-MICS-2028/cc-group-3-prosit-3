---
title: Lab 10 Part D: a one-page choice of message broker and time-series database
tags: [lab, time-series, iot]
source: Lab 10 (week10_lab_Students) Part D
---

Write a one-page decision document. Broker options: Kinesis, Event Hubs, Pub/Sub, or self-hosted Kafka. Time-series DB options: InfluxDB, TimescaleDB, or a managed equivalent. Justify against the team's existing platform, the expected sensor volume (thousands of readings per minute) and the remaining budget. Labs 11 and 12 build on this choice (the budget model and the pipeline), so it is hard to reverse later. Also graded in the lab report (20% of the lab rubric).

## Related
- [Lab 10 overview - auto-scaling, golden-signal dashboard, k6 load test, ingestion-stack choice](lab-10-auto-scaling-monitoring-load-testing.md)
- [Itemize the monthly cost: broker, time-series DB, compute, egress, with stated assumptions](smartcity-ingestion-budget-model.md)
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)
