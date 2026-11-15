---
title: Google File System splits data into 64 MB chunks with a lightweight metadata master
tags: [lecture, storage, scaling]
source: Lecture 5
---

The GFS cost model idea: break all data into fixed-size chunks (64 MB), replicate each chunk across servers, and keep a **master** that stores only metadata (where each chunk lives), not the data itself. Because the master is lean it can answer lookups fast, which is part of why Google search returns instantly.

Chunk size was chosen by optimization (finding the best use of resources under constraints), not guesswork.

Why it matters: it shrinks the serial bottleneck from [amdahls-law.md](amdahls-law.md) by organizing storage so many machines can work in parallel. It also sets up MapReduce, which the lecturer said comes in the last part of the course.

For SmartCity Accra: the same pattern appears as object storage plus an index or catalogue for archived sensor data.

## Related
- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)
- [Data-intensive computing moves work to data spread across servers, not data into one machine's RAM](data-intensive-computing-distribute-chunks.md)
