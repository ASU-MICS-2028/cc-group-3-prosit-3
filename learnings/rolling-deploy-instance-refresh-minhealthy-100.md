---
title: Roll servers with instance refresh at MinHealthy 100 and MaxHealthy 200 to avoid downtime
tags: [ci-cd, reliability, prosit-1]
source: Prosit 1 docs/ci-cd-and-operations.md (section 3)
---

Prosit 1's deploy pushed an image tagged both `:latest` and the commit SHA, then started an Auto Scaling Group instance refresh. The first setting (50% minimum healthy) rounded down to zero with a single instance and took the API offline for minutes on each deploy.

Working settings: `MinHealthyPercentage 100`, `MaxHealthyPercentage 200`, `InstanceWarmup 180`. Launch the replacement first, wait for it to pass the ALB `/health` check, then terminate the old one.

AWS allows only one refresh per ASG at a time. `terraform apply` on a launch template starts its own refresh; the deploy workflow catches `InstanceRefreshInProgress` and retries every 15 s for up to 30 minutes, then starts its own so instances boot with the new image. The workflow polls until Successful and fails on cancelled or rolled-back.

The SHA tag gives auditability and a quick rollback.

## Related
- [CI/CD shape that worked: test everything, scan, then deploy only what changed on merge to main](cicd-pipeline-shape-test-scan-deploy-changed.md)
- [AgroConnect scales on ALBRequestCountPerTarget (500 per minute), not CPU](../knowledge/agroconnect-target-tracking-request-count-decision.md)
