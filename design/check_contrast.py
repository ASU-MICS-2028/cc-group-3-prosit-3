"""WCAG contrast check for design/tokens.css. Exit 1 if any pair is below its minimum.
Usage: python3 design/check_contrast.py"""
import re, sys, pathlib

css = pathlib.Path(__file__).with_name("tokens.css").read_text()

def themes():
    light = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6}|[0-9.]+(?=;))", css.split("/* dark theme */")[0]))
    m = re.search(r'\[data-theme="dark"\]\s*\{([^}]*)\}', css)
    dark = {**light, **dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6}|[0-9.]+(?=;))", m.group(1)))}
    return {"light": light, "dark": dark}

def lum(h):
    c = [int(h[i:i+2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

# (foreground, background, minimum): 4.5 for text, 3.0 for borders, focus ring and big text
PAIRS = [
    ("ink", "bg", 4.5), ("gauge", "bg", 3.0), ("gauge", "surface", 3.0), ("on-handle", "handle", 3.0), ("on-tile-on", "tile-on", 4.5), ("tile-accent", "tile-on", 3.0), ("on-tile-accent", "tile-accent", 3.0), ("ink", "surface", 4.5), ("ink", "surface-2", 4.5),
    ("ink-muted", "bg", 4.5), ("ink-muted", "surface", 4.5), ("ink-muted", "surface-2", 4.5),
    ("on-primary", "primary", 4.5), ("on-accent", "accent", 4.5), ("on-nav", "nav", 4.5), ("accent", "nav", 3.0),
    ("ok", "ok-bg", 4.5), ("warn", "warn-bg", 4.5), ("danger", "danger-bg", 4.5),
    ("ok", "surface", 4.5), ("warn", "surface", 4.5), ("danger", "surface", 4.5),
    ("border", "bg", 3.0), ("border", "surface", 3.0),
    ("focus", "bg", 3.0), ("focus", "surface", 3.0),
]
def over(fg, a, bg):
    """Colour of fg at opacity a drawn over bg."""
    f = [int(fg[i:i+2], 16) for i in (1, 3, 5)]
    b = [int(bg[i:i+2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x * a + y * (1 - a)):02x}" for x, y in zip(f, b))

bad = 0
for name, t in themes().items():
    # text on a glass card, over each end of the backdrop gradient (blur only averages these)
    for end in ("backdrop-a", "backdrop-b"):
        g = over(t["glass"], float(t["glass-alpha"]), t[end])
        for fg in ("ink", "ink-muted", "ok", "warn", "danger"):
            r = ratio(t[fg], g)
            ok = r >= 4.5
            bad += not ok
            print(f"{'PASS' if ok else 'FAIL'} {name:14} {fg:10} on glass/{end[-1]:9} {r:5.2f} (need 4.5)")
    for fg, bg, need in PAIRS:
        r = ratio(t[fg], t[bg])
        ok = r >= need
        bad += not ok
        print(f"{'PASS' if ok else 'FAIL'} {name:14} {fg:10} on {bg:9} {r:5.2f} (need {need})")
print(f"\n{bad} failing pair(s)")
sys.exit(1 if bad else 0)
