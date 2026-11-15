---
title: Inside a container, localhost is the container itself
tags: [containers, networking, databases]
source: Lab 4 Troubleshooting
---

If a containerized service gets "connection refused" to its database, check DATABASE_URL: the host must be the database's real endpoint (or a service name), not localhost. Localhost inside a container is that container.

Same idea in Compose and Kubernetes: reach other containers by service name.

## Related
- [Services find each other by Kubernetes DNS name, not IP](kubernetes-service-dns-name-between-services.md)
- [Put the database in a private subnet with no public access](database-in-private-subnet-no-public-access.md)
