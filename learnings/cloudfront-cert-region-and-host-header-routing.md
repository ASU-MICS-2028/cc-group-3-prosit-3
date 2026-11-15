---
title: CloudFront needs its certificate in us-east-1 and routes by Host header, not by DNS target
tags: [networking, security, prosit-1, prosit-2]
source: Prosit 1 docs/learnings.md L-002; Prosit 2 docs/decisions.md D-033; Prosit 2 knowledge/sessions/2026-11-05-pwa-hosting.md
---

Two separate facts:

1. **Certificate region.** CloudFront only reads ACM certificates from `us-east-1`. Prosit 2 added a second AWS provider alias in Terraform for that one resource. An ALB certificate must be in the ALB's own region.
2. **Host-header routing.** Visiting the raw `dxxxx.cloudfront.net` name returned 404 while the custom CNAME returned 200. CloudFront picks the distribution by the HTTP Host header against its alternate-domain list, so the raw name is not browsable. Test with `curl -I https://custom-name/` or `--resolve`, not the CloudFront hostname.

Prosit 2 also saw a missing file return 403 (not 404) from the private S3 origin, because CloudFront may read but not list the bucket. A CloudFront Function rewrites extension-less app routes to `index.html`, and anything with a dot in the name is treated as a real file.

SmartCity: a static dashboard can use the same S3 + CloudFront + us-east-1 certificate pattern at about zero cost.

## Related
- [HTTPS on the ALB with an ACM certificate when DNS lives outside Terraform](https-acm-certificate-with-external-dns.md)
- [Static PWA hosting: cache headers and how a new release reaches phones](pwa-cache-headers-and-service-worker-updates.md)
