---
title: IoT, edge and offline (map)
tags: [process]
source: index of the notes below
---

MQTT, sensors, buffering, time-series storage, edge computing, offline-first sync.

**Taught or given**

- [A paho-mqtt script publishing a JSON reading every 5 seconds stands in for real hardware](sensor-simulator-mqtt-publisher.md)
- [Core PWA technologies are the service worker, web app manifest and cache API](pwa-core-technologies.md)
- [Edge compute lets sensitive data be used locally instead of moved to the cloud](edge-inference-keeps-data-on-premises.md)
- [Edge devices with CPU and GPU on one chip share memory, enabling zero-copy inference](edge-ai-shared-memory-zero-copy.md)
- [Four places to run ML: cloud, separate CPU+GPU, CPU-only, or a single-chip edge device](edge-vs-cloud-vs-cpu-gpu-tradeoffs.md)
- [If the MQTT broker refuses connections, check mosquitto.conf listener settings](mosquitto-listens-localhost-only-by-default.md)
- [IoT loop: sense at the edge, communicate over MQTT to a central store, compute and control](iot-sense-communicate-compute-control.md)
- [IPv6 is gradually replacing IPv4 and is what makes IoT addressing possible at scale](ipv6-and-iot.md)
- [Lab 10 Part D: a one-page choice of message broker and time-series database](ingestion-stack-decision-document.md)
- [Lab 12 Part A: install Mosquitto and subscribe to accra/# to see all sensor topics](mosquitto-local-mqtt-broker-setup.md)
- [Nano services on IoT sensors and the cache eviction choice](nano-services-iot-lru-vs-lfu.md)
- [Offline sync needs a conflict resolution strategy, like merging in Git](offline-sync-conflict-resolution.md)
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Optional: feed 24 hours of real Accra PM2.5 from OpenAQ through the same MQTT pipeline](openaq-real-pm25-data-option.md)
- [Replay real sensor data against a hypothetical alert threshold and count the extra alerts](digital-twin-what-if-replay.md)
- [Scheduled job turns raw readings into an hourly-average table](downsampling-hourly-averages-job.md)
- [Slow time-series writes: batch inserts instead of one INSERT per reading](batched-inserts-for-time-series-writes.md)
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](mqtt-to-timescaledb-bridge-local-buffering.md)

**Found out by doing** (in `learnings/`)

- [Drain the offline queue in the background, with a Web Lock so only one runner sends](../learnings/background-sync-with-web-locks.md)
- [Ids created on the device make offline retries idempotent](../learnings/client-generated-uuids-make-retries-safe.md)
- [Offline app design: save locally first, encrypt, queue, and let a person settle conflicts](../learnings/offline-conflicts-are-shown-to-a-person.md)
- [Sync downloads with a running-number bookmark can skip records unless numbering is ordered](../learnings/sync-bookmark-lock-avoids-skipped-records.md)
- [WebRTC results: direct paths worked, Chrome Slow 3G does not throttle media, TURN cost is a range](../learnings/webrtc-testing-and-turn-findings.md)

## Related
- [Lectures by week (map)](map-lectures.md)
- [SmartCity Accra brief and our scope (map)](map-smartcity-brief.md)
- [Labs 0–14 (map)](map-labs.md)
- [Course facts (map)](map-course.md)
