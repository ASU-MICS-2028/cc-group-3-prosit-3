---
title: Every cloud account gets MFA and a $5 billing alert on day one
tags: [cloud-basics, security, cost]
source: Lab 0 Part A; Lab 1 Part A
---

Before provisioning anything, enable MFA on the root/owner login (authenticator app preferred over SMS) and create a budget alert (the labs use $5/month, alert at 80% on AWS). Do it on AWS (Budgets), Azure (Cost Management budgets) and GCP (Billing budgets and alerts).

Why: most surprise-bill stories start with skipping this step; free tiers are easy to exceed by leaving a VM or NAT gateway running.

SmartCity Accra: af-south-1 resources with sensors, brokers and ML are costlier than earlier prosits, so the alert matters more.

Free-tier terms noted in Lab 0: AWS 12 months of free-tier services; Azure $200 for 30 days plus 12 months of popular services; GCP $300 for 90 days plus an always-free tier.

## Related
- [Do daily work as a non-root IAM user, never the root account](never-use-root-account-for-daily-work.md)
- [If MFA codes are rejected, check the device clock](mfa-codes-rejected-check-device-clock.md)
- [Write the teardown plan now: resources, one named owner, 48-hour deadline after grades](decommissioning-plan-owner-and-date.md)
