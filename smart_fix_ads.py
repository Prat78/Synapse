import re

def wipe(content):
    # Remove all formatting blocks and native blocks
    content = re.sub(r'<div class="flex[^>]*?>\s*<script[^>]*?>[\s\S]*?invoke\.js"></script>\s*(<div[^>]*?></div>)?\s*</div>', '', content)
    # Remove lingering ad grids in chatroom
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">[\s\S]*?</div>(\s*<div class="flex justify-center my-8">\s*<div>\s*</div>\s*</div>)?', '', content)
    # Remove the empty script block found at bottom of chatroom that had no div
    content = re.sub(r'<script>\s*atOptions = \{[\s\S]*?invoke\.js"></script>', '', content)
    return content

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

# ==================== PLAY.HTML =======================
with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = wipe(play)

# Clean up empty spaces that might have been left
play = re.sub(r'(\s*\n){3,}', '\n\n', play) # remove excessive newlines

play = play.replace(
    '<div class="flex flex-col gap-8 justify-center">\n\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->',
    f'{html_728x90}\n<div class="flex flex-col gap-8 justify-center">\n\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->'
)

play = play.replace(
    '<!-- Full Width Game Container (No max-w constraint) -->',
    f'{row_mixed}\n<!-- Full Width Game Container (No max-w constraint) -->'
)

play = play.replace(
    '</div>\n        </div>\n\n        <footer',
    f'</div>\n        </div>\n{html_728x90}\n{native_banner}\n{html_300x250}\n        <footer'
)

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)

# ==================== CHATROOM.HTML =======================
with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = wipe(chat)

# Remove excessive newlines
chat = re.sub(r'(\s*\n){3,}', '\n\n', chat)

chat = chat.replace(
    '<div class="text-center mb-8">',
    f'{html_728x90}\n<div class="text-center mb-8">'
)

chat = chat.replace(
    '<div class="grid grid-cols-1 lg:grid-cols-4 gap-6">',
    f'{html_728x90}\n<div class="grid grid-cols-1 lg:grid-cols-4 gap-6">'
)

# Put a 160x600 in the sidebar after "Stats"
target_sidebar_end = 'id="totalMessageCount">0</span></div>\n                            </div>\n                        </div>'
chat = chat.replace(
    target_sidebar_end,
    f'{target_sidebar_end}\n                        <div class="hidden lg:block">\n                            {html_160x600}\n                        </div>\n                        <div class="lg:hidden">\n                            {html_300x250}\n                        </div>'
)

# Put bottom ads cleanly before footer, where the grid was
chat = chat.replace(
    '</main>\n    <footer',
    f'</main>\n    <div class="container mx-auto px-4">\n        {row_mixed}\n        {native_banner}\n    </div>\n    <footer'
)

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("Ads injected smartly into outer spaces only.")
