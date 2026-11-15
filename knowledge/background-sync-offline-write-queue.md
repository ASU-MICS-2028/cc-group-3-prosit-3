---
title: Queue offline writes in IndexedDB and replay with Background Sync
tags: [lab, prosit-1]
source: Lab 4 Homework Extension and report prompts
---

A POST made offline is stored locally (IndexedDB, e.g. via idb) and replayed by the Background Sync API when connectivity returns. The report must state a conflict-resolution strategy; last-write-wins documented as a known limitation is acceptable.

Same idea as sensor store-and-forward at the edge.

## Related
- [Service worker plus manifest gives an installable, offline-rendering app shell](service-worker-cache-first-offline-shell.md)
- [Add a dead-letter queue and make consumers idempotent](dead-letter-queue-and-idempotent-consumers.md)
