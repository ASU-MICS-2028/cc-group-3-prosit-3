---
title: Team IAM with a group, PowerUser, and a ForceMFA deny policy
tags: [iam, security, prosit-1]
source: Prosit 1 docs/ci-cd-and-operations.md (section 5)
---

Prosit 1 scripted team access: one IAM group, AWS-managed `PowerUserAccess` (everything except IAM administration), `IAMUserChangePassword`, and a custom `ForceMFA` policy that denies every action except the MFA setup actions until `aws:MultiFactorAuthPresent` is true. Individual users got generated passwords with mandatory reset, written to a restricted local folder, never the repo. Root is protected with MFA.

Consequence seen in Prosit 2: logins were per person with MFA, so on a deadline night nobody else could reach the team account. Agree who has access, and that at least two people can deploy, before a crunch.

SmartCity: reuse the script; add every member the first week.

## Related
- [What slowed the team down in Prosits 1 and 2, and how to avoid it in Prosit 3](what-slowed-the-team-down.md)
- [Least privilege in practice: one IAM role per job, each permission naming one resource](least-privilege-one-role-per-job.md)
