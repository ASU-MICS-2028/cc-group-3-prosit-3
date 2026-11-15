---
title: Scale out vs up, and lead, lag or match capacity strategies
tags: [scaling, cloud-basics]
source: Study Session 1
---

Scaling: handling more or less demand. Horizontal: add or release resources of the same type (scale out/in). Vertical: replace with a bigger or smaller one (scale up/down).
Capacity planning: meeting future demand. Lead strategy adds capacity ahead of demand; lag adds when full; match adds in small steps as demand rises.
For Prosit 3 auto-scaling, target tracking is a match strategy; scheduled scaling is a lead strategy.

## Related
- [Cloud benefits (responsiveness, lower upfront cost, availability) and risks (trust boundaries, lock-in, cost overruns)](cloud-benefits-and-risks.md)
- [Virtualization turns physical resources into virtual ones; a hypervisor manages the VMs](virtualization-and-hypervisor.md)
