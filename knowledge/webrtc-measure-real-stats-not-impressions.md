---
title: Measure connection quality with real stats
tags: [monitoring, networking]
source: Lab 7 Part C.3
---

Use chrome://webrtc-internals or log pc.getStats() every 5 s: packetsLost, jitter and framesDecoded from inbound-rtp video; currentRoundTripTime from the candidate pair. Compare the normal and Slow-3G runs by numbers.

General rule: do not trust "it looked fine".

## Related
- [WebRTC - test across two networks because direct peer links often fail](webrtc-stun-turn-cross-network-testing.md)
- [Generate controlled CPU load with stress-ng to see monitoring work](stress-ng-generate-cpu-load-for-monitoring.md)
