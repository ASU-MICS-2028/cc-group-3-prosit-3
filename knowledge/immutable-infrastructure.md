---
title: Immutable infrastructure: replace the image, never patch a running container
tags: [containers, ci-cd, lecture]
source: Lecture 4
---

Do not edit a live container to fix a bug. Fix the code, build a new image and redeploy, taking the old one offline. This is why CI/CD exists: merge in GitHub, a pipeline builds and deploys the new version. The lecturer compared this to web apps and AI tools that update for users without any install.

For SmartCity Accra: deploy changes by pushing a new image through the pipeline, not by SSHing into a server.

## Related
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
- [Liveness probes ask "is it stuck?" and readiness probes ask "can it take traffic?"](liveness-vs-readiness-probes.md)
