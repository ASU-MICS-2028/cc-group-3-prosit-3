# Plan: MQTT bridge with local buffering (L12-C)

- **Issue:** #20
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** stub (owner fills in "What gets built" before starting)

## Goal
Carry readings from MQTT into storage, surviving outages (Lab 12 Part C, 35% + 20%).

## What gets built
- _to fill in_

## Depends on
- #2
- #7 decision

## Done when
- Bridge consumes MQTT and writes to the broker/time-series DB in batches
- Stopping the DB buffers readings locally; they flush on recovery with none lost (demonstrated)

## Evidence to capture
- _to fill in_

## Not doing
- _to fill in_
