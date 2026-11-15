---
title: Publish one event, let independent functions react
tags: [event-driven, serverless, lab]
source: Lab 7 Parts A-B and Troubleshooting
---

The API inserts the appointment and publishes appointment.created to a queue/topic (SQS, Service Bus, Pub/Sub) instead of calling anything directly. A reminder function and a specialist-notify function each consume it without knowing about each other. If SMS is down, creation still succeeds.

Most common misconfiguration: the trigger (event source mapping) is not attached to the queue, so the function never fires. Check function logs to confirm. A logged reminder is acceptable without SMS credentials.

SmartCity Accra: sensor reading events fan out to storage, alerting and ML.

## Related
- [Add a dead-letter queue and make consumers idempotent](dead-letter-queue-and-idempotent-consumers.md)
- [Lab 7 - event-driven serverless reminders and a WebRTC video call](lab-7-event-driven-serverless-and-webrtc.md)
