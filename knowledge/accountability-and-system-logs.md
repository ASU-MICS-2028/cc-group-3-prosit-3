---
title: Accountability means every action can be traced to a user, through system logs
tags: [security, monitoring, lecture]
source: Lecture 3
---

Accountability is the goal that any action performed on a system can be traced back to the user (or process) that did it, so nobody can deny it. It is implemented through logs: who did what, which application they accessed, when.

Example from the lecture: an online quiz platform logs actions such as switching tabs, so a later claim can be checked against the log. If an organization's accounts are compromised, logs let you find where it started and who made the mistake, instead of punishing everyone.

Logs also support non-repudiation. Operating systems and underlying platforms usually provide this; when building applications, make sure important actions are logged.

For SmartCity Accra: log who changed thresholds, alert rules or sensor configuration.

## Related
- [Logging for accountability trades off against privacy, and policy sets the balance](accountability-logging-vs-privacy.md)
- [Authenticity means the sender and data are genuine, which gives non-repudiation](authenticity-and-non-repudiation.md)
