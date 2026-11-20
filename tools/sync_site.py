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
if token and "cloudflareinsights" not in page:
    beacon = ('<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
              "data-cf-beacon='" + json.dumps({"token": token}) + "'></script>\n")
    i = page.rfind("</body>")
    page = page[:i] + beacon + page[i:] if i != -1 else page + beacon

# Click tracking (which postings students open), via GoatCounter. Public copy only.
# Set {"goatcounter_code": "yourcode"} in tools/site_config.json; empty = off.
try:
    gc = json.load(open(cfg_path, encoding="utf-8")).get("goatcounter_code", "").strip()
except (FileNotFoundError, ValueError):
    gc = ""
if re.fullmatch(r"[a-z0-9-]+", gc or "") and "goatcounter.com/count" not in page:
    clicks = (
        '<script data-goatcounter="https://' + gc + '.goatcounter.com/count" '
        "data-goatcounter-settings='{\"no_onload\": true}' async src=\"https://gc.zgo.at/count.js\"></script>\n"
        "<script>\n"
        "(function () {\n"
        "  var byLink = null;\n"
        "  function lookup() {\n"
        "    if (byLink) return byLink; byLink = {};\n"
        "    try { JSON.parse(document.getElementById('board-data').textContent).listings.forEach(function (l) {\n"
        "      if (l.link_url) byLink[l.link_url] = l; if (l.apply_email) byLink['mailto:' + l.apply_email] = l; }); } catch (e) {}\n"
        "    return byLink;\n"
        "  }\n"
        "  document.addEventListener('click', function (e) {\n"
        "    var a = e.target && e.target.closest ? e.target.closest('a[href]') : null; if (!a) return;\n"
        "    var href = a.getAttribute('href') || '';\n"
        "    if (!/^(https?:|mailto:)/i.test(href) || /goatcounter|cloudflareinsights/.test(href)) return;\n"
        "    var l = lookup()[href] || lookup()[href.split('?')[0]];\n"
        "    if (!l) return;\n"
        "    var kind = /^mailto:/i.test(href) ? 'email' : 'posting';\n"
        "    try { if (window.goatcounter && window.goatcounter.count) window.goatcounter.count({\n"
        "      path: kind + '/' + l.id, title: l.company + ': ' + l.role_title + (kind === 'email' ? ' (email)' : ''), event: true }); } catch (e) {}\n"
        "  }, true);\n"
        "})();\n"
        "</script>\n")
    i = page.rfind("</body>")
    page = page[:i] + clicks + page[i:] if i != -1 else page + clicks
try:
    old = open(out, encoding="utf-8").read()
except FileNotFoundError:
    old = None
if old == page:
    print("unchanged: %d published listings" % len(d["listings"]))
else:
    open(out, "w", encoding="utf-8").write(page)
    print("updated: %d published listings (%d queue items left out)" % (len(d["listings"]), before - len(d["listings"])))
