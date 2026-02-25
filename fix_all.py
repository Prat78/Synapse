import re, os

# ═══════════════════════════════════════════════════════════════
#  Ad snippets
# ═══════════════════════════════════════════════════════════════
A728 = ('  <script data-cfasync="false">'
        "atOptions={'key':'24d82a14f251de0b584c1c1878965100','format':'iframe','height':90,'width':728,'params':{}};"
        '</script>\n  <script data-cfasync="false" src="https://www.highperformanceformat.com/'
        '24d82a14f251de0b584c1c1878965100/invoke.js"></script>')

A300 = ('  <script data-cfasync="false">'
        "atOptions={'key':'cf6a125c26299b4a476c85e2b484cb3a','format':'iframe','height':250,'width':300,'params':{}};"
        '</script>\n  <script data-cfasync="false" src="https://www.highperformanceformat.com/'
        'cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>')

NATIVE = ('  <script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/'
          'cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>\n'
          '  <div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>')

def ad_box(inner, cls='flex justify-center w-full my-6'):
    return f'<div class="{cls}">\n{inner}\n</div>'

# ═══════════════════════════════════════════════════════════════
#  TASK 1: Remove pop-under script from every HTML file
# ═══════════════════════════════════════════════════════════════
POP_UNDER = re.compile(
    r'<script[^>]*effectivegatecpm\.com/6f/08/45/6f0845[^>]*></script>\s*',
    re.IGNORECASE)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    cleaned = POP_UNDER.sub('', c)
    if cleaned != c:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(cleaned)
        print(f'[pop-under removed] {fname}')

# ═══════════════════════════════════════════════════════════════
#  TASK 2: Fix chatroom.html — clean rebuild
# ═══════════════════════════════════════════════════════════════
with open('chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

# --- wipe ALL ad blocks ---
chat = re.sub(
    r'<div[^>]*>\s*<script[^>]*>atOptions[\s\S]*?invoke\.js["\']>\s*</script>\s*</div>',
    '', chat, flags=re.IGNORECASE)
chat = re.sub(
    r'<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*invoke\.js[^>]*></script>',
    '', chat, flags=re.IGNORECASE)
chat = re.sub(
    r'<div[^>]*>\s*<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>\s*</div>',
    '', chat, flags=re.IGNORECASE)
chat = re.sub(
    r'<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>',
    '', chat, flags=re.IGNORECASE)

# --- remove the broken left-sidebar wrapper injected by mistake ---
chat = re.sub(
    r'<!--\s*Left Sidebar\s*-->[\s\S]*?</div>\s*\n(\s*<main class="flex-grow)',
    '', chat)
chat = re.sub(
    r'<div class="hidden lg:flex flex-shrink-0 w-\[180px\][^"]*"[^>]*>[\s\S]*?</div>\s*\n(\s*<main)',
    r'\1', chat)

# --- remove duplicate / broken <main> tags ---
# Keep only the real one: <main class="pt-20">
chat = re.sub(r'<main class="flex-grow[^"]*"[^>]*>\s*\n', '', chat)

# --- fix broken title section (remove weird flex wrapper around h1) ---
chat = re.sub(
    r'<div class="text-center mb-8">\s*<div class="flex flex-col md:flex-row items-center justify-between">\s*'
    r'<div class="md:w-1/2 text-left">\s*',
    '<div class="text-center mb-8">\n                    ',
    chat)
# close out the injected wrapper divs after the title block
chat = re.sub(
    r'(Choose a room and start chatting!</p>)</div><div class="md:w-1/2 text-right">[^<]*</div>\s*\n\s*</div>',
    r'\1\n                </div>\n',
    chat)

# --- clean leftovers ---
chat = re.sub(r'<div class="flex justify-center my-4 w-full" style="max-height:90px; overflow:hidden;">\s*</div>', '', chat)
chat = re.sub(r'<div class="container mx-auto px-4">\s*</div>', '', chat)
chat = re.sub(r'<div class="flex justify-center">\s*</div>', '', chat)
chat = re.sub(r'<div class="flex justify-center my-8">\s*<div>\s*</div>\s*</div>', '', chat)
chat = re.sub(r'(\n\s*){3,}', '\n\n', chat)

# --- add clean ads in proper spots ---

# 1) 728x90 below the room selector buttons
chat = chat.replace(
    '<div class="mb-6 flex flex-wrap gap-3 justify-center" id="roomSelector">',
    ad_box(A728) + '\n\n                <div class="mb-6 flex flex-wrap gap-3 justify-center" id="roomSelector">'
)

# 2) 300x250 in the sidebar after stats, inside the lg:hidden block (mobile)
chat = chat.replace(
    'id="totalMessageCount">0</span></div>\n                            </div>\n                        </div>',
    'id="totalMessageCount">0</span></div>\n                            </div>\n                        </div>\n'
    + '                        <div class="mt-4">' + ad_box(A300) + '</div>'
)

# 3) native banner before the footer
chat = chat.replace('<footer', ad_box(NATIVE) + '\n\n<footer')

with open('chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)
print('[chatroom.html] Fixed and ads added.')

# ═══════════════════════════════════════════════════════════════
#  TASK 3: Fill games.html with ads all the way to the bottom
# ═══════════════════════════════════════════════════════════════
with open('games.html', 'r', encoding='utf-8') as f:
    games = f.read()

# wipe old ad blocks first
games = re.sub(
    r'<div[^>]*>\s*<script[^>]*>atOptions[\s\S]*?invoke\.js["\']>\s*</script>\s*</div>',
    '', games, flags=re.IGNORECASE)
games = re.sub(
    r'<script[^>]*>atOptions[\s\S]*?</script>\s*<script[^>]*invoke\.js[^>]*></script>',
    '', games, flags=re.IGNORECASE)
games = re.sub(
    r'<div[^>]*>\s*<script[^>]*async[^>]*effectivegatecpm[^>]*></script>\s*<div[^>]*></div>\s*</div>',
    '', games, flags=re.IGNORECASE)
games = re.sub(r'(\n\s*){3,}', '\n\n', games)

# We'll inject ads after every ~8 game cards by targeting the closing </div> of card groups.
# Strategy: find the games grid section and insert ad rows periodically.
# The game cards have class "game-card" — count occurrences and inject after every 8th closing tag.

CARD_CLOSE = '</div><!-- end game-card -->'
# Since cards may not have that exact comment, use a different landmark.
# Game cards are <div class="...game-card..."> — let's add ads after the games-grid div sections.

# Find the games grid container and add ads interspersed
# Most reliable: inject 3 ad rows evenly spaced before </section> or before footer

ad_row_728 = '\n\n<!-- ░░ AD ROW ░░ -->\n<div class="w-full flex justify-center my-8 px-4">\n' + A728 + '\n</div>\n'
ad_row_300pair = ('\n\n<!-- ░░ AD ROW ░░ -->\n'
                  '<div class="flex flex-wrap justify-center gap-8 my-8 px-4">\n'
                  + '  <div>' + ad_box(A300) + '</div>\n'
                  + '  <div class="hidden md:block">' + ad_box(A300) + '</div>\n'
                  + '</div>\n')
ad_row_native = '\n\n<!-- ░░ AD ROW ░░ -->\n' + ad_box(NATIVE, 'flex justify-center my-8 px-4') + '\n'

# Insert before the footer
games = games.replace('<footer', 
    ad_row_728 + ad_row_300pair + ad_row_native + '\n<footer')

# Also insert inside the page — find the section that wraps game cards
# Look for the closing of the first major game grid and add an ad there
games = re.sub(
    r'(<!-- (?:featured|games|game) [\s\S]{0,40}?-->)',
    r'\1' + ad_row_728,
    games, count=1, flags=re.IGNORECASE)

# Add ads every ~¼ into the page by splitting on </div> patterns
# More reliable: after every "Partner Grid" section or after known structural divs
sections = re.split(r'(<section[^>]*>)', games)
result = []
ad_count = 0
for i, section in enumerate(sections):
    result.append(section)
    if section.startswith('<section') and ad_count < 4:
        result.append(ad_row_728 if ad_count % 2 == 0 else ad_row_300pair)
        ad_count += 1
games = ''.join(result)

# Clean duplicate blank lines
games = re.sub(r'\n{4,}', '\n\n', games)

with open('games.html', 'w', encoding='utf-8') as f:
    f.write(games)
print('[games.html] Ads added all the way down.')

print('\nAll done!')
