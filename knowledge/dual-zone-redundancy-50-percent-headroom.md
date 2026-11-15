---
title: Dual-zone redundancy means each zone runs at about 50 percent
tags: [reliability, scaling, lecture]
source: Lecture 9
---

If two zones back each other up, each must be able to absorb the other's traffic when one fails. So in steady state each zone can use only about half its capacity. The Alibaba paper noted that traditional balancers, busy with data transfer, broke this headroom rule.

Practical meaning: high availability across availability zones costs spare capacity, so cost and resilience trade off directly. For SmartCity Accra's multi-AZ design, size each AZ to carry the full load or accept degraded service during a failure.

## Related
- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)
- [Threshold load balancing, stop at 75 percent and resume below 25 percent](threshold-load-balancing-75-25.md)
