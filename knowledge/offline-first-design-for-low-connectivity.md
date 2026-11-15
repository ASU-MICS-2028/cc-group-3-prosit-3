---
title: Offline-first design for unreliable connectivity
tags: [edge, iot, cloud-basics]
source: Lecture 7; Lecture 5; Lecture 6
---

A Prosit 1 team designed around four rules that carry over to any intermittent-network system:
1. The app never waits for the network: it works offline and syncs later.
2. The client assigns every record a permanent ID, so a retry can never create a duplicate.
3. Nothing private faces the internet.
4. Pay only for what you use (small instances, auto scaling).

Supporting techniques they described: cache the app shell, save drafts to an on-device database every few seconds, a single sync worker at a time so foreground and background sync do not collide, and shrinking uploaded photos to about 100 KB or less (a trade-off against model accuracy that they judged acceptable).

For SmartCity Accra: sensor nodes and gateways should buffer readings, attach unique message IDs, and resend safely, so a dropped link does not lose or double-count data.

**Also (Lecture 5; Lecture 6):** Design so most functions work without internet: keep a local cache on the device, and push or pull changes when a connection is available. The lecturer's analogy is Google Maps: downloaded maps work offline, but live updates such as a new road block only arrive when you reconnect.

Reason in the course project: rural users have intermittent 2G/3G and costly data, so a live-only app would not work. Redis was mentioned as a caching tool that helps here.

For SmartCity Accra: edge gateways should buffer sensor readings locally during an outage and forward them later; the lesson maps directly onto store-and-forward at the edge.

## Related
- [AgroConnect picked af-south-1 by measuring latency from Ghana (74 ms median)](agroconnect-region-selection-by-latency.md)
- [Keep a human approving high-stakes ML recommendations](human-in-the-loop-ml-recommendations.md)
- [Offline sync needs a conflict resolution strategy, like merging in Git](offline-sync-conflict-resolution.md)
- [Core PWA technologies are the service worker, web app manifest and cache API](pwa-core-technologies.md)
