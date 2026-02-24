import re

html_728x90 = """
<div class="flex justify-center my-8">
<script>
  atOptions = {
    'key' : '24d82a14f251de0b584c1c1878965100',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
</div>
"""

html_160x600 = """
<div class="flex justify-center my-8 hidden md:block">
<script>
  atOptions = {
    'key' : '81f56b1bdcad21cd55ab223c4f4c2c92',
    'format' : 'iframe',
    'height' : 600,
    'width' : 160,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
</div>
"""

html_300x250 = """
<div class="flex justify-center my-8">
<script>
  atOptions = {
    'key' : 'cf6a125c26299b4a476c85e2b484cb3a',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
</div>
"""

native_banner = """
<div class="flex justify-center my-8">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

# Remove all ad blocks
play = re.sub(r'<div class="flex justify-center.*?">\s*<script>[\s\S]*?invoke\.js"></script>\s*</div>', '', play)
# Remove native banner
play = re.sub(r'<div class="flex justify-center.*?">\s*<script async="async".*?invoke\.js"></script>\s*<div id="container-cb54d.*?></div>\s*</div>', '', play)

# Now play is clean of all those div wrappers with highperformanceformat scripts.
# Let's insert exactly 6 ads, well scattered.

# 1. Thin ad right above the Top Tools Section
play = play.replace('<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->', f'{html_728x90}\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->')

# 2. Box ad inside the empty lg:col-span-12 xl:col-span-12
play = re.sub(r'(<div class="lg:col-span-12 xl:col-span-12">)\s*(</div>)', f'\\1\n{html_300x250}\n\\2', play)

# 3. Native banner between the top tools and the game viewport
play = play.replace('<!-- Full Width Game Container (No max-w constraint) -->', f'{native_banner}\n<!-- Full Width Game Container (No max-w constraint) -->')

# 4. Long ad (160x600) + 5. Thin ad (728x90) + 6. Box ad (300x250)
# Instead of stacking them vertically, let's put them in a flex grid at the bottom below the game viewport.
ad_grid = f"""
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 my-12 items-center justify-items-center">
    {html_160x600.replace('my-8', 'my-2')}
    {html_728x90.replace('my-8', 'my-2 max-w-full overflow-hidden')}
    {html_300x250.replace('my-8', 'my-2')}
</div>
"""
# Insert it after the gameContainer
play = play.replace('</div>\n\n            </div>\n        </div>', f'</div>\n{ad_grid}\n            </div>\n        </div>')

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)

print("Play.html ads cleaned and fixed nicely")
