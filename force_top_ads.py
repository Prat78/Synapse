import os
import glob
import re

dir_path = r"c:\Users\abhil\Desktop\website"
html_files = glob.glob(os.path.join(dir_path, "*.html"))

new_ads = """
<!-- ALL SIX ADS - TOP OF PAGE -->
<div class="all-ads-top-container w-full bg-black/20 border-b border-white/10 pt-20 pb-4 px-2 z-40 relative flex flex-wrap items-center justify-center gap-4">
    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 300px; min-height: 250px;">
        <script>
          atOptions = { 'key' : 'cf6a125c26299b4a476c85e2b484cb3a', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
    </div>

    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 160px; min-height: 600px;">
        <script>
          atOptions = { 'key' : '81f56b1bdcad21cd55ab223c4f4c2c92', 'format' : 'iframe', 'height' : 600, 'width' : 160, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
    </div>

    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 728px; min-height: 90px;">
        <script>
          atOptions = { 'key' : '24d82a14f251de0b584c1c1878965100', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
    </div>

    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 468px; min-height: 60px;">
        <script>
          atOptions = { 'key' : '412228ce3f7e514eff0e088bc88dd0a7', 'format' : 'iframe', 'height' : 60, 'width' : 468, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js"></script>
    </div>

    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 160px; min-height: 300px;">
        <script>
          atOptions = { 'key' : '4f27449c855a63c1993335475e8b0253', 'format' : 'iframe', 'height' : 300, 'width' : 160, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js"></script>
    </div>

    <div class="flex items-center justify-center bg-dark/50 p-2 rounded-xl shadow-lg" style="min-width: 320px; min-height: 50px;">
        <script>
          atOptions = { 'key' : '3b778bf9b4ac85cd02fc7e17f000d8d5', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {} };
        </script>
        <script src="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js"></script>
    </div>
</div>
<!-- END ALL SIX ADS -->
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # REMOVE ALL EXISTING ADS
    # Remove containers doing flex center with ad code inside
    content = re.sub(r'<div class="[^"]*">[\s\n]*<div[^>]*>[\s\n]*<script>[\s\n]*atOptions = \{[\s\S]*?invoke\.js"></script>[\s\n]*</div>[\s\n]*</div>', '', content)
    # Remove any un-wrapped atOptions blocks
    content = re.sub(r'<div[^>]*>[\s\n]*<script>[\s\n]*atOptions = \{[\s\S]*?invoke\.js"></script>[\s\n]*</div>', '', content)
    content = re.sub(r'<script>[\s\n]*atOptions = \{[\s\S]*?invoke\.js"></script>', '', content)
    # Remove any previous unified blocks or floating wrappers
    content = re.sub(r'<!-- ALL SIX ADS [\s\S]*?<!-- END ALL SIX ADS -->\s*', '', content)
    content = re.sub(r'<!-- NEW ADS BLOCK -->[\s\S]*?<!-- END NEW ADS BLOCK -->\s*', '', content)
    content = re.sub(r'<div class="fixed bottom-.*?>.*?invoke\.js"></script>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # In some pages, the navbar has pt-16 or similar on the main content wrap. We will place our big ad container right below the </nav>
    
    # Inject new_ads right after </nav>
    if '</nav>' in content:
        content = content.replace('</nav>', '</nav>\n' + new_ads, 1)
    elif '<body' in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + new_ads, content, count=1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Placed all six ads at the very top of every page.")
