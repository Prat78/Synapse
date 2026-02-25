
import re
import os

def redo_all_ads_extreme():
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
<div class="flex justify-center my-8 w-full border-t border-b border-white/5 py-4">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

    partner_grid = f"""
<section class="container mx-auto px-4 py-16 border-t border-white/10">
    <div class="text-center mb-12">
        <h2 class="text-3xl font-orbitron font-bold text-glow italic"><span class="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">SYNAPSE PREMIUM PARTNERS</span></h2>
        <p class="text-gray-500 text-xs uppercase tracking-widest mt-2">Aggressive Monetization Grid v5.0</p>
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

    floating_ads = f"""
<!-- Floating Ads -->
<div class="fixed bottom-4 left-4 z-[9999] hidden xl:block w-[300px] glassmorphism p-2 rounded-xl border border-primary/20 shadow-2xl animate-bounce-slow">
    <div class="flex justify-between items-center mb-1 px-2">
        <span class="text-[8px] text-gray-400 uppercase tracking-widest">Sponsored</span>
        <button onclick="this.parentElement.parentElement.remove()" class="text-gray-500 hover:text-white"><i class="fas fa-times text-[10px]"></i></button>
    </div>
    {html_300x250}
</div>
<div class="fixed bottom-4 right-4 z-[9999] hidden xl:block w-[300px] glassmorphism p-2 rounded-xl border border-secondary/20 shadow-2xl animate-bounce-slow" style="animation-delay: 1s;">
    <div class="flex justify-between items-center mb-1 px-2">
        <span class="text-[8px] text-gray-400 uppercase tracking-widest">Sponsored</span>
        <button onclick="this.parentElement.parentElement.remove()" class="text-gray-500 hover:text-white"><i class="fas fa-times text-[10px]"></i></button>
    </div>
    {html_300x250}
</div>
"""

    sticky_bottom = f"""
<!-- Sticky Bottom Ad -->
<div class="fixed bottom-0 left-0 right-0 z-[10000] bg-black/80 backdrop-blur-md border-t border-white/10 py-2 flex justify-center items-center">
    <div class="absolute -top-6 right-4">
        <button onclick="this.parentElement.parentElement.remove()" class="bg-dark border border-white/10 text-white px-3 py-1 rounded-t-lg text-[10px] font-bold uppercase tracking-widest">Close Ad</button>
    </div>
    <div class="max-w-[728px] w-full mx-auto">
        <script>
          atOptions = {{
            'key' : '24d82a14f251de0b584c1c1878965100',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {{}}
          }};
        </script>
        <script src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
    </div>
</div>
"""

    def process_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing Partner Grids to avoid duplication if running multiple times
        content = re.sub(r'<section class="container mx-auto px-4 py-16 border-t border-white/10">[\s\S]*?Aggressive Monetization Grid[\s\S]*?</section>', '', content)
        content = re.sub(r'<section class="container mx-auto px-4 py-16">[\s\S]*?Aggressive Monetization Grid[\s\S]*?</section>', '', content)
        
        # 1. Add Sidebars (Global if missing)
        if '<div class="flex flex-col lg:flex-row justify-between' not in content:
            # We need to find where to insert. After nav is usually good.
            # But play.html has a header.
            insertion_point = '</nav>'
            if '<div class="header" id="header">' in content:
                insertion_point = '</div>' # After the header div
                # But let's be more precise
                content = content.replace('<div id="topSection"', f"""
<div class="flex flex-col lg:flex-row justify-between min-h-screen pt-16 px-0 shrink-0">
    <!-- Left Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
        {html_160x600}
    </div>
    <main class="flex-grow w-full px-2">
        <div id="topSection" """, 1)
                
                content = content.replace('</footer>', f"""</main>
    <!-- Right Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
        {html_160x600}
    </div>
</div>
<footer""", 1)
            else:
                # Standard pages
                content = content.replace('</nav>', f"""</nav>
<div class="flex flex-col lg:flex-row justify-between min-h-screen pt-16 px-0 shrink-0">
    <!-- Left Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
        {html_160x600}
    </div>
    <main class="flex-grow w-full px-2">""", 1)
                
                content = content.replace('<footer', f"""</main>
    <!-- Right Sidebar -->
    <div class="hidden lg:flex flex-shrink-0 w-[180px] flex-col gap-2 items-center py-2 bg-black/10">
        {html_160x600}
        {html_160x600}
        {html_160x600}
    </div>
</div>
<footer""", 1)

        # 2. Add Partner Grid before footer
        content = content.replace('<footer', partner_grid + '<footer')

        # 3. Add Floating Ads and Sticky Bottom before body close
        if 'Floating Ads' not in content:
            content = content.replace('</body>', floating_ads + sticky_bottom + '</body>')

        # 4. Add more internal 728x90 banners in articles
        if 'articles.html' in file_path:
             content = content.replace('</article>', '</article>' + html_728x90)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Processed {file_path} with EXTREME ads")

    files_to_process = [
        'c:\\Users\\abhil\\Desktop\\website\\index.html',
        'c:\\Users\\abhil\\Desktop\\website\\games.html',
        'c:\\Users\\abhil\\Desktop\\website\\play.html',
        'c:\\Users\\abhil\\Desktop\\website\\chatroom.html',
        'c:\\Users\\abhil\\Desktop\\website\\articles.html',
        'c:\\Users\\abhil\\Desktop\\website\\about.html',
        'c:\\Users\\abhil\\Desktop\\website\\policy.html',
        'c:\\Users\\abhil\\Desktop\\website\\feedback.html'
    ]

    for f in files_to_process:
        if os.path.exists(f):
            process_file(f)

if __name__ == "__main__":
    redo_all_ads_extreme()
