import os
import re

# Each ad block is wrapped in a consistent container for spacing and visual style.
# We'll use different layouts for different ad sizes.

ADS_DATA = {
    'cf6a125c26299b4a476c85e2b484cb3a': { # 300x250
        'html': """
<div class="ad-block my-6 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-2" style="min-width: 300px; min-height: 250px;">
        <span class="block text-[10px] text-gray-500 uppercase tracking-widest mb-1 text-center">SPONSORED</span>
        <script type="text/javascript">
            atOptions = { 'key' : 'cf6a125c26299b4a476c85e2b484cb3a', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
    </div>
</div>"""
    },
    '81f56b1bdcad21cd55ab223c4f4c2c92': { # 160x600
        'html': """
<div class="ad-block my-6 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-2" style="min-width: 160px; min-height: 600px;">
        <span class="block text-[10px] text-gray-500 uppercase tracking-widest mb-1 text-center">PARTNER</span>
        <script type="text/javascript">
            atOptions = { 'key' : '81f56b1bdcad21cd55ab223c4f4c2c92', 'format' : 'iframe', 'height' : 600, 'width' : 160, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
    </div>
</div>"""
    },
    '24d82a14f251de0b584c1c1878965100': { # 728x90
        'html': """
<div class="ad-block my-8 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-2" style="min-width: 728px; min-height: 90px; max-width: 100%; overflow-x: auto;">
        <span class="block text-[10px] text-gray-500 uppercase tracking-widest mb-1 text-center">FEATURED</span>
        <script type="text/javascript">
            atOptions = { 'key' : '24d82a14f251de0b584c1c1878965100', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
    </div>
</div>"""
    },
    '412228ce3f7e514eff0e088bc88dd0a7': { # 468x60
        'html': """
<div class="ad-block my-6 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-2" style="min-width: 468px; min-height: 60px; max-width: 100%; overflow-x: auto;">
        <span class="block text-[10px] text-gray-500 uppercase tracking-widest mb-1 text-center">ADVERTISEMENT</span>
        <script type="text/javascript">
            atOptions = { 'key' : '412228ce3f7e514eff0e088bc88dd0a7', 'format' : 'iframe', 'height' : 60, 'width' : 468, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js"></script>
    </div>
</div>"""
    },
    '4f27449c855a63c1993335475e8b0253': { # 160x300
        'html': """
<div class="ad-block my-6 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-2" style="min-width: 160px; min-height: 300px;">
        <span class="block text-[10px] text-gray-500 uppercase tracking-widest mb-1 text-center">PROMOTED</span>
        <script type="text/javascript">
            atOptions = { 'key' : '4f27449c855a63c1993335475e8b0253', 'format' : 'iframe', 'height' : 300, 'width' : 160, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js"></script>
    </div>
</div>"""
    },
    '3b778bf9b4ac85cd02fc7e17f000d8d5': { # 320x50
        'html': """
<div class="ad-block my-4 flex justify-center w-full">
    <div class="overflow-hidden rounded-xl shadow-2xl border border-white/10 bg-black/40 p-1" style="min-width: 320px; min-height: 50px;">
        <span class="block text-[8px] text-gray-600 uppercase tracking-widest text-center">SYNAPSE PARTNER</span>
        <script type="text/javascript">
            atOptions = { 'key' : '3b778bf9b4ac85cd02fc7e17f000d8d5', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {} };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js"></script>
    </div>
</div>"""
    }
}

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. First, scrape out all existing instances of these ads to start fresh
    for key in ADS_DATA.keys():
        # Match script blocks
        pattern_script = r'<script[^>]*>[\s\S]*?' + re.escape(key) + r'[\s\S]*?</script>'
        content = re.sub(pattern_script, '', content)
        # Match invoke scripts
        pattern_invoke = r'<script[^>]*src="[^"]*?' + re.escape(key) + r'[^"]*?"[^>]*></script>'
        content = re.sub(pattern_invoke, '', content)
        # Match the container grid from before 
        content = re.sub(r'<!-- START OF THE 6 TOP ADS GRID -->[\s\S]*?<!-- END OF THE 6 TOP ADS GRID -->', '', content)
        content = re.sub(r'<!-- ALL SIX ADS - TOP OF PAGE -->[\s\S]*?<!-- END ALL SIX ADS -->', '', content)
        # Match the div containers
        content = re.sub(r'<div class="ad-block[\s\S]*?' + re.escape(key) + r'[\s\S]*?</div>\s*</div>', '', content)

    # 2. Inject them distributedly
    # We'll use a specific order and look for suitable insertion points
    keys = list(ADS_DATA.keys())
    
    # 2a. First Ad (Leaderboard 728x90) - Top of page inside <main> or right after nav
    # Find the first <main> or first section after nav
    ins_728 = re.search(r'(<nav[\s\S]*?</nav>)', content, re.IGNORECASE)
    if ins_728:
        content = content[:ins_728.end()] + "\n" + ADS_DATA['24d82a14f251de0b584c1c1878965100']['html'] + content[ins_728.end():]
    
    # 2b. Second Ad (Skyscraper 160x600) - Start of Left Sidebar
    ins_sidebar = re.search(r'(<!-- Left Sidebar -->[\s\S]*?<div[^>]*>)', content, re.IGNORECASE)
    if ins_sidebar:
        content = content[:ins_sidebar.end()] + "\n" + ADS_DATA['81f56b1bdcad21cd55ab223c4f4c2c92']['html'] + content[ins_sidebar.end():]

    # 2c. Third Ad (300x250 Square) - Middle of first section (e.g., after hero text)
    hero_match = re.search(r'(</button>|</h1>|</h2>)', content, re.IGNORECASE)
    if hero_match:
         content = content[:hero_match.end()] + "\n" + ADS_DATA['cf6a125c26299b4a476c85e2b484cb3a']['html'] + content[hero_match.end():]

    # 2d. Fourth Ad (468x60) - Before the FAQ/Grid section
    grid_match = re.search(r'(<div\s+class="mt-20\s+reveal\s+stagger-5">|<div[^>]*id="gamesGrid">)', content, re.IGNORECASE)
    if grid_match:
        content = content[:grid_match.start()] + "\n" + ADS_DATA['412228ce3f7e514eff0e088bc88dd0a7']['html'] + content[grid_match.start():]

    # 2e. Fifth Ad (160x300 Mini Skyscraper) - Start of Right Sidebar
    ins_rsidebar = re.search(r'(<!-- Right Sidebar -->[\s\S]*?<div[^>]*>)', content, re.IGNORECASE)
    if ins_rsidebar:
        content = content[:ins_rsidebar.end()] + "\n" + ADS_DATA['4f27449c855a63c1993335475e8b0253']['html'] + content[ins_rsidebar.end():]

    # 2f. Sixth Ad (320x50 Mobile) - Right before Footer
    footer_match = re.search(r'(<footer)', content, re.IGNORECASE)
    if footer_match:
        content = content[:footer_match.start()] + "\n" + ADS_DATA['3b778bf9b4ac85cd02fc7e17f000d8d5']['html'] + content[footer_match.start():]

    # Clean up double newlines
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Target all HTML files
for f in os.listdir('.'):
    if f.endswith('.html'):
        process_file(f)

print("Done spreading ads!")
