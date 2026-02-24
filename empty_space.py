import re

html_728x90 = """
<div class="flex justify-center my-4 w-full" style="max-height:90px; overflow:hidden;">
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

def clean(s):
    # Rip out every flex div containing highperformanceformat and effectivegatecpm
    s = re.sub(r'<div class="flex[^>]*?>\s*<script>\s*atOptions[\s\S]*?invoke\.js"></script>\s*</div>', '', s)
    s = re.sub(r'<div class="flex[^>]*?>\s*<script async="async"[\s\S]*?invoke\.js"></script>\s*<div[^>]*?></div>\s*</div>', '', s)
    s = re.sub(r'<div class="flex flex-col md:flex-row gap-8 justify-center items-center my-8 w-full max-w-full overflow-hidden">[\s\S]*?(<div class="hidden lg:block">[\s\S]*?</div>)?\s*</div>', '', s)
    s = re.sub(r'<div class="hidden lg:block">\s*</div>', '', s)
    s = re.sub(r'<div class="lg:hidden">\s*</div>', '', s)
    # clean stranded empty layouts
    s = re.sub(r'<div class="lg:col-span-12 xl:col-span-12">\s*</div>', '', s)
    s = re.sub(r'<div class="flex justify-center my-4 w-[^>]*?>\s*</div>', '', s)
    # cleanup extra whitespace blocks
    s = re.sub(r'(\n\s*){3,}', '\n\n', s)
    return s


with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = clean(play)

# For play.html: Fit the 300x250 INSIDE the "gameInfo" div below the description!
target_p = r'(<p class="text-gray-400 leading-relaxed text-sm mb-8" id="gameDescription">[\s\S]*?</p>\s*</div>)'
play = re.sub(target_p, rf'\1\n{html_300x250}', play)

# Fit the native banner explicitly before footer so it doesnt bloat layout
play = play.replace('<footer', f'{native_banner}\n<footer')


with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)

# ==============
with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = clean(chat)

# Fit the 300x250 nicely into the sidebar after the Chat Rules and Stats block without bloating
chat_target = r'(id="totalMessageCount">0</span></div>\s*</div>\s*</div>)'
chat = re.sub(chat_target, rf'\1\n<div class="mt-6 flex justify-center">{html_300x250}</div>', chat)

# Add a neat 728x90 tightly into the chat header (which is very thin)
chat_target2 = r'(<h1 class="text-3xl md:text-4xl font-orbitron font-bold mb-4">[\s\S]*?</p>\s*</div>)'
chat = re.sub(chat_target2, rf'<div class="flex flex-col md:flex-row items-center justify-between">\n<div class="md:w-1/2 text-left">\n\1\n</div><div class="md:w-1/2 text-right">\n{html_728x90}\n</div>\n</div>', chat)
# Note: actually it might be better to just put the 728 cleanly next to title. Let's just use Native banner before footer.
chat = chat.replace('<footer', f'{native_banner}\n<footer')

# Clean any artifacts
chat = chat.replace('<div class="flex flex-col md:flex-row items-center justify-between">\n<div class="md:w-1/2 text-left">\n<div class="text-center mb-8">', '<div class="flex flex-col md:flex-row items-center justify-between mb-8">\n<div class="md:w-1/2 text-left">')
chat = chat.replace('</p>\n                </div>\n</div><div class="md:w-1/2 text-right">', '</p></div><div class="md:w-1/2 text-right">')

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("Placed ads into real empty space WITHOUT lengthening the pages.")
