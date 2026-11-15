---
title: Cost tracking and teardown: what keeps billing and what to delete by hand
tags: [cost, process, prosit-1, prosit-2]
source: Prosit 2 learnings/infra.md (section 6); Prosit 2 CONTRIBUTING.md; Prosit 2 knowledge/sessions/2026-10-22-lab5-submission.md and 2026-10-26-lab7-event-infra.md; Prosit 1 docs/cloud-infrastructure.md
---

Team rule: every cloud resource goes into the cost tracker the same day and is torn down when its lab is done. A budget alarm emailed everyone (Prosit 1: $100 limit; Prosit 2: $50 forecast, $100 actual).

Reference numbers: AgroConnect baseline $27-52/month; HealthConnect about $70-90/month (ALB ~$19, three t3.micro ~$28, RDS ~$16, NAT ~$3, plus public IPs and CloudWatch).

Teardown gotchas:
- Deleting an Aurora DB is two steps: the instance, then the cluster, which keeps billing for storage.
- `terraform destroy` deleted the RDS with no final snapshot (lab setting; fine only for synthetic data); the photo bucket must be emptied first.
- A NAT Gateway and Elastic IP created by hand are not in state: delete them manually.
- A stopped RDS instance restarts itself after 7 days.
- Extra servers (like the Lab 7 call server) are removed by setting their hostname variable to empty and applying.
- A second-account copy (Stockholm) needed 52 resources destroyed plus manual cleanup.

SmartCity: cost is a graded topic, so keep the tracker current from day one.

## Related
- [fck-nat instance versus managed NAT Gateway: about $3 versus $32 a month](fck-nat-vs-nat-gateway.md)
- [Unconfirmed SNS email subscriptions are silently deleted after three days](alarm-email-subscriptions-expire-after-3-days.md)
