import re

def wipe_banners(content):
    # Remove all High Performance Format standard blocks
    content = re.sub(r'<div class="flex justify-center[\s\S]*?">\s*<script>[\s\S]*?invoke\.js"></script>\s*</div>', '', content)
    # Remove Native
    content = re.sub(r'<div class="flex justify-center[\s\S]*?">\s*<script async="async".*?invoke\.js"></script>\s*<div id="container-cb54d.*?></div>\s*</div>', '', content)
    # Remove the bottom ad grid I tried to add in play.html
    content = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-8 my-12 items-center justify-items-center">[\s\S]*?</div>', '', content)
    
    return content

html_728x90 = """
<div class="flex justify-center my-4 w-full" style="clear: both;">
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
<div class="flex justify-center my-4 w-full hidden md:flex" style="clear: both;">
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
<div class="flex justify-center my-4 w-full" style="clear: both;">
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
<div class="flex justify-center my-4 w-full" style="clear: both;">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

# ======================= PLAY.HTML ========================
with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = wipe_banners(play)

# AD 1: Top 728 right above Top Tools (After the gap-8 flex col start)
play = play.replace('<div class="flex flex-col gap-8 justify-center">\n\n            \n\n\n\n\n\n', 
                    f'<div class="flex flex-col gap-8 justify-center">\n\n{html_728x90}\n')

# AD 2: 300x250 right above the game title/description info box inside the Right column
# Let's target the info icon
target_right_col = '<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">'
play = play.replace(target_right_col, f'{target_right_col}\n{html_300x250}')

# AD 3: 160x600 in the Left column of the Top Tools section
target_left_col = '<div class="lg:col-span-12 xl:col-span-12">'
play = play.replace(target_left_col, f'{target_left_col}\n{html_728x90}')

# AD 4: Native banner just above the game container entirely
# The game container is inside the flex flex-col gap-8 justify-center block.
play = play.replace('<!-- Full Width Game Container (No max-w constraint) -->', f'{native_banner}\n<!-- Full Width Game Container (No max-w constraint) -->')

# AD 5 & 6: After the end of the very last component before footer
play = play.replace('</footer>', f'{html_300x250}\n{html_160x600}\n</footer>')

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)

# ======================= CHATROOM.HTML ========================
with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = wipe_banners(chat)

# AD 1: 728x90 above the room selector
target_chat_1 = '<div class="text-center mb-8">'
chat = chat.replace(target_chat_1, f'{html_728x90}\n{target_chat_1}')

# AD 2: 300x250 inside the main chat area right above the discord banner
target_chat_2 = '<!-- Discord Invitation Banner -->'
chat = chat.replace(target_chat_2, f'{html_300x250}\n{target_chat_2}')

# AD 3: 300x250 right below User Profile in sidebar
target_chat_3 = '<div class="space-y-3">\n                                <div class="flex items-center space-x-3">'
chat = chat.replace(target_chat_3, f'{html_300x250}\n{target_chat_3}')

# AD 4: 300x250 right under Chat Rules
target_chat_4 = '</ul>\n                        </div>'
# Instead of replacing all </ul>, be specific
chat = chat.replace('<li>❌ No spam flooding</li>\n                            </ul>\n                        </div>', 
                    f'<li>❌ No spam flooding</li>\n                            </ul>\n                        </div>\n{html_300x250}')


# AD 5 & AD 6 + Native: Put at the very bottom right before footer, cleanly outside the flex grid
chat = chat.replace('<footer class="mt-16', f'{html_728x90}\n{html_300x250}\n{native_banner}\n<footer class="mt-16')

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("Ads wiped and redone cleanly!")
