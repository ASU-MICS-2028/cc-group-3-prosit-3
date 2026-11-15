---
title: Keep servers and databases in private subnets behind the load balancer
tags: [networking, security, aws]
source: Lecture 7
---

Design rule from a Prosit 1 presentation: only the load balancer is public; application servers, database and everything else sit in private subnets across two availability zones.

Why: security groups alone already protect instances in a public subnet, but a private subnet adds a second layer. Instances can be configured to accept traffic only from the load balancer, so there is no route to them from the internet at all.

The same team also:
- put a rate limiter in front of the load balancer to cut off request floods,
- disabled SSH entirely and used SSM Session Manager when a shell on an instance was needed,
- enforced HTTPS everywhere with certificates from ACM,
- limited each field agent to seeing only their own farmers.

For SmartCity Accra: the MQTT broker and database should not be reachable directly; devices connect through a controlled public endpoint only.

## Related
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)
- [Geography-aware networking and CDNs](geography-aware-networking-and-cdns.md)
