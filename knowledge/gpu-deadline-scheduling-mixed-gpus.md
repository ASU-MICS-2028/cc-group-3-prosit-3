---
title: Deadline-aware GPU scheduling across mixed GPU types
tags: [ml, cost, lecture]
source: Lecture 9
---

A reviewed paper (Dancer) schedules ML training jobs across a pool of different GPUs (for example A100 and T4) by deadline. It uses pricing to accept or reject jobs, and places jobs in powers-of-two GPU counts to avoid fragmentation (leftover GPUs that no job can use).

Reported: about 8 of 10 deadlines met versus about 5 of 10 for the elastic baseline. A reviewer found an error in the authors' example diagram and noted they measured success by training rounds rather than reaching target accuracy.

The instructor compared the slow-start then fast pattern to Ghana's base-load versus peaker power plants.

For SmartCity Accra: relevant if ML training is scheduled on cheaper GPU or spot capacity.

## Related
- [Federated learning with edge-level averaging keeps data local](federated-learning-at-the-edge.md)
- [Dynamic VM scheduling by chaining five existing algorithms](dynamic-vm-scheduling-five-algorithms.md)
