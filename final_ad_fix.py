import os

ADS_HTML = """
<!-- START OF THE 6 TOP ADS GRID -->
<div class="all-ads-top-grid w-full bg-black/40 border-b border-white/10 pt-24 pb-8 px-4 z-40 relative">
    <div class="container mx-auto">
        <h2 class="text-xs text-center text-gray-500 uppercase tracking-widest mb-6 font-orbitron">Featured Partners</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center">
            <!-- Ad 1: 300x250 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[340px] min-h-[300px]">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Square Banner</div>
                <script type="text/javascript">
                    atOptions = { 'key' : 'cf6a125c26299b4a476c85e2b484cb3a', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
            </div>
            
            <!-- Ad 2: 728x90 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[768px] min-h-[140px] lg:col-span-2">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Leaderboard</div>
                <script type="text/javascript">
                    atOptions = { 'key' : '24d82a14f251de0b584c1c1878965100', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
            </div>

            <!-- Ad 3: 160x600 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[200px] min-h-[650px] md:row-span-2">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Skyscraper</div>
                <script type="text/javascript">
                    atOptions = { 'key' : '81f56b1bdcad21cd55ab223c4f4c2c92', 'format' : 'iframe', 'height' : 600, 'width' : 160, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
            </div>

            <!-- Ad 4: 468x60 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[508px] min-h-[110px]">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Content Banner</div>
                <script type="text/javascript">
                    atOptions = { 'key' : '412228ce3f7e514eff0e088bc88dd0a7', 'format' : 'iframe', 'height' : 60, 'width' : 468, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/412228ce3f7e514eff0e088bc88dd0a7/invoke.js"></script>
            </div>

            <!-- Ad 5: 160x300 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[200px] min-h-[350px]">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Mini Skyscraper</div>
                <script type="text/javascript">
                    atOptions = { 'key' : '4f27449c855a63c1993335475e8b0253', 'format' : 'iframe', 'height' : 300, 'width' : 160, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/4f27449c855a63c1993335475e8b0253/invoke.js"></script>
            </div>

            <!-- Ad 6: 320x50 -->
            <div class="flex flex-col items-center bg-dark/80 p-4 rounded-2xl border border-white/10 shadow-2xl hover:border-primary/50 transition-all w-full max-w-[360px] min-h-[100px]">
                <div class="w-full text-[10px] text-gray-500 mb-2 uppercase tracking-tighter">Mobile Banner</div>
                <script type="text/javascript">
                    atOptions = { 'key' : '3b778bf9b4ac85cd02fc7e17f000d8d5', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {} };
                </script>
                <script type="text/javascript" src="https://www.highperformanceformat.com/3b778bf9b4ac85cd02fc7e17f000d8d5/invoke.js"></script>
            </div>
        </div>
    </div>
</div>
<!-- END OF THE 6 TOP ADS GRID -->
"""

keys_to_remove = [
    'cf6a125c26299b4a476c85e2b484cb3a',
    '81f56b1bdcad21cd55ab223c4f4c2c92',
    '24d82a14f251de0b584c1c1878965100',
    '412228ce3f7e514eff0e088bc88dd0a7',
    '4f27449c855a63c1993335475e8b0253',
    '3b778bf9b4ac85cd02fc7e17f000d8d5'
]

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    skip_script = False
    
    for line in lines:
        # Check if we should start/stop skipping a script block
        if '<script' in line.lower():
            # Check if this script block contains any restricted keys
            # (Simplistic check: if the key is on the same line as <script...>)
            # For multi-line scripts, we'd need more logic, but let's try this.
            if any(key in line for key in keys_to_remove):
                if '</script>' not in line.lower():
                    skip_script = True
                continue # Skip this line
        
        if skip_script:
            if '</script>' in line.lower():
                skip_script = False
            continue
            
        # Also skip lines that are NOT in a block but contain the key 
        # (e.g., the closing tag or the internal lines if we weren't skipping properly)
        if any(key in line for key in keys_to_remove):
             continue

        # If it's the body tag, inject the ads
        if '<body' in line.lower():
            new_lines.append(line)
            new_lines.append(ADS_HTML + "\n")
        else:
            new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for html_file in html_files:
    process_file(html_file)

print("Done!")
