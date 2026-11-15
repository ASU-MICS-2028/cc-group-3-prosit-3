---
title: Capture least-privilege evidence with the IAM policy simulator
tags: [iam, process, prosit-2]
source: Prosit 2 learnings/infra.md (section 4); Prosit 2 knowledge/sessions/2026-10-30-cicd-pipeline.md; Prosit 2 knowledge/labs.md (Lab 6)
---

The simulator evaluates a role's real policies and answers allowed or implicitDeny without doing anything, so it is safe evidence and repeatable. Prosit 2 wrote a script (`check_least_privilege.sh`) with 10 allow/deny checks, each line ending in PASS, and a similar 11-check run for the CI deploy role (pushes only to two repositories, refreshes only one ASG, no secrets, no database).

Lab 6's sample policy used the Aurora Data API action, which does not apply to plain RDS PostgreSQL. The team proved "allowed" with `secretsmanager:GetSecretValue` on its own secret and "denied" with `rds:DeleteDBInstance` or another project's secret.

"implicitDeny" means no policy allows the action, so AWS refuses.

SmartCity: write the checks as a script beside the Terraform, and re-run after every IAM change.

## Related
- [Least privilege in practice: one IAM role per job, each permission naming one resource](least-privilege-one-role-per-job.md)
- [Capture evidence honestly: report the real result, label what is faked, never rewrite history](honest-evidence-capture.md)
