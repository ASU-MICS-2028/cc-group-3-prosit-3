---
title: Data residency plan - shard by country and keep personal data in its home region
tags: [data-governance, privacy, databases]
source: Lab 5 Part C; Lecture 6
---

One-page plan: countries (Ghana plus Nigeria or Kenya), sharding key (e.g. one DB per country routed by a country field), the specific data protection law for each, and one concrete way the design respects it (PII stays in-country, only anonymized aggregates replicated centrally). State what still needs real legal review.

Cross-region reports become federated queries; identify where.

SmartCity Accra: sensor readings are not personal, but any resident-linked data needs the same thinking.

**Also (Lecture 6):** The Prosit 1 week-2 scope: extend a system across several countries with regional data-protection compliance (each country has its own law), shard databases by country for performance and compliance, an API gateway per country, load balancing with CDN, multi-country monitoring, and disaster recovery across data centres.

For SmartCity Accra: keep resident-related data in the region (af-south-1) and plan backup and monitoring across zones.

## Related
- [FHIR-shaped schema now, with a written gap list for real interoperability](fhir-aligned-schema-with-gap-analysis.md)
- [Lab 5 - VPC, load balancer and multi-country data residency (Prosit 1 wrap-up)](lab-5-vpc-load-balancer-data-residency.md)
- [Data-intensive computing moves work to data spread across servers, not data into one machine's RAM](data-intensive-computing-distribute-chunks.md)
- [Replication keeps data safe when a server fails, at the cost of duplicates](replication-for-fault-tolerance.md)
