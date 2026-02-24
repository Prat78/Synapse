import os
import re

# We will target ONLY the problematic domain and its handlers.
BAD_DOMAIN = "quickwittedconclusion.com"
GOOD_BANNER = "//rapid-university.com/b.XBVBs_d/G/lI0KY/WtcT/zemmE9euGZ/U-lmkqPpTSYS4OMLjtEX3/NwDWUmt/NVjSgTyBM/T/c/0XOnQg"

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove script blocks that contain the bad domain
    # This catches psffcg, amz, and other named handlers.
    # We look for <script> blocks that contain BAD_DOMAIN
    content = re.sub(r'<script>.*?' + re.escape(BAD_DOMAIN) + r'.*?<\/script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Specifically remove "Direct Force-Pop" and "Direct Pop-Under" comments and following script if they were left
    content = re.sub(r'<!-- Direct Force-Pop -->\s*<script>.*?<\/script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<!-- Direct Pop-Under Handler.*?-->\s*<script>.*?<\/script>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 3. Clean up the grid slots if they were using the bad domain but were not in a script block (rare but safe to check)
    # Actually, most grid slots are in script blocks, so step 1 handles them.
    # But if there's a script tag ALREADY containing the bad domain, step 1 wiped it, leaving an empty ad-container.
    # We want to fill those ad-containers with a working banner.
    
    def fill_empty_ads(match):
        return f'<div class="ad-container overflow-hidden rounded-2xl border border-white/5 bg-white/5 p-1 opacity-70 hover:opacity-100 transition-opacity"><script>(function(v){{var d=document,s=d.createElement("script"),l=d.scripts[d.scripts.length-1];s.settings=v||{{}};s.src="{GOOD_BANNER}";s.async=true;l.parentNode.insertBefore(s,l);}})({{}})</script></div>'
    
    # Match empty ad-containers or those where the script was removed
    content = re.sub(r'<div class="ad-container[^>]*>\s*<\/div>', fill_empty_ads, content)

    # 4. Final sweep for any raw URLs of the bad domain strings (even in JS variables)
    content = content.replace(BAD_DOMAIN, "about:blank") # Fallback to prevent redirects

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Target files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    print(f"Cleaning {f}...")
    clean_file(f)

# Also clean script.js if it has it
if os.path.exists('script.js'):
    print("Cleaning script.js...")
    clean_file('script.js')

print("Exhaustive cleanup done.")
