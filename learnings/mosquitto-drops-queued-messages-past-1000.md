---
title: Mosquitto queues only 1000 messages for a client that falls behind, then silently drops the rest
tags: [iot, mqtt, reliability]
source: Issue #73 (evidence/lab12/73-*)
---

A persistent session (`clean_session=False`) with QoS 1 sounds like "the broker keeps everything until the client takes it". It doesn't. Mosquitto's `max_queued_messages` defaults to **1000** per client. Past that, it drops new messages for that client. The only sign is one line in the broker log: `Outgoing messages are being dropped for client bridge-1`.

We found it when running the pipeline in containers. The simulator published 2,214 readings in a burst. The bridge writes each one to its spool with an `fsync` before taking the next, so it fell behind, and only 1,565 were stored. Our buffering test (#20) had stopped the database, not the bridge, so it never filled the broker's queue.

The fix is one config line: `max_queued_messages 100000` in `mosquitto.conf`. That's about 3 hours of the 500-sensor pilot and roughly 30 MB of memory. After it, 2,214 were published and 2,214 stored.

The queue is still in memory (`persistence false`), so a broker restart loses it. Turn persistence on, with a volume, before relying on it in production.

Check for this: whenever a reliability claim depends on the broker holding messages, look up the queue limits and test with a backlog bigger than them.

## Related
- [Write every reading to a local spool first, so one path covers normal running and DB outages](bridge-writes-to-a-local-spool-first.md)
- [Events arrive at least once; claim the id with a conditional write before acting](at-least-once-events-need-idempotent-consumers.md)
