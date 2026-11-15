---
title: Data-intensive computing moves work to data spread across servers, not data into one machine's RAM
tags: [lecture, scaling, databases]
source: Lecture 5
---

On a laptop you load data into RAM, and for bigger data you buy more RAM. That does not scale to internet-size data. The approach taught: take data in whatever form it arrives, split it into chunks, distribute the chunks across servers in different zones or regions, and replicate them for tolerance and backup.

Four ideas the lecturer named as the base before MapReduce: the Vs of big data, the GFS cost model, Amdahl's law, and CAP.

Warning given: an architecture that handles about 15,000 users will not survive hundreds of thousands across several countries; scalability needs a rethink, not just a bigger box.

For SmartCity Accra: partition sensor data by time and region, and plan for city-wide growth from the start.

## Related
- [Big data is described by Volume, Velocity, Variety (and Veracity)](big-data-four-vs.md)
- [Google File System splits data into 64 MB chunks with a lightweight metadata master](gfs-chunking-and-lightweight-master.md)
- [Amdahl's law - the serial portion caps speedup no matter how many cores you add](amdahls-law.md)
