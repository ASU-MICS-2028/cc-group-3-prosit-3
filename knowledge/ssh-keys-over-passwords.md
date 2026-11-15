---
title: Prefer SSH keys with a passphrase over password logins to servers
tags: [lecture, security]
source: Lecture 6
---

Advice given for server access: do not design systems around shared passwords, which leak or get taken over. Use SSH key authentication protected by a passphrase for the resources we use.

For SmartCity Accra: EC2 access via key pairs or SSM, no password SSH, and never commit keys to the public repo.

## Related
- [Users and insiders are usually the weakest security link](users-are-weakest-security-link.md)
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
