---
title: A cluster is many servers stacked together; heavy jobs like LLM training rent whole clusters
tags: [scaling, cost, lecture]
source: Lecture 4
---

A cluster is many servers (not ordinary PCs) networked together; a data center is far bigger than a node. Large language model training runs on cloud clusters for months, around the clock (the lecture said roughly three to six months), consuming a lot of energy, which is why it is expensive. Cloud providers meter server time, and sometimes credit it as a donation to partners.

Takeaway for cost and sustainability: compute running 24/7 is billed and uses power.

## Related
- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
- [Distributed computing spreads work over many sites with a master node coordinating](distributed-computing-master-node-map-reduce.md)
