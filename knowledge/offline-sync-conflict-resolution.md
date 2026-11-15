---
title: Offline sync needs a conflict resolution strategy, like merging in Git
tags: [lecture, edge, databases]
source: Lecture 6
---

If users change data offline on a phone and the server also changes, the two copies diverge. An offline-first design therefore needs a synchronization strategy with conflict resolution: decide how changes are merged, similar to resolving merge conflicts in GitHub.

Lab 4 asked for a first offline capability of the PWA backed by a managed database and object storage.

For SmartCity Accra: when a gateway uploads buffered readings after an outage, use timestamps and device IDs so duplicates and late arrivals are merged rather than overwritten.

## Related
- [Offline-first design for unreliable connectivity](offline-first-design-for-low-connectivity.md)
- [Core PWA technologies are the service worker, web app manifest and cache API](pwa-core-technologies.md)
- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)
