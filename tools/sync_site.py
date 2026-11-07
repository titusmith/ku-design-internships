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
try:
    old = open(out, encoding="utf-8").read()
except FileNotFoundError:
    old = None
if old == page:
    print("unchanged: %d published listings" % len(d["listings"]))
else:
    open(out, "w", encoding="utf-8").write(page)
    print("updated: %d published listings (%d queue items left out)" % (len(d["listings"]), before - len(d["listings"])))
