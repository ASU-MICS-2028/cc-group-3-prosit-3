---
title: Per-service idle timeouts instead of one global timeout
tags: [networking, scaling, lecture]
source: Lecture 9
---

Idle connections still consume memory. The Alibaba paper measured about 4 GB of memory per 100 million requests held by idle balancer state, which hurt at peak hours.

A single global timeout is a blunt tool: it can cut live sessions or keep dead ones. The paper's fix was a timeout per service, with the component sending a TCP reset (RST) when a connection has been idle too long so both ends can free it.

General lesson: tune timeouts per workload. For SmartCity Accra, an MQTT broker keeping many mostly-quiet sensor connections open needs keep-alive and timeout settings chosen for the reporting interval of each device type.

## Related
- [Alibaba's next-generation load balancer takes the data path out of the balancer](nglb-full-bypass-load-balancer.md)
