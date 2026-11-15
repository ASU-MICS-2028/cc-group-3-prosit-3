---
title: VPC layout - two public and two private subnets across two AZs
tags: [networking, aws]
source: Lab 5 Part A; Lab 9 Part D
---

Lab 5 pattern: VPC 10.0.0.0/16; public subnets 10.0.1.0/24 and 10.0.2.0/24; private subnets 10.0.11.0/24 and 10.0.12.0/24, each pair in different AZs. Public subnets route to an Internet Gateway; private ones route to a NAT (or have no internet route). Load balancer in public, app and DB in private. Azure: VNet with app and data subnets plus NSGs; GCP: custom-mode VPC plus explicit firewall rules.

Lab 9 recreates this in Terraform (healthconnect used 10.1.0.0/16, so use a distinct range per project).

SmartCity Accra: reuse as the base network in af-south-1.

## Related
- [Verify subnet isolation from the route table, do not trust labels](verify-private-subnet-has-no-internet-gateway-route.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
- [Test load-balancer failover by stopping an instance](load-balancer-health-check-failover-test.md)
