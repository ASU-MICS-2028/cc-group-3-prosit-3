---
title: Pick one primary cloud for billable resources; keep the others empty
tags: [cost, cloud-basics, process]
source: Lab 1 Graded Deliverable
---

The course has you open AWS, Azure and GCP but choose a single primary platform for all billable compute, storage and database work from Week 2. The other two stay MFA-secured and are used only for comparisons (for example the Week 11 cost comparison) or when a lab says so.

Why: three parallel accounts triple real spend. Check non-primary accounts stay at zero resources.

The choice must be justified by at least two technical factors (latency to region, free tier, a managed service needed), and honest about familiarity bias.

SmartCity Accra brief targets AWS af-south-1.

## Related
- [Verify CLI access with one identity check per provider](verify-cli-access-to-all-three-clouds.md)
- [Every cloud account gets MFA and a $5 billing alert on day one](cloud-account-baseline-mfa-billing-alert.md)
- [Lab 1 - three cloud accounts, CLI check, console comparison, problem statement](lab-1-cloud-accounts-console-problem-statement.md)
