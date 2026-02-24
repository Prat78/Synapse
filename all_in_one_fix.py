import re

html_728x90 = """
<div class="flex justify-center my-4 w-full">
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
<div class="flex justify-center my-4 w-full">
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
<div class="flex justify-center my-4 w-full">
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
<div class="flex justify-center my-4 w-full">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

row_mixed = f"""
<div class="flex flex-col md:flex-row gap-8 justify-center items-center my-8 w-full max-w-full overflow-hidden">
    {html_300x250}
    <div class="hidden lg:block">{html_728x90}</div>
</div>
"""

def replace_ads_in_play(content):
    # Wipe logic
    content = re.sub(r'<div class="flex[^>]*?>\s*<script>\s*atOptions[\s\S]*?invoke\.js"></script>\s*</div>', '', content)
    content = re.sub(r'<div class="flex[^>]*?>\s*<script async="async"[\s\S]*?invoke\.js"></script>\s*<div[^>]*?></div>\s*</div>', '', content)
    content = re.sub(r'(\s*\n){3,}', '\n\n', content)
    
    # Safe inserts
    content = content.replace(
        '<div class="flex flex-col gap-8 justify-center">\n\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->',
        f'{html_728x90}\n<div class="flex flex-col gap-8 justify-center">\n\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->'
    )

    content = content.replace(
        '<!-- Full Width Game Container (No max-w constraint) -->',
        f'{row_mixed}\n<!-- Full Width Game Container (No max-w constraint) -->'
    )

    content = content.replace(
        '</div>\n        </div>\n\n        <footer',
        f'</div>\n        </div>\n{html_728x90}\n{native_banner}\n{html_300x250}\n        <footer'
    )
    return content

def replace_ads_in_chat(content):
    # Wipe logic
    content = re.sub(r'<div class="flex[^>]*?>\s*<script>\s*atOptions[\s\S]*?invoke\.js"></script>\s*</div>', '', content)
    content = re.sub(r'<div class="flex[^>]*?>\s*<script async="async"[\s\S]*?invoke\.js"></script>\s*<div[^>]*?></div>\s*</div>', '', content)
    # The grid wipe
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">[\s\S]*?</div>(\s*</div>\s*</div>\s*<div class="flex justify-center my-8">)?', '', content)
    content = re.sub(r'<script>\s*atOptions = \{[\s\S]*?invoke\.js"></script>', '', content)
    content = re.sub(r'(\s*\n){3,}', '\n\n', content)

    content = content.replace(
        '<div class="text-center mb-8">',
        f'{html_728x90}\n<div class="text-center mb-8">'
    )

    content = content.replace(
        '<div class="grid grid-cols-1 lg:grid-cols-4 gap-6">',
        f'{html_728x90}\n<div class="grid grid-cols-1 lg:grid-cols-4 gap-6">'
    )

    # Sidebar ad placement
    target_sidebar_end = 'id="totalMessageCount">0</span></div>\n                            </div>\n                        </div>'
    content = content.replace(
        target_sidebar_end,
        f'{target_sidebar_end}\n                        <div class="hidden lg:block">\n                            {html_160x600}\n                        </div>\n                        <div class="lg:hidden">\n                            {html_300x250}\n                        </div>'
    )

    content = content.replace(
        '</main>\n    <footer',
        f'</main>\n    <div class="container mx-auto px-4">\n        {row_mixed}\n        {native_banner}\n    </div>\n    <footer'
    )
    return content

import sys
if __name__ == '__main__':
    import os
    os.system("git checkout -- play.html chatroom.html")
    
    with open('play.html', 'r', encoding='utf-8') as f:
        play = f.read()
    with open('play.html', 'w', encoding='utf-8') as f:
        f.write(replace_ads_in_play(play))
        
    with open('chatroom.html', 'r', encoding='utf-8') as f:
        chat = f.read()
    with open('chatroom.html', 'w', encoding='utf-8') as f:
        f.write(replace_ads_in_chat(chat))
    
    print("Clean checkout and replaced safely!")
