import os
import re

# Precise Ad Script Definitions
AD_CONFIG = {
    'leaderboard_728x90': {
        'key': '24d82a14f251de0b584c1c1878965100',
        'html': """<div class="ad-slot-leaderboard flex justify-center my-8 w-full overflow-hidden">
    <div class="bg-black/20 p-2 rounded-lg border border-white/5 shadow-xl text-center" style="min-width: 728px; min-height: 90px;">
        <span class="block text-[10px] text-gray-600 mb-1 uppercase tracking-widest font-orbitron">Featured Partner</span>
        <script type="text/javascript">atOptions = { 'key' : '24d82a14f251de0b584c1c1878965100', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
    </div>
</div>"""
    },
    'skyscraper_160x600': {
        'key': '81f56b1bdcad21cd55ab223c4f4c2c92',
        'html': """<div class="ad-slot-skyscraper flex justify-center my-4 w-full">
    <div class="bg-black/20 p-2 rounded-xl border border-white/5 shadow-lg text-center" style="min-width: 160px; min-height: 600px;">
        <span class="block text-[9px] text-gray-600 mb-1 uppercase font-orbitron">Recommended</span>
        <script type="text/javascript">atOptions = { 'key' : '81f56b1bdcad21cd55ab223c4f4c2c92', 'format' : 'iframe', 'height' : 600, 'width' : 160, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
    </div>
</div>"""
    },
    'square_300x250': {
        'key': 'cf6a125c26299b4a476c85e2b484cb3a',
        'html': """<div class="ad-slot-square flex justify-center my-10 w-full px-4">
    <div class="bg-black/40 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/30 transition-all text-center" style="min-width: 300px; min-height: 250px;">
        <span class="block text-[10px] text-gray-500 mb-2 uppercase tracking-tighter font-orbitron">Premium Content</span>
        <script type="text/javascript">atOptions = { 'key' : 'cf6a125c26299b4a476c85e2b484cb3a', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
    </div>
</div>"""
    },
    'minisky_160x300': {
        'key': '4f27449c855a63c1993335475e8b0253',
        'html': """<div class="ad-slot-minisky flex justify-center my-4 w-full">
    <div class="bg-black/20 p-2 rounded-xl border border-white/5 shadow-lg text-center" style="min-width: 160px; min-height: 300px;">
        <span class="block text-[9px] text-gray-600 mb-1 uppercase font-orbitron">Promoted</span>
        <script type="text/javascript">atOptions = { 'key' : '4f27449c855a63c1993335475e8b0253', 'format' : 'iframe', 'height' : 300, 'width' : 160, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js"></script>
    </div>
</div>"""
    },
    'content_468x60': {
        'key': '412228ce3f7e514eff0e088bc88dd0a7',
        'html': """<div class="ad-slot-content flex justify-center my-8 w-full overflow-hidden">
    <div class="bg-black/20 p-2 rounded-lg border border-white/5 shadow-md text-center" style="min-width: 468px; min-height: 60px;">
        <span class="block text-[10px] text-gray-600 mb-1 uppercase font-orbitron">Advertisement</span>
        <script type="text/javascript">atOptions = { 'key' : '412228ce3f7e514eff0e088bc88dd0a7', 'format' : 'iframe', 'height' : 60, 'width' : 468, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js"></script>
    </div>
</div>"""
    },
    'mobile_320x50': {
        'key': '3b778bf9b4ac85cd02fc7e17f000d8d5',
        'html': """<div class="ad-slot-mobile flex justify-center my-4 w-full">
    <div class="bg-black/10 p-1 rounded-md border border-white/5 shadow-sm text-center" style="min-width: 320px; min-height: 50px;">
        <span class="block text-[8px] text-gray-600 uppercase font-orbitron">Sponsor Hub</span>
        <script type="text/javascript">atOptions = { 'key' : '3b778bf9b4ac85cd02fc7e17f000d8d5', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {} };</script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js"></script>
    </div>
</div>"""
    }
}

ALL_KEYS = [ad['key'] for ad in AD_CONFIG.values()]

def process_file(filepath):
    print(f"Professional spread for {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. DEEP CLEAN STAGE
    # Remove all scripts with keys
    for key in ALL_KEYS:
        content = re.sub(r'<script[^>]*>[\s\S]*?' + re.escape(key) + r'[\s\S]*?</script>', '', content)
        content = re.sub(r'<script[^>]*src="[^"]*?' + re.escape(key) + r'[^"]*?"[^>]*></script>', '', content)
        content = re.sub(r'<div class="ad-slot-[\w-]+">[\s\S]*?</div>\s*</div>', '', content, flags=re.MULTILINE)
        content = re.sub(r'<div class="ad-slot-[\w-]+ flex[\s\S]*?</div>\s*</div>', '', content, flags=re.MULTILINE)
    
    # Clean identified broken injections (inside class strings)
    content = re.sub(r'reveal stagger-1\s*<div class="ad-slot-square[\s\S]*?</div>\s*</div>\s*">', 'reveal stagger-1">', content)
    content = re.sub(r'reveal\s*<div class="ad-slot-content[\s\S]*?</div>\s*</div>\s*stagger-3">', 'reveal stagger-3">', content)
    
    # Remove old grid blocks
    content = re.sub(r'<!-- START OF THE 6 TOP ADS GRID -->[\s\S]*?<!-- END OF THE 6 TOP ADS GRID -->', '', content)
    content = re.sub(r'<!-- ALL SIX ADS - TOP OF PAGE -->[\s\S]*?<!-- END ALL SIX ADS -->', '', content)
    
    # Clean up empty tags left by previous regexes
    content = re.sub(r'<div[^>]*>\s*<script>\s*</script>\s*</div>\s*</div>', '', content)

    # 2. PRECISE INJECTION STAGE
    
    # Anchor: Head Preloads
    head_match = re.search(r'</head>', content, re.IGNORECASE)
    if head_match:
        preloads = "\n    <!-- Ad Performance Optimization -->\n"
        for ad in AD_CONFIG.values():
            preloads += f'    <link rel="preload" href="https://www.highperformanceformat.com/{ad["key"]}/invoke.js" as="script">\n'
        content = content.replace('</head>', preloads + '</head>', 1)

    # Ad 1: Mobile Banner (320x50) - Very Top
    body_match = re.search(r'(<body[^>]*>)', content, re.IGNORECASE)
    if body_match:
        content = content.replace(body_match.group(1), body_match.group(1) + "\n" + AD_CONFIG['mobile_320x50']['html'] + "\n", 1)

    # Ad 2: Main Leaderboard (728x90) - After Nav
    nav_match = re.search(r'(</nav>|<div class="header">)', content, re.IGNORECASE)
    if nav_match:
        content = content[:nav_match.end()] + "\n" + AD_CONFIG['leaderboard_728x90']['html'] + content[nav_match.end():]

    # Ad 3: Skyscraper (160x600) - Left Sidebar Start
    left_match = re.search(r'(<!-- Left Sidebar -->\s*<div[^>]*>)', content, re.IGNORECASE)
    if left_match:
        content = content[:left_match.end()] + "\n" + AD_CONFIG['skyscraper_160x600']['html'] + content[left_match.end():]
    else:
        # Fallback for pages without sidebar
        content = content.replace(AD_CONFIG['leaderboard_728x90']['html'], AD_CONFIG['leaderboard_728x90']['html'] + "\n" + AD_CONFIG['skyscraper_160x600']['html'], 1)

    # Ad 4: Hero Square (300x250) - After H1
    h1_match = re.search(r'(</h1>)', content, re.IGNORECASE)
    if h1_match:
        content = content.replace('</h1>', '</h1>\n' + AD_CONFIG['square_300x250']['html'], 1)

    # Ad 5: Mini Sky (160x300) - Right Sidebar Start
    right_match = re.search(r'(<!-- Right Sidebar -->\s*<div[^>]*>)', content, re.IGNORECASE)
    if right_match:
        content = content[:right_match.end()] + "\n" + AD_CONFIG['minisky_160x300']['html'] + content[right_match.end():]
    else:
         # Fallback for pages without right sidebar - Put before footer
         footer_match = re.search(r'<footer', content, re.IGNORECASE)
         if footer_match:
             content = content[:footer_match.start()] + "\n" + AD_CONFIG['minisky_160x300']['html'] + content[footer_match.start():]

    # Ad 6: Content Banner (468x60) - Before Games Grid / Features
    grid_match = re.search(r'(id="gamesGrid"|class="mt-20"|reveal stagger-3)', content, re.IGNORECASE)
    if grid_match:
        content = content[:grid_match.start()] + "\n" + AD_CONFIG['content_468x60']['html'] + content[grid_match.start():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for f in os.listdir('.'):
    if f.endswith('.html'):
        process_file(f)

print("Pro Spread Deployment Success.")
