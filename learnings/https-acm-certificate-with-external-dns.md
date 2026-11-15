---
title: HTTPS on the ALB with an ACM certificate when DNS lives outside Terraform
tags: [security, networking, prosit-1, prosit-2]
source: Prosit 1 docs/architecture-decisions.md ADR-006; Prosit 2 docs/decisions.md D-022; Prosit 2 learnings/infra.md (sections 2, 4, 6)
---

Setup used twice: one ACM certificate (can cover several names) on the ALB, TLS on port 443, port 80 answering a 301 redirect to HTTPS. DNS is at the registrar (Hostinger), so the team added by hand: one CNAME per public name pointing at the ALB, plus the `_...` validation CNAMEs ACM asks for.

Gotchas:
- Use the friendly names, not the raw `...elb.amazonaws.com` address: after the redirect the certificate does not cover that name, so curl and browsers reject it.
- A brand-new DNS name can fail for a minute; retry before debugging.
- DNS is not in Terraform, so recreating the ALB or the certificate changes the targets or validation records and they must be updated by hand (`terraform output cert_validation_records`).
- The TLS policy allowed 1.2 as well as 1.3; say "1.3 preferred" in diagrams, not "1.3 only".
- Check with `curl -sv http://host/` (expect 301) and `curl -sv https://host/` (TLS 1.3, HTTP/2 200).

SmartCity: browsers need HTTPS for camera or microphone and for service workers, and MQTT over TLS needs a certificate too.

## Related
- [CloudFront needs its certificate in us-east-1 and routes by Host header, not by DNS target](cloudfront-cert-region-and-host-header-routing.md)
- [Use terraform apply -target for a one-off change, then do the full apply later](terraform-target-for-one-off-applies.md)
