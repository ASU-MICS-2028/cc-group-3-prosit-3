-- Tables the API owns (contracts/storage.md "Other tables"). Applied by app.py at start-up; safe to re-run.
CREATE TABLE IF NOT EXISTS alerts (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  kind text NOT NULL CHECK (kind IN ('flood_warning', 'anomaly', 'bin_due')),
  domain text NOT NULL CHECK (domain IN ('air_quality', 'waste', 'flood')),
  neighbourhood text NOT NULL, device_id text,
  opened_at timestamptz NOT NULL DEFAULT now(),
  status text NOT NULL DEFAULT 'open' CHECK (status IN ('open', 'closed')),
  reason text NOT NULL);

-- No names or phone numbers (contracts/storage.md).
CREATE TABLE IF NOT EXISTS citizen_reports (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  received_at timestamptz NOT NULL DEFAULT now(),
  category text NOT NULL, description text NOT NULL,
  lat double precision NOT NULL, lon double precision NOT NULL, photo_url text);

-- One row per forecast point served, so the drift log (#32) can join it to the actual reading later.
CREATE TABLE IF NOT EXISTS predictions (
  served_at timestamptz NOT NULL DEFAULT now(),
  station text NOT NULL, model_version text NOT NULL,
  target_ts timestamptz NOT NULL, pm25 double precision NOT NULL);
CREATE INDEX IF NOT EXISTS predictions_station_target ON predictions (station, target_ts);
