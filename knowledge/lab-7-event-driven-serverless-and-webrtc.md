---
title: Lab 7 - event-driven serverless reminders and a WebRTC video call
tags: [lab, prosit-2, event-driven]
source: Lab 7 handout (week07_lab_students); Prosit 2 knowledge/labs.md
---

Week 7, 3 h, team. Prosit 2 telemedicine feature.

**Objectives:** a function triggered by a queue/topic event, not a direct call; an event bus between appointment creation and reactive functions; a second independent consumer of the same event; a two-party WebRTC call using STUN; test across two real networks; reason about what belongs on serverless.

**Parts:** A queue (SQS / Service Bus / Pub/Sub), API publishes appointment.created, a Lambda-style reminder function consumes it. B second consumer (specialist notify) on the same event. C WebRTC: WebSocket signaling server, browser client with STUN, same-network test, cross-network test, Slow-3G throttle, getStats() numbers.

**Deliverables:** logs of created, published, triggered; evidence both functions fired; screenshots of same/cross-network calls and stats; 300-word report (before Week 8).

**Rubric:** event flow with 2 independent consumers 35%; WebRTC established and tested under throttling 35%; report on serverless fit and network reality 30%.

Extension: dead-letter queue, idempotency check, TURN cost research for 50 calls/day x 15 min.

**Also (Prosit 2 knowledge/labs.md):** Parts: A an `appointment-events` queue or topic; `POST /appointments` saves and publishes `appointment.created` (no direct call); a function consumes it and sends or logs a reminder; evidence of the whole flow. B a second independent function (specialist notify) reacting to the same event. C a WebRTC call using a signaling server and public STUN: same network, then two networks, throttle one side to Slow 3G, read packet loss, jitter and round trip from `getStats()` or `chrome://webrtc-internals`.

Report: 300 words (what moved to serverless and one thing deliberately not, cross-network result and TURN implication, one resilience question). Rubric: event flow with two consumers 35, WebRTC under throttling 35, reasoning 30. Homework: DLQ demo, idempotency (publish twice, send once), TURN cost for 50 calls/day x 15 min.

Facts: two functions on one SQS queue compete, so fan out with SNS to two queues; browsers allow the camera only on HTTPS or localhost; if cross-network fails, that is the finding.

## Related
- [Publish one event, let independent functions react](publish-one-event-two-independent-consumers.md)
- [Add a dead-letter queue and make consumers idempotent](dead-letter-queue-and-idempotent-consumers.md)
- [WebRTC - test across two networks because direct peer links often fail](webrtc-stun-turn-cross-network-testing.md)
- [Measure connection quality with real stats](webrtc-measure-real-stats-not-impressions.md)
- [Lab 8 - structured peer design review and midterm preparation](lab-8-peer-review-and-midterm-prep.md)
- [HealthConnect event flow: appointment.created fans out to two independent Lambdas](healthconnect-event-flow-sns-sqs-lambda.md)
