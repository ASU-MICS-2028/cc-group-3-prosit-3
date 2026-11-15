---
title: Lab 4 - managed Postgres, private object storage and an offline-capable PWA
tags: [lab, prosit-1, databases]
source: Lab 4 handout (week04_lab_Students); Lecture 6
---

Week 4, 3 h, team. Prosit 1 storage and offline.

**Objectives:** managed relational DB (RDS / Azure Flexible Server / Cloud SQL) plus a private bucket; a normalized schema; migrate the service from an in-memory Map to Postgres via DATABASE_URL; a service worker with cache-first behaviour; an installable web manifest; a background-sync flow for offline writes.

**Parts:** A database (db.t3.micro, not publicly accessible, only the VM's security group). B object storage (private by default). C migrate the service and prove a record survives a container restart. D PWA shell (manifest.json, sw.js, DevTools Offline check, Lighthouse PWA audit).

**Deliverables:** DB and bucket screenshots with team tag; restart-persistence output; offline-render screenshot plus Lighthouse score; 300-word report (SQL vs NoSQL, cache strategy, conflict resolution) before Week 5.

**Rubric:** DB and storage private 20%; persistence across restarts 25%; service worker and manifest 30%; report reasoning 25%.

Extension: IndexedDB write queue replayed by Background Sync, a second table with a JOIN, 5-minute signed upload URL.

**Also (Lecture 6):** Lab 4 builds on the Lab 3 profile microservice. Needs: cloud CLI and console from earlier labs, a Postgres client (psql, DBeaver or pgAdmin), a Postgres driver for the team's language, and the team's chosen cloud (AWS, Azure or GCP). Steps include printing the schema (name, phone, region, language), provisioning the managed database (about 20 minutes), populating it, then adding the PWA manifest and service worker.

Prerequisite stressed: reasonable skill in one language (Python, Java or C++).

## Related
- [Put the database in a private subnet with no public access](database-in-private-subnet-no-public-access.md)
- [Service worker plus manifest gives an installable, offline-rendering app shell](service-worker-cache-first-offline-shell.md)
- [Queue offline writes in IndexedDB and replay with Background Sync](background-sync-offline-write-queue.md)
- [Use short-lived pre-signed URLs with a private bucket](presigned-url-upload-to-private-bucket.md)
- [Block, object and file storage serve different jobs](block-object-file-storage.md)
- [Core PWA technologies are the service worker, web app manifest and cache API](pwa-core-technologies.md)
- [In-memory data in a container is lost on restart; make it persistent](persistent-data-vs-in-memory-containers.md)
