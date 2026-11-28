# One image for every Python process in SmartCity Accra (#73). The command picks which one runs:
#   API (default):     python api/app.py           port 8000, needs DATABASE_URL
#   Bridge:            python ingest/bridge.py     needs DATABASE_URL, MQTT_HOST, MQTT_USERNAME, MQTT_PASSWORD; spool in /data
#   Alert checker:     python api/alerts.py        needs DATABASE_URL
#   Simulator:         python sensors/simulator.py --host <broker> --creds /run/creds.csv
# Build from the repo root:  docker build -t smartcity .
FROM python:3.12.8-slim-bookworm

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 SPOOL=/data/spool.jsonl
WORKDIR /app

COPY contracts/requirements.txt contracts/
COPY ingest/requirements.txt ingest/
COPY api/requirements.txt api/
COPY sensors/requirements.txt sensors/
RUN pip install --no-cache-dir -r contracts/requirements.txt -r ingest/requirements.txt \
      -r api/requirements.txt -r sensors/requirements.txt

# Only the runtime files; .dockerignore keeps credentials, .env and the spool out of the build context too.
COPY contracts/sensor-reading.schema.json contracts/api.openapi.yaml contracts/
COPY ingest/bridge.py ingest/
COPY api/app.py api/alerts.py api/schema.sql api/
COPY sensors/simulator.py sensors/openaq.py sensors/

# Non-root; /data holds the bridge's spool, so mount a volume there to keep readings through a restart.
RUN useradd --uid 10001 --no-create-home app && mkdir /data && chown app /data
USER app
VOLUME /data
EXPOSE 8000
CMD ["python", "api/app.py"]
