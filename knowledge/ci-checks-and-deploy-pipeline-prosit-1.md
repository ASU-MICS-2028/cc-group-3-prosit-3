---
title: Pull-request checks then image build then rolling refresh
tags: [ci-cd, containers, lecture]
source: Lecture 7
---

The Prosit 1 pipeline shown in class is a good template:
- On a pull request: pre-commit checks, front-end tests, back-end tests, and Terraform format plus validate. A teammate reviews before merge.
- After merge to main: build the container image, push it to ECR, then trigger a rolling refresh of the instances so the new image goes live.
- Front end: AWS Amplify builds and publishes it (served via CloudFront). One reason given for Amplify over S3 plus CloudFront was automatic preview branches for every push, which would cost extra effort to rebuild by hand.
- Secrets live in a secrets manager, never in the repo; third-party connections used OIDC credentials rather than long-lived keys.

For SmartCity Accra: the same shape works for the ingestion service, the ML service and the dashboard.

## Related
- [Terraform workflow - init, plan, apply; import or destroy pre-existing resources](terraform-init-plan-apply-and-import.md)
- [Keep servers and databases in private subnets behind the load balancer](private-subnets-behind-load-balancer.md)
