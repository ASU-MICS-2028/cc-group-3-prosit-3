---
title: Lab 3 - containerize a microservice, push to a registry, run it on Kubernetes
tags: [lab, prosit-1, containers]
source: Lab 3 handout (week03_lab-Students)
---

Week 3, 3 h, team. Prosit 1 microservices.

**Objectives:** Docker on laptop and VM; a small HTTP API with /health and CRUD endpoints (Node/Express starter, other languages allowed); a production-style Dockerfile (layer caching, non-root user); push to Docker Hub and pull on a second machine; deploy to Minikube or Kind, scale to 3 replicas, delete a Pod and watch it come back.

**Parts:** A build and test the container (image should be under 300 MB for a simple API). B registry push/pull. C local Kubernetes (create deployment, expose NodePort, scale, delete pod).

**Deliverables:** build/curl output plus Dockerfile and server.js; registry link plus pull-on-second-machine proof; kubectl get pods with 3 replicas and a note on self-healing; 300-word report (before Week 4).

**Rubric:** working Dockerfile 30%; image in registry 15%; K8s 3 replicas plus self-healing 30%; report on microservice boundaries and data consistency 25%.

Homework extension: second service, service DNS name, multi-stage build.

## Related
- [Dockerfile pattern - copy manifests first, install, then copy code, run as non-root](dockerfile-layer-cache-and-non-root-user.md)
- [Prove Kubernetes self-healing by deleting a Pod on purpose](kubernetes-self-healing-delete-pod-demo.md)
- [Services find each other by Kubernetes DNS name, not IP](kubernetes-service-dns-name-between-services.md)
- [Inside a container, localhost is the container itself](localhost-inside-a-container-is-the-container.md)
