---
title: Amdahl's law - the serial portion caps speedup no matter how many cores you add
tags: [lecture, scaling]
source: Lecture 5; Lecture 4
---

If a fraction P of a task can run in parallel and the rest (1 - P) is serial, speedup on N processors is:

`speedup = 1 / ((1 - P) + P / N)`

As N grows, P/N goes to 0, so the limit is `1 / (1 - P)`. Adding hardware never beats that ceiling.

Worked example from the lecture: P = 0.9, so the serial part is 0.1. With N = 4: 0.9/4 = 0.225, plus 0.1 = 0.325, speedup about 3.08. With 8, 16, 32 and more cores speedup keeps rising but can never exceed 1/0.1 = **10x**.

Lesson: to go faster, shrink the serial part (better data layout, algorithms, storage design, as Google did with its file system) instead of only buying more machines. The lecturer said exam-style questions will include calculations like this.

For SmartCity Accra: scaling out ingest workers helps only the parallel part; a single-writer database or single broker is the serial bottleneck.

**Also (Lecture 4):** Sequential code runs step by step; independent work can be split across nodes. Example: a loop of 100,000 iterations can be divided among 100 nodes, 1,000 each, and run at the same time, with communication overhead adding some time.

Amdahl's law: the sequential portion of a program limits total speedup; adding nodes only speeds up the parallelizable portion. For the sequential part, better data structures and algorithms (time and space complexity) are the tool. MATLAB's parallel toolbox was mentioned as an example.

For SmartCity Accra: batch ML training or feature calculations can be parallelized; the serial parts set the ceiling.

## Related
- [Google File System splits data into 64 MB chunks with a lightweight metadata master](gfs-chunking-and-lightweight-master.md)
- [Big data is described by Volume, Velocity, Variety (and Veracity)](big-data-four-vs.md)
- [Distributed computing spreads work over many sites with a master node coordinating](distributed-computing-master-node-map-reduce.md)
- [A cluster is many servers stacked together; heavy jobs like LLM training rent whole clusters](compute-clusters-for-heavy-workloads.md)
