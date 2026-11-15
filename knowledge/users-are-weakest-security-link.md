---
title: Users and insiders are usually the weakest security link
tags: [lecture, security]
source: Lecture 6
---

Even well-built systems fall to social engineering and insider leaks. In the incident discussed, an insider passed access to outsiders who emailed students offering to change grades for a fee. It was found because friends talked and admins noticed grade changes in logs; confessing students helped the investigation.

Takeaways: least-privilege access, train people, keep paper or independent records for critical data, and remember that the lecturer's view is that no system is perfectly secure.

For SmartCity Accra: limit who can see raw location-tagged data and credentials, and review IAM permissions.

## Related
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
- [Prefer SSH keys with a passphrase over password logins to servers](ssh-keys-over-passwords.md)
- [Attackers with a shell can hide their tracks, so protect and ship logs](audit-logs-can-be-tampered.md)
