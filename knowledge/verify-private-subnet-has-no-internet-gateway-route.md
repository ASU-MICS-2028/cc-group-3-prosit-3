---
title: Verify subnet isolation from the route table, do not trust labels
tags: [networking, security, aws]
source: Lab 5 Part A
---

Naming a subnet "private" proves nothing. Check with aws ec2 describe-route-tables --filters Name=association.subnet-id,Values=<id> --query RouteTables[].Routes. Public subnet: a route to an Internet Gateway. Private subnet: a NAT route or none, never an IGW.

Keep this as a small script (verify_subnet_isolation.sh) as evidence.

## Related
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [Put the database in a private subnet with no public access](database-in-private-subnet-no-public-access.md)
