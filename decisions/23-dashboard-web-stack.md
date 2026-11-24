---
issue: 23
title: Use React, TypeScript, and Vite for the AMA dashboard
date: 2026-11-24
decided_by: Elise
status: accepted
---

## Context

The dashboard displays changing sensor readings from the team's API.

## Options

1. React with TypeScript and Vite provides reusable UI components and a browser build.
2. A full-stack web framework adds server features that the dashboard's first chart does not require.

## Decision

Use React with TypeScript and Vite for the dashboard.

## Consequences

The frontend can start with sample readings and connect to the shared API when it is available.
