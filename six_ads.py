import re

# ── Ad snippets ──────────────────────────────────────────────────────────────

AD_728x90 = """\
<div class="flex justify-center w-full" style="min-height:90px;">
  <script data-cfasync="false">atOptions={'key':'24d82a14f251de0b584c1c1878965100','format':'iframe','height':90,'width':728,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
</div>"""

AD_300x250 = """\
<div class="flex justify-center w-full" style="min-height:250px;">
  <script data-cfasync="false">atOptions={'key':'cf6a125c26299b4a476c85e2b484cb3a','format':'iframe','height':250,'width':300,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
</div>"""

AD_160x600 = """\
<div class="hidden lg:flex justify-center" style="min-height:600px;">
  <script data-cfasync="false">atOptions={'key':'81f56b1bdcad21cd55ab223c4f4c2c92','format':'iframe','height':600,'width':160,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
</div>"""

AD_NATIVE = """\
<div class="flex justify-center w-full">
  <script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
  <div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>"""

# ── Read play.html ────────────────────────────────────────────────────────────
with open('play.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ── Step 1: Nuke ALL existing ad blocks (highperformanceformat + effectivegatecpm) ──
html = re.sub(
    r'<div[^>]*>\s*<script[^>]*>[\s\S]*?invoke\.js["\']>\s*</script>\s*</div>',
    '', html, flags=re.IGNORECASE)
html = re.sub(
    r'<div[^>]*>\s*<script[^>]*>atOptions[\s\S]*?invoke\.js["\']>\s*</script>\s*</div>',
    '', html, flags=re.IGNORECASE)
html = re.sub(
    r'<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*invoke\.js[^>]*></script>',
    '', html, flags=re.IGNORECASE)
html = re.sub(
    r'<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>',
    '', html, flags=re.IGNORECASE)

# ── Step 2: Remove both sidebar divs so we can rebuild them ──────────────────
# Remove left sidebar
html = re.sub(
    r'<!--\s*Left Sidebar.*?-->\s*<div class="hidden lg:flex[^"]*"[^>]*>[\s\S]*?</div>\s*(?=<main)',
    '', html, flags=re.IGNORECASE)

# Remove right sidebar comment leftover 
html = re.sub(r'<!--\s*Right Sidebar.*?-->\s*', '', html, flags=re.IGNORECASE)

# Remove stale mobile banner divs we may have added before
html = re.sub(r'<!--\s*AD \d+:.*?-->\s*<div[^>]*block lg:hidden[^>]*>[\s\S]*?</div>\s*', '', html)

# Remove outer flex wrapper if it exists already 
html = re.sub(
    r'<div class="flex flex-col lg:flex-row justify-between min-h-screen pt-16 px-0 shrink-0">',
    '', html)

# Clean up the stray </div> that was the closing of that wrapper
# We'll add our own structure below

# ── Step 3: Clean excessive blank lines ──────────────────────────────────────
html = re.sub(r'\n{3,}', '\n\n', html)

# ── Step 4: Find the <body> open and the header close, insert our new layout ─
# The header ends at </div>\n\n    <main  OR  </div>\n<div class="flex...
# We will insert a fresh outer layout after the header block.

OUTER_LAYOUT_START = f"""
<!-- ═══════════════════════════════════════════════════
     SIX-AD LAYOUT  — ads 1-6 all visible on load
     ═══════════════════════════════════════════════════ -->

<!-- AD 1 (mobile only): 320×50 strip below the nav bar -->
<div class="block lg:hidden flex justify-center w-full bg-black/40" style="min-height:50px;">
  <script data-cfasync="false">atOptions={{'key':'24d82a14f251de0b584c1c1878965100','format':'iframe','height':50,'width':320,'params':{{}}}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
</div>

<div class="flex flex-row justify-between min-h-screen pt-16 px-0">

  <!-- AD 2: Left sticky 160×600 skyscraper -->
  <div class="hidden lg:flex flex-shrink-0 w-[180px] items-start justify-center py-6 bg-black/10">
    <div class="sticky top-20">
      {AD_160x600}
    </div>
  </div>

  <!-- CENTRE: main content -->
  <main class="flex-grow w-full px-2 overflow-x-hidden">
"""

OUTER_LAYOUT_END = f"""
  </main><!-- end centre -->

  <!-- AD 6: Right sticky 160×600 skyscraper -->
  <div class="hidden lg:flex flex-shrink-0 w-[180px] items-start justify-center py-6 bg-black/10">
    <div class="sticky top-20">
      {AD_160x600}
    </div>
  </div>

</div><!-- end six-ad outer flex -->
"""

# ── Insert layout start after the header div ─────────────────────────────────
# Header ends with:  </div>\n\n    and then the old content starts
# We find the closing </div> of the header by looking for id="header"
header_end_match = re.search(r'(</div>\s*)\n(\s*<div id="topSection")', html)
if not header_end_match:
    # fallback: insert after the header div
    header_end_match = re.search(r'(</div>)\s*\n(\s*<div class="header|<div id="topSection")', html)

# Better: find the line that starts topSection and inject wrapper just before it
html = re.sub(
    r'(<div id="topSection"[^>]*>)',
    OUTER_LAYOUT_START + r'\1',
    html, count=1)

# ── Insert layout end before </body> ─────────────────────────────────────────
html = html.replace('</body>', OUTER_LAYOUT_END + '\n</body>', 1)

# ── Step 5: Inside the game info panel (right col), add AD 3 (300×250) ───────
# After the gameDescription paragraph, before the closing </div> of the panel
html = re.sub(
    r'(id="gameDescription"[^>]*>[\s\S]*?</p>)(\s*</div>\s*</div>\s*</div>)',
    rf'\1\n<!-- AD 3: 300×250 inside game-info panel -->\n{AD_300x250}\2',
    html, count=1)

# ── Step 6: Above the game viewport (gameContainer), add AD 4 (728×90) ───────
html = re.sub(
    r'(<div id="gameContainer")',
    f'<!-- AD 4: 728×90 banner directly above the game -->\n{AD_728x90}\n\\1',
    html, count=1)

# ── Step 7: Below the game viewport closing div, add AD 5 (native) ───────────
html = re.sub(
    r'(</div>\s*<!-- end gameContainer closing|</div>\s*\n\s*</div>\s*\n\s*</div>\s*\n\s*</div>)\s*\n(\s*<!--)',
    rf'\1\n<!-- AD 5: Native banner below the game -->\n{AD_NATIVE}\n\2',
    html, count=1)

# Remove duplicate container div id that could have been cloned
html = re.sub(
    r'(<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>\s*){2,}',
    r'<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>',
    html)

# Clean extra blank lines
html = re.sub(r'\n{4,}', '\n\n', html)

# ── Write back ────────────────────────────────────────────────────────────────
with open('play.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done — 6 ads injected into play.html:")
print("  AD 1: 320×50 mobile strip (below nav, phones only)")
print("  AD 2: 160×600 LEFT sticky skyscraper (desktop)")
print("  AD 3: 300×250 inside game-info right panel")
print("  AD 4: 728×90 leaderboard directly above the game")
print("  AD 5: Native banner below the game viewport")
print("  AD 6: 160×600 RIGHT sticky skyscraper (desktop)")
