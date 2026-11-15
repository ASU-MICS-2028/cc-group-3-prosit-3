---
title: Dockerfile pattern - copy manifests first, install, then copy code, run as non-root
tags: [containers, lab]
source: Lab 3 Part A
---

Starter Dockerfile: FROM node:20-alpine, WORKDIR /app, COPY package*.json, RUN npm ci --omit=dev, COPY . ., EXPOSE 3000, USER node, CMD. Copying dependency manifests before the rest of the code lets Docker reuse the cached install layer when only source changes.

Use a small base image (target under 300 MB for a simple API) and a non-root user. Multi-stage builds are the next step to shrink further.

Gotchas: build fails on install if manifests were not copied before RUN install; Apple Silicon may need --platform=linux/amd64.

SmartCity Accra: same pattern for ingest, ML and API containers.

## Related
- [Inside a container, localhost is the container itself](localhost-inside-a-container-is-the-container.md)
- [Prove Kubernetes self-healing by deleting a Pod on purpose](kubernetes-self-healing-delete-pod-demo.md)
- [Clone and build a partner's repo to catch files that were never committed](partner-clone-build-catches-uncommitted-files.md)
