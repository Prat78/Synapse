
import re
import os

def redo_all_ads():
    # Ad Templates
    html_728x90 = """
<div class="flex justify-center my-8 w-full">
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
<div class="my-4 sticky top-24">
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
<div class="flex justify-center my-4">
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
<div class="flex justify-center my-8 w-full">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

    partner_grid = f"""
<section class="container mx-auto px-4 py-16">
    <div class="text-center mb-12">
        <h2 class="text-3xl font-orbitron font-bold text-glow italic"><span class="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">SYNAPSE PREMIUM PARTNERS</span></h2>
        <p class="text-gray-500 text-xs uppercase tracking-widest mt-2">Aggressive Monetization Grid v4.0</p>
    </div>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {html_300x250}
        {html_300x250}
        {html_300x250}
        {html_300x250}
        {html_300x250}
        {html_300x250}
        {html_300x250}
        {html_300x250}
    </div>
</section>
"""

    def process_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add Sidebars to files that don't have them (index.html)
        if 'index.html' in file_path and '<div class="flex flex-col lg:flex-row justify-between' not in content:
            # Wrap standard main content in a flexbox with sidebars
            sidebar_structure_start = f"""
<div class="flex flex-col lg:flex-row justify-between min-h-screen pt-16 px-0 shrink-0">
    <!-- Left Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
    </div>
    <main class="flex-grow w-full px-2">
"""
            sidebar_structure_end = f"""
    </main>
    <!-- Right Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
    </div>
</div>
"""
            # Insert after nav
            content = content.replace('</nav>', '</nav>' + sidebar_structure_start)
            # Insert before footer
            content = content.replace('<footer', sidebar_structure_end + '<footer')
        
        # 2. Add Partner Grid before footer
        if partner_grid not in content:
            content = content.replace('<footer', partner_grid + '<footer')

        # 3. Add more 728x90 banners
        if content.count('24d82a14f251de0b584c1c1878965100') < 3:
            # Add one at the top of main
            content = content.replace('<main>', '<main>' + html_728x90)
            # Add one before sitemap/footer links
            content = content.replace('</footer>', html_728x90 + '</footer>')

        # 4. Add Native banner middle of page
        if 'cb54d1e3a7a7a676c81b222b316e2f9d' not in content:
             content = content.replace('</section>', '</section>' + native_banner, 1)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {file_path}")

    files_to_process = [
        'c:\\Users\\abhil\\Desktop\\website\\index.html',
        'c:\\Users\\abhil\\Desktop\\website\\games.html',
        'c:\\Users\\abhil\\Desktop\\website\\play.html',
        'c:\\Users\\abhil\\Desktop\\website\\chatroom.html',
        'c:\\Users\\abhil\\Desktop\\website\\articles.html',
        'c:\\Users\\abhil\\Desktop\\website\\about.html'
    ]

    for f in files_to_process:
        if os.path.exists(f):
            process_file(f)

if __name__ == "__main__":
    redo_all_ads()
