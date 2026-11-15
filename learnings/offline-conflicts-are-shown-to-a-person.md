---
title: Offline app design: save locally first, encrypt, queue, and let a person settle conflicts
tags: [edge, security, prosit-2]
source: Prosit 2 learnings/frontend.md (FB-3 and FB-4); Prosit 2 docs/decisions.md D-031
---

HealthConnect's phone app: every write is one IndexedDB transaction holding the record, its "to send" entry and its audit entry. Records are encrypted with a random key locked by a 10+ character passphrase (PBKDF2, 600,000 rounds), typed only on a cold start; a 4 to 6 digit PIN only opens the 5-minute screen lock. Five wrong tries wipe local data.

Sync goes oldest first and runs after every save, when signal returns and every 20 seconds. If the other side changed the same record, nothing is overwritten: a person chooses "keep mine" or "use theirs". A booking lost to another phone is kept as "Needs attention" with "choose another time". A 503 from the API is treated like a network error.

Bugs the tests found: a save during a send waited up to 20 s; a send requested as an offline round ended was dropped; screens did not refresh after a download; a 1 MB photo crashed base64 conversion in one call (chunk it).

SmartCity relevance: gateways or field apps that buffer sensor data offline need the same retry, ordering and conflict rules.

## Related
- [Sync downloads with a running-number bookmark can skip records unless numbering is ordered](sync-bookmark-lock-avoids-skipped-records.md)
- [Drain the offline queue in the background, with a Web Lock so only one runner sends](background-sync-with-web-locks.md)
