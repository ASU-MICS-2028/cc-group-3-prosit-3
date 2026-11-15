---
title: Distributed computing spreads work over many sites with a master node coordinating
tags: [scaling, lecture]
source: Lecture 4
---

When one site lacks the compute, work is distributed across nodes in different locations. A master node coordinates, and nodes both compute and communicate results. The lecture named map-reduce as the pattern and noted that code must be written to take advantage of parallelism. Example: African genomics centers pooling clusters over fiber and submarine links to sequence the COVID virus.

## Related
- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
- [A cluster is many servers stacked together; heavy jobs like LLM training rent whole clusters](compute-clusters-for-heavy-workloads.md)
