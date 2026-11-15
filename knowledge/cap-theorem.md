---
title: CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance
tags: [lecture, databases, reliability]
source: Lecture 5; Lecture 6
---

CAP says a distributed data system cannot have all three of: **Consistency** (every replica shows the same data), **Availability** (the system answers requests), and **Partition tolerance** (it keeps working when the network between nodes breaks).

Partition tolerance is not optional in the cloud: networks fail, so the real design choice is what to give up when a partition happens, consistency or availability. The lecturer stressed that "partition" means survival of a failure, not routine network splitting.

The formal proof is by contradiction (a paper by Brewer was promised); the intuition is the bank example in [cap-choice-bank-vs-social-media.md](cap-choice-bank-vs-social-media.md).

Why it matters for SmartCity Accra: sensor readings are replicated across brokers, databases and regions, so we must decide per component whether stale-but-available or correct-but-blocked is acceptable.

Quick recap from Lecture 6: banking systems pick consistency, social media picks availability, and systems that must be both always consistent and always available (the lecturer's example was military) are extremely expensive.

## Related
- [Pick consistency or availability by what a wrong answer costs (bank vs social media)](cap-choice-bank-vs-social-media.md)
- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)
