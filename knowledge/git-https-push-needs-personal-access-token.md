---
title: git push over HTTPS needs a token or SSH key, not your password
tags: [cloud-basics, ci-cd]
source: Lab 0 Troubleshooting
---

GitHub rejects account passwords for git push over HTTPS. Use a Personal Access Token (Settings, Developer settings) in place of the password, or switch to SSH key authentication.

Related Git habits from Lab 0: feature branch, push -u, pull request, merge, delete the branch. If conflict markers (<<<<<<<, =======, >>>>>>>) appear, edit the file to the right content, remove the markers, then git add and commit.

SmartCity Accra: tokens must never be committed; see secret scanning.

## Related
- [Scan for committed secrets in CI with gitleaks](secret-scanning-with-gitleaks-in-ci.md)
- [Lab 0 - cloud accounts, Linux CLI, Git/GitHub and Docker foundations](lab-0-foundations-accounts-linux-git-docker.md)
