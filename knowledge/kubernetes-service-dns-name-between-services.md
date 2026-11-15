---
title: Services find each other by Kubernetes DNS name, not IP
tags: [containers, networking]
source: Lab 3 Homework Extension
---

Create a Kubernetes Service for a second microservice and, from inside another Pod (kubectl exec -it POD -- sh), curl it at NAME.default.svc.cluster.local:PORT. Pod IPs change; the Service name stays stable.

SmartCity Accra: an ingest service should reach the broker or the DB through a stable name.

## Related
- [Prove Kubernetes self-healing by deleting a Pod on purpose](kubernetes-self-healing-delete-pod-demo.md)
- [Inside a container, localhost is the container itself](localhost-inside-a-container-is-the-container.md)
