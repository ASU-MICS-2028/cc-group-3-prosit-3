---
title: Docker core concepts: image, container, Dockerfile, registry
tags: [containers, lecture]
source: Lecture 4
---

- Image: a read-only template built from a Dockerfile.
- Container: a running instance of an image, like a process is a running instance of a program stored on disk.
- Dockerfile: the instructions used to build an image layer by layer.
- Registry: where images are stored and pulled from.

Docker architecture: the Docker CLI is the client; the daemon is the background process that builds images, runs containers and manages networking. The client just points at a daemon, so it can talk to a remote one (for example over SSH).

## Related
- [Immutable infrastructure: replace the image, never patch a running container](immutable-infrastructure.md)
- [Containers are lighter than VMs because they share the host kernel instead of bundling an OS](containers-vs-virtual-machines.md)
- [SSH gives secure remote access; ports sit at the transport layer](ssh-ports-and-osi-layers.md)
