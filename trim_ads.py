"""
trim_ads.py  —  Reduce ads to a sensible number on each page.

Target:
  play.html     → 3 ads  (left skyscraper, 300x250 in info panel, 728x90 above game)
  games.html    → 3 ads  (728x90 near top, 300x250 mid-page, native near bottom)
  chatroom.html → 2 ads  (728x90 below room buttons, native before footer)
"""
import re

# ─── Ad snippets ────────────────────────────────────────────────────────────
A728 = '''\
<div class="flex justify-center w-full my-6">
  <script data-cfasync="false">atOptions={'key':'24d82a14f251de0b584c1c1878965100','format':'iframe','height':90,'width':728,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
</div>'''

A300 = '''\
<div class="flex justify-center w-full my-6">
  <script data-cfasync="false">atOptions={'key':'cf6a125c26299b4a476c85e2b484cb3a','format':'iframe','height':250,'width':300,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
</div>'''

A160 = '''\
<div class="hidden lg:flex justify-center sticky top-20" style="min-height:600px;">
  <script data-cfasync="false">atOptions={'key':'81f56b1bdcad21cd55ab223c4f4c2c92','format':'iframe','height':600,'width':160,'params':{}};</script>
  <script data-cfasync="false" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
</div>'''

NATIVE = '''\
<div class="flex justify-center w-full my-6">
  <script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
  <div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>'''

# ─── Helper: wipe every ad block in a string ────────────────────────────────
AD_BLOCK = re.compile(
    r'<div[^>]*>\s*'
    r'(?:<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*/invoke\.js[^>]*></script>|'
    r'<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*src=[^>]*/invoke\.js[^>]*></script>|'
    r'<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>)\s*'
    r'</div>',
    re.IGNORECASE)

INLINE_AD = re.compile(
    r'<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*/invoke\.js[^>]*></script>',
    re.IGNORECASE)

NATIVE_BLOCK = re.compile(
    r'<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>',
    re.IGNORECASE)

# Also remove the whole ░░ AD ROW sections we added to games.html
AD_ROW_COMMENT = re.compile(
    r'<!--\s*░░\s*AD ROW\s*░░\s*-->[\s\S]*?(?=<!--|\Z|<section|<footer)',
    re.IGNORECASE)

# And remove sidebar-injected skyscraper wrappers
SIDEBAR_WRAP = re.compile(
    r'<div class="(?:hidden lg:flex|my-4 sticky)[^"]*"[^>]*>\s*<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*/invoke\.js[^>]*></script>\s*</div>',
    re.IGNORECASE)

def wipe_all_ads(html):
    html = AD_ROW_COMMENT.sub('', html)
    html = AD_BLOCK.sub('', html)
    html = SIDEBAR_WRAP.sub('', html)
    html = INLINE_AD.sub('', html)
    html = NATIVE_BLOCK.sub('', html)
    # clean empty/orphaned wrappers
    html = re.sub(r'<div[^>]*class="[^"]*flex justify-center[^"]*"[^>]*>\s*</div>', '', html)
    html = re.sub(r'<div[^>]*class="[^"]*my-\d+[^"]*"[^>]*>\s*</div>', '', html)
    html = re.sub(r'(\n\s*){3,}', '\n\n', html)
    return html

# ════════════════════════════════════════════════════════════════════════════
#  play.html  →  3 ads
# ════════════════════════════════════════════════════════════════════════════
with open('play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = wipe_all_ads(play)

# Restore the one left skyscraper sidebar (already in the sidebar div)
play = play.replace(
    '<!-- Left Sidebar AD 2: 160x600 skyscraper -->\n  <div class="hidden lg:flex flex-shrink-0 w-[180px] items-start justify-center py-6 bg-black/10">\n    <div class="sticky top-20">\n      \n    </div>\n  </div>',
    f'<!-- Left Sidebar AD 2: 160x600 skyscraper -->\n  <div class="hidden lg:flex flex-shrink-0 w-[180px] items-start justify-center py-6 bg-black/10">\n    <div class="sticky top-20">\n      {A160}\n    </div>\n  </div>'
)

# Put 300x250 inside game-info panel (after description paragraph)
play = re.sub(
    r'(id="gameDescription"[^>]*>[\s\S]*?</p>)(\s*</div>\s*</div>\s*</div>)',
    rf'\1\n{A300}\2',
    play, count=1)

# Put 728x90 directly above gameContainer
play = re.sub(
    r'(<div id="gameContainer")',
    f'{A728}\n\\1',
    play, count=1)

with open('play.html', 'w', encoding='utf-8') as f:
    f.write(play)

count = play.count('atOptions') + play.count('effectivegatecpm.com/cb54d')
print(f'play.html    → {count} ads')

# ════════════════════════════════════════════════════════════════════════════
#  games.html  →  3 ads
# ════════════════════════════════════════════════════════════════════════════
with open('games.html', 'r', encoding='utf-8') as f:
    games = f.read()

games = wipe_all_ads(games)

# 1) 728x90 right after the page hero/header section
# Find the first </section> or the games grid heading and insert there
games = re.sub(
    r'(<div[^>]*id=["\']gamesGrid["\'][^>]*>|<div[^>]*class=["\'][^"\']*games-grid[^"\']*["\'][^>]*>|<div[^>]*class=["\'][^"\']*grid[^"\']*gap[^"\']*["\'][^>]*>)',
    f'{A728}\n\\1',
    games, count=1)

# 2) 300x250 roughly mid-page — before the footer
games = games.replace('<footer', f'{A300}\n\n<footer')

# 3) Native banner just before the footer (after the 300x250)
games = games.replace('<footer', f'{NATIVE}\n\n<footer')

with open('games.html', 'w', encoding='utf-8') as f:
    f.write(games)

count = games.count('atOptions') + games.count('effectivegatecpm.com/cb54d')
print(f'games.html   → {count} ads')

# ════════════════════════════════════════════════════════════════════════════
#  chatroom.html  →  2 ads
# ════════════════════════════════════════════════════════════════════════════
with open('chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = wipe_all_ads(chat)

# 1) 728x90 below the room selector buttons
chat = chat.replace(
    '<div class="mb-6 flex flex-wrap gap-3 justify-center" id="roomSelector">',
    f'{A728}\n\n                <div class="mb-6 flex flex-wrap gap-3 justify-center" id="roomSelector">'
)

# 2) Native banner before footer
chat = chat.replace('<footer', f'{NATIVE}\n\n<footer')

with open('chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

count = chat.count('atOptions') + chat.count('effectivegatecpm.com/cb54d')
print(f'chatroom.html → {count} ads')

print('\nDone — ads trimmed to sensible levels.')
