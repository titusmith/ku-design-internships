#!/usr/bin/env python3
"""Make the public GitHub Pages copy from the board artifact's HTML.

Usage: python3 tools/sync_site.py <artifact.html> [index.html]

Copies the page as-is, except that listings waiting in (or dismissed from)
the Suggested queue are removed, so students' copy only has published posts.
"""
import json, re, sys

src = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "index.html"
s = open(src, encoding="utf-8").read()
m = re.search(r'(<script type="application/json" id="board-data">)(.*?)(</script>)', s, re.S)
if not m:
    sys.exit("board-data block not found; not syncing")
d = json.loads(m.group(2))
before = len(d.get("listings", []))
d["listings"] = [l for l in d.get("listings", []) if not l.get("status")]
body = json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
page = s[:m.start(2)] + body + s[m.end(2):]

# Visitor analytics for the public copy only (never added to the board on claude.ai).
# Set the token in tools/site_config.json -> {"cloudflare_token": "..."}; leave it empty to turn analytics off.
import os
cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site_config.json")
try:
    token = json.load(open(cfg_path, encoding="utf-8")).get("cloudflare_token", "").strip()
except (FileNotFoundError, ValueError):
    token = ""
if token:
    beacon = ('<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
              "data-cf-beacon='" + json.dumps({"token": token}) + "'></script>\n")
    i = page.rfind("</body>")
    page = page[:i] + beacon + page[i:] if i != -1 else page + beacon
try:
    old = open(out, encoding="utf-8").read()
except FileNotFoundError:
    old = None
if old == page:
    print("unchanged: %d published listings" % len(d["listings"]))
else:
    open(out, "w", encoding="utf-8").write(page)
    print("updated: %d published listings (%d queue items left out)" % (len(d["listings"]), before - len(d["listings"])))
