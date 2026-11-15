---
title: In-memory data in a container is lost on restart; make it persistent
tags: [lecture, containers, storage]
source: Lecture 5
---

In Lab 3 the microservice held data in memory inside a container. That is fine for a demo but the data disappears when the container stops. Persistent data means it survives shutdown, which requires a real database or attached storage.

The next lab (Lab 4) moves this data into a managed database and object storage, which is also the step that lets a progressive web app work offline and sync later.

For SmartCity Accra: never keep sensor readings only in a service's memory or container filesystem; write them to the time-series database or object store.

## Related
- [Lab 4 - managed Postgres, private object storage and an offline-capable PWA](lab-4-managed-database-storage-offline-pwa.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
