---
title: If MFA codes are rejected, check the device clock
tags: [security, cloud-basics]
source: Lab 0 Troubleshooting
---

Authenticator apps generate codes from the current time, so a phone clock even a minute off makes every code fail. Set date and time to automatic/network time before assuming the setup is broken.

## Related
- [Every cloud account gets MFA and a $5 billing alert on day one](cloud-account-baseline-mfa-billing-alert.md)
- [Do daily work as a non-root IAM user, never the root account](never-use-root-account-for-daily-work.md)
