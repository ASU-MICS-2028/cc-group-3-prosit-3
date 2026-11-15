---
title: Infrastructure as Code has edges: Amplify hosting could not be fully created by Terraform
tags: [iac, process, prosit-1]
source: Prosit 1 docs/learnings.md L-001
---

Prosit 1 tried AWS Amplify Hosting through Terraform and hit three failures in turn: Amplify is not offered in `af-south-1`; a classic token made Amplify create a GitHub deploy key, which the organisation blocks; and installing the Amplify GitHub App then failed because the public CreateApp API only accepts a token (the console uses a private API).

Workaround: create the app once in the console (using the GitHub App), then `terraform import` it, after which Terraform can manage its attributes. The click path was written into the ADR so a rebuild is a known, finite sequence.

Takeaways: a vendor can claim Terraform support and still gate steps behind the console; document any irreducible manual step; prove reproducibility by recreating from scratch. Prosit 2 avoided the issue by using S3 + CloudFront instead.

## Related
- [Check that a service and instance type exist in af-south-1 before designing around it](check-service-availability-in-af-south-1.md)
- [CloudFront needs its certificate in us-east-1 and routes by Host header, not by DNS target](cloudfront-cert-region-and-host-header-routing.md)
