---
title: Put the database in a private subnet with no public access
tags: [networking, security, databases]
source: Lab 4 Part A; Lab 5 Part B
---

Create managed databases (RDS, Azure Flexible Server, Cloud SQL) with public access off, reachable only from the app tier's security group or private IP (not "allow all", not just your laptop). Never open it publicly "to make testing easier".

Lab 5 makes moving the DB private a required fix; it can break things that quietly relied on the flat network. Store the endpoint and credentials in env vars or a secrets manager, not in code.

SmartCity Accra: time-series store and metadata DB belong in private subnets.

## Related
- [Verify subnet isolation from the route table, do not trust labels](verify-private-subnet-has-no-internet-gateway-route.md)
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [Inside a container, localhost is the container itself](localhost-inside-a-container-is-the-container.md)
