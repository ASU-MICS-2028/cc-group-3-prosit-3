---
title: Pick consistency or availability by what a wrong answer costs (bank vs social media)
tags: [lecture, databases, reliability]
source: Lecture 5; Lecture 6
---

When a network partition splits two replicas, you choose between refusing requests (consistency) and answering with possibly stale data (availability).

- **Bank: choose consistency.** Account shows 1,000 cedis on both servers. The link breaks, 200 is withdrawn at location A. If B stays "available" it still shows 1,000 and allows another withdrawal; reconciliation later finds the money was paid twice. This is why ATMs often refuse service when the network is down.
- **Social media: choose availability.** An out-of-date profile picture for a few minutes harms nobody, so replicas keep serving and catch up later.
- **Both C and A, no partition tolerance:** only affordable for very high-budget systems (lecturer's example: military).

Rule of thumb: ask "what is the damage if two users see different data?" Money or safety means consistency; convenience means availability.

For SmartCity Accra: a dashboard showing PM2.5 a few seconds late is fine (favour availability), but a flood alert must not be lost or duplicated inconsistently, and billing or quota counters need consistency.

## Related
- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)
- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)
