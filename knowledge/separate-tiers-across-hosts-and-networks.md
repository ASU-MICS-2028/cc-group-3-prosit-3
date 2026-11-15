---
title: Do not put frontend, backend and database on the same host
tags: [security, networking, lecture]
source: Lecture 4; Lecture 6
---

Design the network so front end, back end and database are in separate places with controlled access (separate LANs or subnets, who can reach what). The lecturer's analogy: do not keep all valuables in one place, so one breach does not give everything.

For SmartCity Accra: put the time-series DB in a private subnet, reachable only from the services that need it.

**Also (Lecture 6):** A grade-tampering incident discussed in class was traced partly to the database and backend sharing one IP address, so compromising the backend gave direct access to the data. Insider help from the registry made it worse.

Lesson: in cloud network planning, put the database on a separate host in a private network, reachable only from the backend. Analogy used: the president and vice president do not travel in the same plane.

For SmartCity Accra: place the time-series DB and broker in private subnets with security groups allowing only the services that need them; only the load balancer or API faces the public.

## Related
- [SSH gives secure remote access; ports sit at the transport layer](ssh-ports-and-osi-layers.md)
- [Data centers protect data with physical and software security layers](data-center-layered-security.md)
- [Users and insiders are usually the weakest security link](users-are-weakest-security-link.md)
- [Prefer SSH keys with a passphrase over password logins to servers](ssh-keys-over-passwords.md)
