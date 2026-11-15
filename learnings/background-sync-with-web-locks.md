---
title: Drain the offline queue in the background, with a Web Lock so only one runner sends
tags: [edge, reliability, prosit-1]
source: Prosit 1 docs/architecture-decisions.md ADR-012
---

Problem: a PWA only syncs while its tab is open, so queued registrations stay stranded if the user never reopens it; but if the browser also wakes the service worker, the UI thread and the worker could both drain the same IndexedDB queue and double-send.

AgroConnect's answer: a custom service worker (`injectManifest`) with a `sync` listener and the tag `agroconnect-sync`; both the in-app runner and the worker take the same exclusive Web Lock (`navigator.locks.request`) before touching the outbox. Holding the lock means anything in `sending` state is stale and can safely be reset to `saved`. The worker reads the saved token and calls `/auth/refresh` on a 401. Failing the `sync` event makes the browser back off.

Limits: Background Sync works on Chromium Android, not iOS Safari or desktop Firefox, where it falls back to foreground sync.

## Related
- [Offline app design: save locally first, encrypt, queue, and let a person settle conflicts](offline-conflicts-are-shown-to-a-person.md)
- [Ids created on the device make offline retries idempotent](client-generated-uuids-make-retries-safe.md)
