import os
import re

# Deep clean patterns
CLEAN_PATTERNS = [
    r'<!-- START OF THE 6 TOP ADS GRID -->[\s\S]*?<!-- END OF THE 6 TOP ADS GRID -->',
    r'<!-- ALL SIX ADS - TOP OF PAGE -->[\s\S]*?<!-- END ALL SIX ADS -->',
    r'<!-- AD PERFORMANCE OPTIMIZATION -->[\s\S]*?<!-- END AD PERFORMANCE OPTIMIZATION -->',
    r'<div class="ad-slot-[\w-]+">[\s\S]*?</div>',
    r'<div class="ad-container">[\s\S]*?</div>',
    r'<div class="ad-block">[\s\S]*?</div>',
     # Specific keys
    r'<script[^>]*>[\s\S]*?cf6a125c26299b4a476c85e2b484cb3a[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?cf6a125c26299b4a476c85e2b484cb3a[\s\S]*?</script>',
    r'<script[^>]*>[\s\S]*?81f56b1bdcad21cd55ab223c4f4c2c92[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?81f56b1bdcad21cd55ab223c4f4c2c92[\s\S]*?</script>',
    r'<script[^>]*>[\s\S]*?24d82a14f251de0b584c1c1878965100[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?24d82a14f251de0b584c1c1878965100[\s\S]*?</script>',
    r'<script[^>]*>[\s\S]*?412228ce3f7e514eff0e088bc88dd0a7[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?412228ce3f7e514eff0e088bc88dd0a7[\s\S]*?</script>',
    r'<script[^>]*>[\s\S]*?4f27449c855a63c1993335475e8b0253[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?4f27449c855a63c1993335475e8b0253[\s\S]*?</script>',
    r'<script[^>]*>[\s\S]*?3b778bf9b4ac85cd02fc7e17f000d8d5[\s\S]*?</script>',
    r'<script[^>]*src="[^"]*?3b778bf9b4ac85cd02fc7e17f000d8d5[\s\S]*?</script>'
]

AD_SCRIPTS = {
    '300x250': """<script type="text/javascript">
	atOptions = {
		'key' : 'cf6a125c26299b4a476c85e2b484cb3a',
		'format' : 'iframe',
		'height' : 250,
		'width' : 300,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>""",
    '160x600': """<script type="text/javascript">
	atOptions = {
		'key' : '81f56b1bdcad21cd55ab223c4f4c2c92',
		'format' : 'iframe',
		'height' : 600,
		'width' : 160,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>""",
    '728x90': """<script type="text/javascript">
	atOptions = {
		'key' : '24d82a14f251de0b584c1c1878965100',
		'format' : 'iframe',
		'height' : 90,
		'width' : 728,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>""",
    '468x60': """<script type="text/javascript">
	atOptions = {
		'key' : '412228ce3f7e514eff0e088bc88dd0a7',
		'format' : 'iframe',
		'height' : 60,
		'width' : 468,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js"></script>""",
    '160x300': """<script type="text/javascript">
	atOptions = {
		'key' : '4f27449c855a63c1993335475e8b0253',
		'format' : 'iframe',
		'height' : 300,
		'width' : 160,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js"></script>""",
    '320x50': """<script type="text/javascript">
	atOptions = {
		'key' : '3b778bf9b4ac85cd02fc7e17f000d8d5',
		'format' : 'iframe',
		'height' : 50,
		'width' : 320,
		'params' : {}
	};
</script>
<script type="text/javascript" src="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js"></script>"""
}

def wrap_ad(ad_type, ad_html):
    return f'<div class="ad-slot-{ad_type} flex justify-center my-4 overflow-hidden rounded-lg">{ad_html}</div>'

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Deep Clean
    for pattern in CLEAN_PATTERNS:
        content = re.sub(pattern, '', content)

    # Distributed Injection
    
    # 1. TOP BANNER (320x50) - Notification style
    body_tag_match = re.search(r'(<body[^>]*>)', content, re.IGNORECASE)
    if body_tag_match:
        tag = body_tag_match.group(1)
        ad = wrap_ad('top-banner', AD_SCRIPTS['320x50'])
        content = content.replace(tag, tag + "\n" + ad + "\n", 1)

    # 2. MAIN LEADERBOARD (728x90) - Below Nav
    nav_end_match = re.search(r'(</nav>|header-placeholder)', content, re.IGNORECASE)
    if nav_end_match:
        tag = nav_end_match.group(0)
        ad = wrap_ad('leaderboard', AD_SCRIPTS['728x90'])
        content = content.replace(tag, tag + "\n" + ad + "\n", 1)
    
    # 3. SIDEBAR LEFT (160x600)
    sidebar_left_match = re.search(r'(<!-- Left Sidebar -->[\s\S]*?<div[^>]*>)', content, re.IGNORECASE)
    if sidebar_left_match:
        tag = sidebar_left_match.group(0)
        ad = wrap_ad('skyscraper', AD_SCRIPTS['160x600'])
        content = content.replace(tag, tag + "\n" + ad + "\n", 1)

    # 4. HERO SQUARE (300x250) - Middle of hero section
    hero_mid_match = re.search(r'(reveal stagger-1|reveal stagger-2)', content, re.IGNORECASE)
    if hero_mid_match:
        tag = hero_mid_match.group(0)
        ad = wrap_ad('square', AD_SCRIPTS['300x250'])
        content = content.replace(tag, tag + "\n" + ad + "\n", 1)

    # 5. SIDEBAR RIGHT (160x300)
    sidebar_right_match = re.search(r'(<!-- Right Sidebar -->[\s\S]*?<div[^>]*>)', content, re.IGNORECASE)
    if sidebar_right_match:
        tag = sidebar_right_match.group(0)
        ad = wrap_ad('minisky', AD_SCRIPTS['160x300'])
        content = content.replace(tag, tag + "\n" + ad + "\n", 1)

    # 6. CONTENT BANNER (468x60) - Above Grid
    content_banner_match = re.search(r'(stagger-3|id="gamesGrid"|class="mt-20")', content, re.IGNORECASE)
    if content_banner_match:
        tag = content_banner_match.group(0)
        ad = wrap_ad('content-banner', AD_SCRIPTS['468x60'])
        content = content.replace(tag, ad + "\n" + tag, 1)

    # Final touch: Preloads in Head
    head_end_match = re.search(r'(</head>)', content, re.IGNORECASE)
    if head_end_match:
        tag = head_end_match.group(0)
        preloads = """
    <!-- AD PERFORMANCE OPTIMIZATION -->
    <link rel="preconnect" href="https://www.highperformanceformat.com">
    <link rel="dns-prefetch" href="https://www.highperformanceformat.com">
    <link rel="preload" href="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js" as="script">
    <link rel="preload" href="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js" as="script">
    <link rel="preload" href="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js" as="script">
    <link rel="preload" href="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js" as="script">
    <link rel="preload" href="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js" as="script">
    <link rel="preload" href="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js" as="script">
    <!-- END AD PERFORMANCE OPTIMIZATION -->
"""
        content = content.replace(tag, preloads + tag, 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Run on all files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    process_file(html_file)

print("Distributed 6 ads across all pages!")
