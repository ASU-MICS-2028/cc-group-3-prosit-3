---
title: Lab 5 - VPC, load balancer and multi-country data residency (Prosit 1 wrap-up)
tags: [lab, prosit-1, networking]
source: Lab 5 handout (week05_lab_Students); Prosit 2 knowledge/labs.md
---

Week 5, 3 h, team. Closes Prosit 1 with the final AgroConnect package.

**Objectives:** VPC with public and private subnets across two AZs; route tables that really enforce the boundary; a load balancer with health-check failover; database moved to a private subnet; a legally grounded data-residency and sharding design; consolidate five weeks into one package.

**Parts:** A VPC (10.0.0.0/16, four /24 subnets, IGW, NAT) plus verify_subnet_isolation.sh. B private DB, two service instances, ALB checking /health, test_load_balancer.sh before and after stopping one instance. C one-page residency plan (Ghana plus Nigeria or Kenya, sharding key, applicable law, what still needs legal review). D decommissioning checklist.

**Deliverables:** subnet and route-table evidence; target-health screenshots before and after failover; residency PDF; checklist and spend; 300-word report, consolidated diagram, links, retrospective (before Week 6).

**Rubric:** VPC segmented, DB not public 20%; LB failover 15%; residency design 20%; offline PWA 15%; retrospective 20%; decommissioning 10%.

Extension: CDN measurement on Slow 3G, egress rule audit, NAT cost comparison, second-country database.

**Also (Prosit 2 knowledge/labs.md):** Parts: A one VPC with 2 public and 2 private subnets in 2 AZs, IGW for public and NAT for private, proof by route-table script that the database subnet has no internet route; B a private database plus 2 service instances behind a load balancer health-checking `/health`, with target-health screenshots (both healthy, then one unhealthy after stopping it) and before/after `test_load_balancer.sh` output; C a one-page residency design for Ghana plus Nigeria or Kenya (sharding key, data-protection law per country, one concrete way to respect it); D decommissioning (inventory in the cost tracker, delete unused NAT Gateways, log spend).

Report: 300 words, a consolidated architecture diagram with public/private boundaries, screenshots, one honest retrospective paragraph, single PDF. Rubric: VPC 20, failover 15, residency 20, offline PWA 15, retrospective honesty 20, decommissioning 10.

Lessons: "all targets unhealthy" is usually a security group not allowing the ALB; a stopped RDS restarts after 7 days. Homework ideas: CDN before/after on Slow 3G, egress audit, NAT Gateway versus instance cost.

## Related
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [Verify subnet isolation from the route table, do not trust labels](verify-private-subnet-has-no-internet-gateway-route.md)
- [Test load-balancer failover by stopping an instance](load-balancer-health-check-failover-test.md)
- [Data residency plan - shard by country and keep personal data in its home region](data-residency-plan-sharding-by-country.md)
- [Lab 6 - least-privilege IAM, encryption, FHIR-aligned schema and audit logging](lab-6-iam-encryption-fhir-audit-logging.md)
- [Cost tracking and teardown: what keeps billing and what to delete by hand](../learnings/cost-tracking-and-teardown-checklist.md)
