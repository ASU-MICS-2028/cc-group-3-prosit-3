---
title: Write every reading to a local spool first, so one path covers normal running and DB outages
tags: [iot, mqtt, reliability]
source: PR for #20 (ingest/bridge.py)
---

The Lab 12 starter bridge inserts each reading and only spools it when the insert fails, so it has two paths and a reading in memory is lost if the bridge crashes mid-insert. Our bridge appends every reading to `spool.jsonl` (fsynced) as it arrives, and a once-a-second loop writes the spool to the DB in one transaction, then drops what was written. DB down: the spool just grows. DB back: the backlog goes in first, in order.

It's safe to repeat because `(device_id, ts)` is unique and inserts use `ON CONFLICT DO NOTHING`: a crash between commit and trimming the spool re-sends rows that are then ignored. Tested by stopping TimescaleDB for 12 s mid-run: 289 published, 289 stored, no `seq` gaps.

## Related
- [Paho raises on publish while the broker is down; catch it or the sensor dies](paho-publish-raises-while-broker-is-down.md)
- [The outbox gap: saving data then publishing can lose the event](outbox-pattern-for-lost-events.md)
- [The bridge writes each MQTT reading to TimescaleDB and spools to a local file when the DB is down](../knowledge/mqtt-to-timescaledb-bridge-local-buffering.md)
