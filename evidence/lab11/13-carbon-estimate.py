"""Lab 11 Part D: monthly operational carbon of the SmartCity stack per region (#13).

Method: Cloud Carbon Footprint (CCF), https://www.cloudcarbonfootprint.org/docs/methodology/
  energy = (vCPU-h x (min W + util x (max W - min W)) + GB-h x 0.392 W) x PUE
  CO2e   = energy x grid factor (location-based)
Run: python3 evidence/lab11/13-carbon-estimate.py
"""
HOURS = 730  # one month

# Stack sizing: an assumption until #12 (budget model) fixes the real sizes. Edit and rerun.
# (component, instances, vCPU each, GB RAM each, hours a month each)
STACK = [
    ("MQTT broker + bridge", 1, 2, 2, HOURS),
    ("API (auto-scaling min 2)", 2, 2, 2, HOURS),
    ("Time-series DB", 1, 2, 8, HOURS),
    ("ML training (2 h a day)", 1, 2, 8, 60),
]
UTIL = 0.5  # CCF's default when real utilisation is unknown
MEM_W_PER_GB = 0.392

# CCF coefficients (methodology page, read 15 Nov 2026)
PROVIDER = {"aws": {"min_w": 0.74, "max_w": 3.5, "pue": 1.135},
            "gcp": {"min_w": 0.71, "max_w": 4.26, "pue": 1.1}}

# Grid factors in gCO2e/kWh. AWS: CCF table (af-south-1: Carbon Data Intelligence; us-east-1: EPA eGRID).
# GCP: Google region-carbon-info data/yearly/2025.csv (Electricity Maps), with Google CFE.
REGIONS = [
    # (provider, region, place, gCO2e/kWh, Google CFE or None)
    ("aws", "af-south-1", "Cape Town", 757.44, None),
    ("aws", "us-east-1", "N. Virginia", 365.13, None),
    ("gcp", "africa-south1", "Johannesburg", 641.42, 0.15),
    ("gcp", "europe-west1", "Belgium", 126.43, 0.79),
    ("gcp", "europe-west9", "Paris", 15.83, 0.96),
]


def kwh(provider):
    p = PROVIDER[provider]
    vcpu_h = sum(n * cpu * h for _, n, cpu, _, h in STACK)
    gb_h = sum(n * gb * h for _, n, _, gb, h in STACK)
    watts = p["min_w"] + UTIL * (p["max_w"] - p["min_w"])
    return (vcpu_h * watts + gb_h * MEM_W_PER_GB) / 1000 * p["pue"], vcpu_h, gb_h


def main():
    _, vcpu_h, gb_h = kwh("aws")
    print(f"Stack: {vcpu_h} vCPU-hours and {gb_h} GB-hours a month, {UTIL:.0%} CPU utilisation\n")
    print(f"{'region':16} {'place':13} {'kWh/month':>9} {'g/kWh':>7} {'kg CO2e/month':>13} {'CFE':>5}")
    rows = []
    for prov, region, place, g, cfe in REGIONS:
        e, _, _ = kwh(prov)
        kg = e * g / 1000
        rows.append((region, kg))
        print(f"{region:16} {place:13} {e:9.1f} {g:7.1f} {kg:13.2f} {'' if cfe is None else f'{cfe:.0%}':>5}")
    base = dict(rows)["af-south-1"]
    print(f"\naf-south-1 vs us-east-1: {base / dict(rows)['us-east-1']:.1f}x the CO2e")
    print(f"af-south-1 over a 4-week prosit: {base * 28 / 30:.1f} kg CO2e")
    return rows


if __name__ == "__main__":
    rows = dict(main())
    # self-check: dirtiest grid gives the most CO2e, cleanest the least
    assert max(rows, key=rows.get) == "af-south-1" and min(rows, key=rows.get) == "europe-west9"
