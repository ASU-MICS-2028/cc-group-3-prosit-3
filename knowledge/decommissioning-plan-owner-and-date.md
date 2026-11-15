---
title: Write the teardown plan now: resources, one named owner, 48-hour deadline after grades
tags: [lab, cost, process]
source: Lab 14 (week14_lab_Students) Part E; Lab 5 Part D; Lab 9 Part E
---

Graders need the three Prosits running, so tear down only after grades are confirmed. The plan lists every live resource across all Prosits and cloud accounts, names one owner to tear down within 48 hours of grades (compute, load balancers, NAT gateways, databases deleted or exported first), decides whether anything is kept downsized for a portfolio, and schedules a billing check one week later. Worth 5% of the final project.

**Also (Lab 5 Part D; Lab 9 Part E):** At each prosit boundary: list every running resource in the Cost_Tracking_Template inventory; decide what must stay for grading; stop compute not needed (a stopped instance costs almost nothing, restartable for a grader); delete hourly-billed items such as NAT gateways; confirm non-primary accounts are empty; log month-to-date spend weekly.

Lab 9 adds: stopping a DB does not delete the data, so write a one-sentence retention/erasure policy.

SmartCity Accra: Week 11 cost work builds on these weekly numbers.

## Related
- [Lab 14 overview: advanced feature test, capstone integration, final architecture doc, presentation](lab-14-advanced-feature-capstone-final-presentation.md)
- [Four acceptable optimizations: right-size, cheaper storage tier, delete unused, scheduled shutdown](cost-optimization-options-right-size-tier-delete-schedule.md)
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](../learnings/fck-nat-vs-nat-gateway.md)
- [Audit running compute on all three clouds before milestones](cross-provider-resource-audit-script.md)
- [Tag and name every cloud resource with the team name](tag-every-resource-with-team-name.md)
