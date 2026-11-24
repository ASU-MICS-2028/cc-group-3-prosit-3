---
title: Paho raises on publish while the broker is down; catch it or the sensor dies
tags: [iot, mqtt]
source: PR for #18 (sensors/simulator.py)
---

With paho-mqtt 2.x, `publish(...).wait_for_publish()` raises `RuntimeError: The client is not currently connected` if the broker has gone away. Uncaught, one broker restart kills every simulated device. We tested it by stopping the Mosquitto container for 5 s during a run.

What works: connect with `connect_async` + `loop_start` (paho reconnects by itself), wait up to a few seconds for the first connection so the first readings aren't lost, and catch the error per reading. The simulator drops that reading and logs it; `seq` keeps counting, so the outage shows downstream as a gap (in our run `seq` went 2 → 10). Real buffering belongs in the bridge, which must survive the DB going down.

## Related
- [Ids created on the device make offline retries idempotent](client-generated-uuids-make-retries-safe.md)
- [The outbox gap: saving data then publishing can lose the event](outbox-pattern-for-lost-events.md)
