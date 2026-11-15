---
title: Clone and build a partner's repo to catch files that were never committed
tags: [containers, process, prosit-1]
source: Lab 0 Part D.3 and Troubleshooting
---

Containers promise the same image on any machine, but only if everything the build needs is in Git. Having a teammate clone the repo fresh and run docker build with no changes exposes: files left untracked, or files wrongly excluded by .dockerignore/.gitignore (for example a too-broad pattern that drops index.html).

Your own machine hides this bug because the file still exists locally. When a partner's build fails, check git status for untracked files and the .dockerignore.

SmartCity Accra: do a clean-clone build before each demo or hand-in.

## Related
- [Dockerfile pattern - copy manifests first, install, then copy code, run as non-root](dockerfile-layer-cache-and-non-root-user.md)
- [Lab 0 - cloud accounts, Linux CLI, Git/GitHub and Docker foundations](lab-0-foundations-accounts-linux-git-docker.md)
- [Tests pass locally but fail in CI - look for environment differences](ci-tests-pass-locally-fail-in-ci.md)
