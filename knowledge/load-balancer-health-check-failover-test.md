---
title: Test load-balancer failover by stopping an instance
tags: [scaling, reliability, networking]
source: Lab 5 Part B and Troubleshooting
---

Put two instances in the private app subnet, an ALB in the public subnet, health check on /health. Send 10 curl requests, stop one instance, repeat: all should succeed and the target shows unhealthy.

If all targets are unhealthy: the instance security group must allow inbound from the load balancer's security group on the health-check port.

SmartCity Accra: the same health endpoint pattern feeds auto-scaling and load-balancer decisions.

## Related
- [VPC layout - two public and two private subnets across two AZs](vpc-two-az-public-private-subnet-layout.md)
- [Prove Kubernetes self-healing by deleting a Pod on purpose](kubernetes-self-healing-delete-pod-demo.md)
