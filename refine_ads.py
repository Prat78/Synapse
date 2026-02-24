import os
import re

BANNER_1 = """<script>(function(vre){var d=document,s=d.createElement('script'),l=d.scripts[d.scripts.length-1];s.settings=vre||{};s.src="\\/\\/rapid-university.com\\/b.XBVBs_d\\/G\\/lI0KY\\/WtcT\\/zemmE9euGZ\\/U-lmkqPpTSYS4OMLjtEX3\\/NwDWUmt\\/NVjSgTyBM\\/T\\/c\\/0XOnQg";s.async=true;s.referrerPolicy='no-referrer-when-downgrade';l.parentNode.insertBefore(s,l);})({})</script>"""
BANNER_2 = """<script>(function(xrx){var d=document,s=d.createElement('script'),l=d.scripts[d.scripts.length-1];s.settings=xrx||{};s.src="\\/\\/rapid-university.com\\/b.XYVysQdXGRl\\/0SYRWicJ\\/Te\\/m\\/9\\/uNZ\\/UDlZkxP\\/TEYd4dMgjeIe5\\/MgT\\/cOtaNLj-giyHM\\/j\\/kGyfMvQe";s.async=true;s.referrerPolicy='no-referrer-when-downgrade';l.parentNode.insertBefore(s,l);})({})</script>"""
BANNER_3 = """<script>(function(lzu){var d=document,s=d.createElement('script'),l=d.scripts[d.scripts.length-1];s.settings=lzu||{};s.src="\\/\\/rapid-university.com\\/bFXDV\\/s.d\\/Gglc0\\/YUW\\/cd\\/LeYmg9\\/usZhU\\/lskkPBT\\/Yx4\\/MQjmI\\/5vMEzIM-tvN\\/jfg\\/yuMnjCkZz\\/N\\/w_";s.async=true;s.referrerPolicy='no-referrer-when-downgrade';l.parentNode.insertBefore(s,l);})({})</script>"""
BANNER_4 = """<script>(function(msfr){var d=document,s=d.createElement('script'),l=d.scripts[d.scripts.length-1];s.settings=msfr||{};s.src="\\/\\/quickwittedconclusion.com\\/cHDa9.6obO2B5\\/lySKWUQc9xNij-glyFMfjgka3uMRye0\\/2YOPD\\/IQyeOUTdcS3p";s.async=true;s.referrerPolicy='no-referrer-when-downgrade';l.parentNode.insertBefore(s,l);})({})</script>"""

GRID_BLOCK = f"""
<!-- Optimized Subtle Grid -->
<div class="container mx-auto px-4 my-16">
    <h3 class="text-center font-orbitron text-[10px] text-gray-700 uppercase tracking-[0.4em] mb-6 opacity-40">Sponsored Partners</h3>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;width:100%;">
        <div class="ad-container overflow-hidden rounded-2xl border border-white/5 bg-white/5 p-1 opacity-70 hover:opacity-100 transition-opacity">{BANNER_1}</div>
        <div class="ad-container overflow-hidden rounded-2xl border border-white/5 bg-white/5 p-1 opacity-70 hover:opacity-100 transition-opacity">{BANNER_2}</div>
        <div class="ad-container overflow-hidden rounded-2xl border border-white/5 bg-white/5 p-1 opacity-70 hover:opacity-100 transition-opacity">{BANNER_3}</div>
        <div class="ad-container overflow-hidden rounded-2xl border border-white/5 bg-white/5 p-1 opacity-70 hover:opacity-100 transition-opacity">{BANNER_4}</div>
    </div>
</div>
"""

def refine_ads(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. REMOVE ALL OLD GRIDS (8-box ones)
    content = re.sub(r'<!-- High-Density Partner Grid -->.*?<!-- High-Density Partner Grid -->', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- High-Density Partner Grid -->.*?</div>\s+</div>\s+</div>', '', content, flags=re.DOTALL) # Catch incomplete removals
    
    # 2. INJECT NEW SUBTLE GRID before footer
    if '<!-- Optimized Subtle Grid -->' not in content:
        if '<footer' in content:
            content = content.replace('<footer', GRID_BLOCK + '\n<footer')
        elif '</footer>' in content:
             content = content.replace('</footer>', '</footer>\n' + GRID_BLOCK)

    # 3. CLEAN UP Header/Meta scripts to be less laggy (Keep 1 universal handler, rotate others)
    # We will keep the 4 specific handlers but mark them as async (they already are)
    
    # 4. Remove any "Grid Removed" comments or broken tags
    content = content.replace('<!-- Grid Removed for Performance -->', '')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Main pages
for f_name in ['index.html', 'games.html', 'play.html']:
    if os.path.exists(f_name):
        print(f"Refining {f_name}...")
        refine_ads(f_name)

print("Ads refined to be subtle and performance-friendly.")
