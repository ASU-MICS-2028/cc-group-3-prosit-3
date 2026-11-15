---
title: Containers fix the "works on my machine" dependency problem
tags: [containers, lecture]
source: Lecture 4
---

Code that runs on a developer's laptop often breaks elsewhere because of missing dependencies, OS differences or library version clashes (for example NumPy, Matplotlib and SymPy needing compatible versions). A container packages the application with its dependencies, so the same image runs the same way on another Docker host. If something breaks, the developer fixes it and ships a new image.

Limit noted in the lecture: a container shares the host's kernel and CPU architecture, so an image built for one CPU architecture (for example Intel versus Apple Silicon) is still tied to it.

For SmartCity Accra: package each service (ingestor, ML forecaster, API) as an image so it behaves the same on a laptop, in CI and on AWS.

## Related
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [Docker core concepts: image, container, Dockerfile, registry](docker-image-container-dockerfile-registry.md)
