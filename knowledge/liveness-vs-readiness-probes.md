---
title: Liveness probes ask "is it stuck?" and readiness probes ask "can it take traffic?"
tags: [containers, reliability, lecture]
source: Lecture 4
---

Health checks in Kubernetes come in two kinds. A liveness probe checks whether the app is alive or stuck; if not, it needs a restart. A readiness probe checks whether the app is ready to receive traffic; an app can be alive but still starting slowly. Both are usually backed by a /health endpoint, as in the lab.

For SmartCity Accra: add a /health endpoint to each service so the load balancer and orchestrator only send traffic to ready instances.

## Related
- [Immutable infrastructure: replace the image, never patch a running container](immutable-infrastructure.md)
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
