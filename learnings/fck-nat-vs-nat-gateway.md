---
title: fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month
tags: [cost, networking, prosit-1, prosit-2]
source: Prosit 1 docs/cloud-infrastructure.md; Prosit 2 learnings/infra.md (section 3); Lecture 7; Lab 5 Part D and Troubleshooting; Lab 9 Part E
---

Private subnets need a NAT to reach the internet (pulling images, updates, outbound APIs). Both prosits used `fck-nat` on a `t4g.nano` (about $3/month) instead of AWS's managed NAT Gateway (about $32/month plus data processing).

Trade-off: one instance, one AZ, no automatic failover. `source_dest_check` must be off on its network interface. Prosit 2 later gave the NAT box its own role allowing only SSM (it had been borrowing the API role) and drew the single NAT visibly on the architecture diagram.

When capacity for the small instance type is missing in a zone, fall back to the managed gateway and remember to delete it (and its Elastic IP) at teardown.

SmartCity: keep the cheap NAT unless the brief's availability target forces a NAT per zone; state the choice in an ADR.

**Also (Lecture 7):** Servers in a private subnet still need outbound internet access (updates, external APIs). The managed AWS NAT gateway is convenient but has a fixed hourly cost. A team in class replaced it with fck-nat, an open-source NAT instance that runs on a tiny instance (they used an ARM Graviton t4g.nano).

Figure quoted in the presentation: a NAT gateway at roughly 36 dollars a month versus about 3 dollars for fck-nat, around a 90 percent saving. Trade-off: you manage the instance, and a single small instance is a single point of failure and a throughput limit.

Their whole stack was costed at roughly 19 dollars for the load balancer plus a few dollars each for NAT, CloudWatch, database, registry and storage, which shows the load balancer is often the biggest fixed item.

For SmartCity Accra: a good cost-optimisation talking point for the cost and sustainability section.

**Also (Lab 5 Part D and Troubleshooting; Lab 9 Part E):** Private subnets need NAT to reach the internet for updates. A managed NAT Gateway costs per hour plus data processed whether used or not, and is the most common source of unexpected lab spend. A NAT instance (small VM) is cheaper but manual and a single point of failure.

Delete NAT gateways you no longer need, or stop the NAT instance. Egress rules should list only the needed external destinations.

SmartCity Accra: decide NAT type up front; consider VPC endpoints.

## Related
- [Cost tracking and teardown: what keeps billing and what to delete by hand](cost-tracking-and-teardown-checklist.md)
- [Check that a service and instance type exist in af-south-1 before designing around it](check-service-availability-in-af-south-1.md)
- [Keep servers and databases in private subnets behind the load balancer](../knowledge/private-subnets-behind-load-balancer.md)
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](../knowledge/terraform-init-plan-apply-and-import.md)
- [Write the teardown plan now: resources, one named owner, 48-hour deadline after grades](../knowledge/decommissioning-plan-owner-and-date.md)
- [VPC layout - two public and two private subnets across two AZs](../knowledge/vpc-two-az-public-private-subnet-layout.md)
