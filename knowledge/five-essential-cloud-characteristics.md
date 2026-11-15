---
title: Five essential characteristics of cloud computing
tags: [cloud-basics, lecture]
source: Lecture 2; Study Session 1
---

From the NIST definition:

1. On-demand self-service: you provision resources yourself, anywhere, without talking to a person. This only works if the provider is highly available and reliable (redundancy built in, data centres powered 24/7).
2. Broad network access: reachable over the network from many device types.
3. Resource pooling: resources are shared across customers (multi-tenancy).
4. Rapid elasticity: capacity grows and shrinks with demand.
5. Measured service / pay as you use: you pay only for what you use; idle means no charge.

Example given: a shop whose sales spike in December. Buying fixed servers for the peak leaves them idle the rest of the year; elastic cloud capacity avoids that.

For SmartCity Accra: elasticity and pay-per-use justify auto-scaling the ingestion and ML tiers instead of sizing for peak.

**Also (Study Session 1):** 1. On-demand self-service: provision a VM any time.
2. Broad network access: over standard internet protocols.
3. Resource pooling (multi-tenancy): VMs share physical hosts with other customers.
4. Rapid elasticity: capacity appears unlimited and can be provisioned in any quantity at any time.
5. Measured service (pay per use): every byte stored and second of compute is metered.

Relevance: auto-scaling and cost tracking in Prosit 3 rest on points 4 and 5. Cloud is a specialised distributed computing model for remotely provisioning scalable, measured resources.

## Related
- [Capex versus opex - why elastic cloud capacity beats owned servers](capex-vs-opex-elasticity.md)
- [NIST definition of cloud computing (SP 800-145)](nist-cloud-definition.md)
- [IaaS, PaaS, SaaS - control versus convenience](iaas-paas-saas-control-vs-convenience.md)
- [Cloud benefits (responsiveness, lower upfront cost, availability) and risks (trust boundaries, lock-in, cost overruns)](cloud-benefits-and-risks.md)
