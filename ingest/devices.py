"""Per-device MQTT credentials and revocation (#21, Lab 12 Part E).

  python3 ingest/devices.py init           # a new password for every simulator device and the bridge
  python3 ingest/devices.py revoke <id>    # remove one device and reload the broker; the rest carry on

Files written (all gitignored, never commit them):
  ingest/mosquitto/passwd          hashed passwords, read by Mosquitto
  ingest/mosquitto/acl             each device may write only its own topic; the bridge may only read
  ingest/device_credentials.csv    plain passwords for the simulator and bridge (local dev only;
                                   on AWS they belong in Secrets Manager)
Hashing is done by Mosquitto's own mosquitto_passwd tool, run in the broker image.
"""
import csv
import secrets
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sensors"))
from simulator import FLEET  # noqa: E402  one list of devices for the simulator and the broker

CONF = ROOT / "ingest" / "mosquitto"
PASSWD, ACL = CONF / "passwd", CONF / "acl"
CREDS = ROOT / "ingest" / "device_credentials.csv"
IMAGE = "eclipse-mosquitto:2.0.20"
COMPOSE = ["docker", "compose", "-f", str(ROOT / "ingest" / "compose.yaml")]
BRIDGE = "bridge"


def acl_text(users):
    """Mosquitto ACL for the given usernames. Anyone not listed gets nothing (the ACL file denies by default)."""
    own = {d: f"accra/{n}/{dom}/{d}" for d, n, dom, _ in FLEET}
    lines = [f"user {BRIDGE}", "topic read accra/#", ""] if BRIDGE in users else []
    for u in users:
        if u in own:
            lines += [f"user {u}", f"topic write {own[u]}", ""]
    return "\n".join(lines)


def read_creds():
    with CREDS.open() as f:
        return {row["username"]: row["password"] for row in csv.DictReader(f)}


def write_files(creds):
    with CREDS.open("w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")  # plain \n so shell tools read it cleanly
        w.writerow(["username", "password"])
        w.writerows(creds.items())
    ACL.write_text(acl_text(creds))
    private()


def private():
    """Owner-only, as Mosquitto asks. On a Linux host also `chown 1883` passwd and acl (the broker's uid)."""
    for f in (CREDS, PASSWD, ACL):
        if f.exists():
            f.chmod(0o600)


def mosquitto_passwd(*args):
    subprocess.run(["docker", "run", "--rm", "-v", f"{CONF}:/m", IMAGE, "mosquitto_passwd", *args], check=True)


def init():
    creds = {u: secrets.token_urlsafe(24) for u in [BRIDGE, *(d for d, *_ in FLEET)]}
    write_files(creds)
    PASSWD.write_text("".join(f"{u}:{p}\n" for u, p in creds.items()))
    private()
    mosquitto_passwd("-U", "/m/passwd")  # hashes the plain file in place
    print(f"{len(creds)} credentials written; start or reload the broker to use them")


def revoke(device_id):
    creds = read_creds()
    if device_id not in creds or device_id == BRIDGE:
        sys.exit(f"no device {device_id}")
    del creds[device_id]
    write_files(creds)
    mosquitto_passwd("-D", "/m/passwd", device_id)
    # SIGHUP makes Mosquitto re-read passwd and acl without dropping the other clients.
    subprocess.run([*COMPOSE, "kill", "-s", "SIGHUP", "mosquitto"], check=True)
    print(f"revoked {device_id}")


if __name__ == "__main__":
    match sys.argv[1:]:
        case ["init"]:
            init()
        case ["revoke", device_id]:
            revoke(device_id)
        case _:
            sys.exit(__doc__)
