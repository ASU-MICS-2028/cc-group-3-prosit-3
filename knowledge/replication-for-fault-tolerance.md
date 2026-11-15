---
title: Replication keeps data safe when a server fails, at the cost of duplicates
tags: [lecture, reliability, storage]
source: Lecture 5
---

Duplicate data wastes space, but some duplication is deliberate: a distributed system is made fault tolerant by keeping copies on several servers, so that if one breaks another has the same data and takes over.

Example from the lecture: Google keeps every piece of data replicated three times (triple replication), so a single server loss loses nothing.

Replication is also why container images are rebuilt and copied to as many nodes as demand needs. Copies must stay in sync, which is where [cap-theorem.md](cap-theorem.md) bites: during a network split you must choose consistency or availability.

For SmartCity Accra: replicate the broker and the time-series database across availability zones in af-south-1 so one zone failure does not drop sensor data.

## Related
- [CAP theorem - a distributed system can guarantee only two of consistency, availability, partition tolerance](cap-theorem.md)
- [Google File System splits data into 64 MB chunks with a lightweight metadata master](gfs-chunking-and-lightweight-master.md)
