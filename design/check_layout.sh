#!/usr/bin/env bash
# Renders a page in a real 320 px wide frame, at 100% and 200% text size, and reports sideways overflow.
# Usage: design/check_layout.sh design/design-system.html
# Prints numbers only (no screenshots, to keep the repo small). Open the page in a browser to look at it.
# Needs Google Chrome. Headless Chrome won't make a window under ~500 px, so the page is put in a 320 px iframe.
set -euo pipefail
PAGE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
TMP="$(mktemp -d)"
for ZOOM in 100 200; do
cat > "$TMP/w$ZOOM.html" <<HTML
<!doctype html><meta charset=utf-8><body style="margin:0;background:#888">
<iframe id=f src="file://$PAGE" style="width:320px;height:3600px;border:0;display:block" onload="
 var d=this.contentDocument; d.documentElement.style.fontSize='${ZOOM}%';
 setTimeout(function(){var e=d.documentElement; document.title='overflow='+(e.scrollWidth-e.clientWidth)+'px width='+e.clientWidth+' height='+e.scrollHeight; this.style.height=e.scrollHeight+'px'; }.bind(this),300)"></iframe>
HTML
echo -n "text ${ZOOM}%: "; "$CHROME" --headless=new --disable-gpu --allow-file-access-from-files --virtual-time-budget=3000 --dump-dom "file://$TMP/w$ZOOM.html" 2>/dev/null | grep -o '<title>[^<]*' | sed 's/<title>//' || echo "no result"
done
