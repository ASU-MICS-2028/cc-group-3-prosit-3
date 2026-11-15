---
id: D-001
title: Sensor reading, MQTT topic, API and storage contracts (draft v0)
date: 2026-11-15
decided_by: Joseph (proposed; open for team comment)
status: proposed
---

## Context

Five parts (simulator and bridge, database, API, web, mobile) are built by different people at the same time. Without fixed formats, each waits for the one before it. Lab 12 builds the pipeline, Lab 13 the model and endpoint; the apps need data shapes now.

## Options

1. **Topic per device** `accra/<neighbourhood>/<domain>/<device_id>` — lets the broker ACL restrict each device to its own topic (Lab 12 per-device credentials) and lets subscribers filter by area or domain with wildcards. Longer topics.
2. **Topic per domain** `accra/<domain>` with the device in the payload — simpler, but any device could publish as any other, and revoking one device can't be enforced by topic.
3. **Generic reading** (any metric, any unit) vs **closed list** of three domain/metric/unit pairs — generic is flexible but lets bad data in silently; the closed list catches a wrong unit at the edge.

## Decision

Option 1 for topics, and a closed list of three domain/metric/unit pairs. Readings carry a per-device `seq` so the bridge can drop duplicates (QoS 1 delivers at least once) and spot gaps after buffering. `additionalProperties: false` so no extra fields (e.g. personal data) slip in. Raw readings kept 90 days (the Lab 11 budget assumption), hourly rollups kept longer.

## Consequences

- Adding a domain (e.g. traffic) means a schema change and a new decision; that's deliberate.
- The physical database layout still follows the Lab 10 Part D broker/DB decision; `storage.md` is logical only.
- Auth for the API is not decided here.
