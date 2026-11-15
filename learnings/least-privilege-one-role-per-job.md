---
title: Least privilege in practice: one IAM role per job, each permission naming one resource
tags: [iam, security, prosit-2]
source: Prosit 2 learnings/infra.md (section 2 item 12 and section 3); Prosit 2 docs/decisions.md D-030
---

Starting state in Prosit 2: the NAT box borrowed the API servers' role, so a break-in on the NAT could read the database password and the token-signing key. Fix (L6-A1b):
- NAT instance got its own role allowing only SSM sessions.
- API role lost AWS's broad "read every ECR repository" policy and may pull only its own repository.
- Every other statement names exactly one resource: one database secret, one signing-key secret, one SNS topic, one log group, one bucket, one SSM parameter.
- Each Lambda has its own role: read only its own queue, write only its own logs.
- The call server's role: pull its image, write logs, SSM.

Two permissions cannot be narrowed: `ecr:GetAuthorizationToken` needs `*` (it only issues a login), and the SSM managed policy is kept so sessions and tunnels work.

If a scoped role breaks something, find the exact denied action in CloudTrail and add only that one.

SmartCity: give the ingest service, the ML job and each device identity separate, resource-scoped roles.

## Related
- [Capture least-privilege evidence with the IAM policy simulator](prove-iam-with-policy-simulator.md)
- [Deploy from GitHub Actions with OIDC, no stored keys, and trust only the main branch](github-oidc-deploy-role-limited-to-main.md)
