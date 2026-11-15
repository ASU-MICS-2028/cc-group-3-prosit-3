---
title: Use terraform apply -target for a one-off change, then do the full apply later
tags: [iac, prosit-2]
source: Prosit 2 learnings/infra.md (sections 2 and 6)
---

`terraform apply -target=module.events` changes only that module. Prosit 2 used it twice: once so the alarm-email subscriptions (which had lapsed) were not re-created and re-sent, and again for the PWA hosting (`-target=module.frontend -target=module.cicd`) when the certificate had to exist and be validated first.

Caveats the team noted:
- `-target` is for exceptions. The next full apply still carries everything that was skipped, so plan for that day (for example, confirm emails that day).
- For a certificate-gated resource, apply the certificate first, add the DNS validation record at the DNS host, then apply the rest.

SmartCity use: a staged first deploy (certificate, then load balancer, then compute) is a normal pattern.

## Related
- [Never stop a terraform apply half-way; recover with force-unlock and import](terraform-interrupted-apply-recovery.md)
- [HTTPS on the ALB with an ACM certificate when DNS lives outside Terraform](https-acm-certificate-with-external-dns.md)
