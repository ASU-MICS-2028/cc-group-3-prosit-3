---
title: Prove Kubernetes self-healing by deleting a Pod on purpose
tags: [containers, reliability, lab]
source: Lab 3 Part C
---

Commands: minikube start; kubectl create deployment NAME --image=...; kubectl expose deployment NAME --type=NodePort --port=3000; kubectl scale deployment NAME --replicas=3; kubectl get pods -w; kubectl delete pod POD.

The Deployment notices the missing replica and starts a new Pod without any recovery code from you. Low on memory? minikube start --memory=2200, or use Kind. After a reboot run minikube start again if kubectl cannot find the cluster.

SmartCity Accra: self-healing and replicas back the reliability story for ingestion and API pods.

## Related
- [Services find each other by Kubernetes DNS name, not IP](kubernetes-service-dns-name-between-services.md)
- [Dockerfile pattern - copy manifests first, install, then copy code, run as non-root](dockerfile-layer-cache-and-non-root-user.md)
- [Lab 3 - containerize a microservice, push to a registry, run it on Kubernetes](lab-3-containerizing-microservice-kubernetes.md)
