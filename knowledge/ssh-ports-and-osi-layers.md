---
title: SSH gives secure remote access; ports sit at the transport layer
tags: [networking, security, lecture]
source: Lecture 4
---

SSH is used to log in securely to a server you are not physically at, over an untrusted network. You specify the port number. OSI recap from the lecture: physical (bits on wire), data link (MAC addresses), network (IP addresses), transport (ports), up to application. Docker CLI commands can run against a remote daemon over SSH.

## Related
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
- [Do not put frontend, backend and database on the same host](separate-tiers-across-hosts-and-networks.md)
