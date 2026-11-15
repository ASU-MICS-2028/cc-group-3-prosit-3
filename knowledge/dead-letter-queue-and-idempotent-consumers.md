---
title: Add a dead-letter queue and make consumers idempotent
tags: [event-driven, reliability]
source: Lab 7 Homework Extension and report prompt
---

Failed events should land in a DLQ, not vanish: break the function on purpose and confirm. Delivery can repeat, so publish the same event twice and check you do not act twice; fix with a processed-events table.

Open question from the lab report: how would you notice a reminder function failing silently?

SmartCity Accra: duplicate or malformed sensor messages are expected.

## Related
- [Publish one event, let independent functions react](publish-one-event-two-independent-consumers.md)
- [Queue offline writes in IndexedDB and replay with Background Sync](background-sync-offline-write-queue.md)
