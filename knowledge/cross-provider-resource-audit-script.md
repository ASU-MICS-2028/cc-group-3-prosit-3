---
title: Audit running compute on all three clouds before milestones
tags: [cost, process]
source: Lab 8 Part C
---

A script listing running EC2 instances (describe-instances with state filter), Azure running VMs (az vm list -d) and GCP RUNNING instances. Do not delete unknown resources blindly; confirm with the team first.

SmartCity Accra: extend to load balancers, NAT gateways and databases, where cost hides.

## Related
- [Write the teardown plan now: resources, one named owner, 48-hour deadline after grades](decommissioning-plan-owner-and-date.md)
- [Tag and name every cloud resource with the team name](tag-every-resource-with-team-name.md)
