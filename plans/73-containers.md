# Plan: Package the bridge, API, alert checker and simulator as one container image

- **Issue:** #73
- **Owner:** Joseph (`josetseph`)
- **Milestone:** Lab 12
- **Status:** done

## Goal
#28 and #35 deploy "from their owner's package", and the bridge and API had none. Give Eugene a container image to deploy.

## What gets built
- `Dockerfile` at the repo root. One image (Python 3.12 slim, non-root); the command picks the API, bridge, alert checker or simulator.
- `.dockerignore` as an allow-list of the runtime files only, so credentials and `.env` can't enter the image.
- `ingest/compose.yaml`: a `--profile app` that adds the bridge, API and alert checker. The DB has a health check that the app services wait for.
- `ingest/README.md`: a "Containers" section with the AWS table (commands, env vars, ports, volume, secrets, health check).
- A fix found while testing: Mosquitto's default `max_queued_messages` (1000) dropped readings when the bridge fell behind. Raised to 100000, with a learnings note.

## Depends on
- nothing

## Done when
- One image runs the API, the bridge, the alert checker or the simulator, chosen by its command
- No secrets in the image; it runs as a non-root user
- `ingest/compose.yaml` runs the whole pipeline in containers locally, with evidence that readings reach the API
- A README section tells Eugene what to deploy

## Evidence to capture
- `evidence/lab12/73-container-run.sh`
  - `73-image-check.txt`: size, user, file list, a search for secrets
  - `73-pipeline-run.txt`: services, API calls, published vs stored

## Not doing
- Terraform or any AWS change (Eugene, #28 and #35).
- A `/health` endpoint. That is a contract change; the ALB can use `GET /alerts` for now.
- Broker persistence. That is noted for #28.
