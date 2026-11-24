---
issue: 12
title: Size the Makola pilot and keep API scaling in the city-wide projection
date: 2026-11-23
decided_by: Elise (review pending)
status: proposed
---

## Context

The [budget model](../evidence/lab11/12-budget-model.md) prices a 500-sensor Makola pilot and projects a 5,000-sensor Greater Accra scenario.

## Options

1. Carry the half-budget pilot cuts into the city-wide scenario. One API server lowers the bill and leaves the API without failover.
2. Keep the load balancer and API auto-scaling in the city-wide scenario. This adds cost and provides room for traffic peaks and API failover.

## Decision

Use the priced pilot as the baseline and model option 2 for city-wide traffic. Treat the city-wide user count and capacity allowances as planning assumptions.

## Consequences

Confirm capacity with workload tests and price the city-wide configuration before using the projection as a spending target.
