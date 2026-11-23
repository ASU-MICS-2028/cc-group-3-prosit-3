-- Dev-only tables for running the bridge locally, shaped by contracts/storage.md.
-- The real schema (rollups, retention, indexes) is Elise's, issue #22; replace this when it lands.
CREATE EXTENSION IF NOT EXISTS timescaledb;

CREATE TABLE IF NOT EXISTS air_quality (
  ts timestamptz NOT NULL, device_id text NOT NULL, neighbourhood text NOT NULL, source text NOT NULL,
  seq integer NOT NULL, pm25 double precision NOT NULL, battery_pct double precision,
  UNIQUE (device_id, ts));
CREATE TABLE IF NOT EXISTS waste (
  ts timestamptz NOT NULL, device_id text NOT NULL, neighbourhood text NOT NULL, source text NOT NULL,
  seq integer NOT NULL, fill_pct double precision NOT NULL, battery_pct double precision,
  UNIQUE (device_id, ts));
CREATE TABLE IF NOT EXISTS flood (
  ts timestamptz NOT NULL, device_id text NOT NULL, neighbourhood text NOT NULL, source text NOT NULL,
  seq integer NOT NULL, water_level_cm double precision NOT NULL, battery_pct double precision,
  UNIQUE (device_id, ts));

SELECT create_hypertable(t, 'ts', if_not_exists => TRUE) FROM unnest(ARRAY['air_quality', 'waste', 'flood']) AS t;
