---
title: History of computing - heavy lifting keeps moving to the provider
tags: [cloud-basics, lecture]
source: Lecture 2
---

Timeline from the lecture:

- 1960s: mainframe time-sharing, many users on one expensive machine (like a telephone exchange sharing lines).
- 1990s: client/server; organisations own servers and capacity on premises.
- Around 2000: virtualization matures (VMware, Xen): one physical machine hosts many isolated VMs, each with its own OS.
- 2006: AWS launches S3 and EC2, so anyone with a card can rent storage and compute by the hour.
- Around 2010: PaaS and containers (Heroku, Docker, Kubernetes) make deployment faster and portable.
- Around 2014 onward: event-driven serverless (AWS Lambda), paying per function invocation not per server.

Pattern: undifferentiated heavy lifting moves from you to the provider. Use this as the lens for every service decision.

## Related
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Serverless - pay per function invocation, not per server](serverless-pay-per-invocation.md)
- [Capex versus opex - why elastic cloud capacity beats owned servers](capex-vs-opex-elasticity.md)
