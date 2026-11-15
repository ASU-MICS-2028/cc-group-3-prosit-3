---
title: Allow SSH only from your own IP, never 0.0.0.0/0
tags: [networking, security, cloud-basics]
source: Lab 2 Part A and Troubleshooting
---

When launching a VM, open port 22 only to "My IP". Key file: chmod 400 on the .pem. Cannot connect? Your IP changes when you switch networks, so update the rule.

"Permission denied (publickey)" usually means the wrong username: ubuntu on Ubuntu AMIs, azureuser on Azure, ec2-user on Amazon Linux.

Also: docker --version "not found" or permission errors right after install need a new SSH session, since usermod -aG docker only applies to new logins.

SmartCity Accra: no sensor-facing or admin ports open to the world; use a bastion or SSM-style access.

## Related
- [Tag and name every cloud resource with the team name](tag-every-resource-with-team-name.md)
- [Do daily work as a non-root IAM user, never the root account](never-use-root-account-for-daily-work.md)
- [Lab 2 - first VM, basic monitoring and a six-pillar architecture diagram](lab-2-first-vm-and-architecture-diagram.md)
