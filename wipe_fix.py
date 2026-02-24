import re

def wipe(content):
    # Remove all High Performance Format standard blocks
    content = re.sub(r'<div class="flex[a-zA-Z0-9\s:;\'"-]*?">\s*<script>[\s\S]*?invoke\.js"></script>\s*</div>', '', content)
    # Remove Native
    content = re.sub(r'<div class="flex[a-zA-Z0-9\s:;\'"-]*?">\s*<script async="async".*?invoke\.js"></script>\s*<div id="container-cb54d.*?></div>\s*</div>', '', content)
    # Remove remnants in chatroom grid
    grid_re = r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">[\s\S]*?</div>(\s*</div>\s*</div>\s*<div class="flex justify-center my-8">)?'
    content = re.sub(grid_re, '', content)
    # Just to be safe, any lingering empty flex justify-center wraps
    content = re.sub(r'<div class="flex justify-center my-8">\s*(<div>\s*</div>|)?\s*</div>', '', content)
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


# PLAY HTML
with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = wipe(play)

# Ensure no ads are inside <footer ...> 
for _ in range(3): # repeat just in case
    play = re.sub(r'(<footer[^>]*>)[\s\S]*?(<div[^>]*>[\s\S]*?</div>\s*)*(</footer>)?', r'\1\n        <div class="container mx-auto...\n        </footer>', play)

# Restoring footer properly
play = re.sub(r'<footer[^>]*>[\s\S]*?</footer>', """<footer
            style="margin-top: 50px; padding: 20px; text-align: center; color: #4b5563; font-size: 12px; background: #0f172a;">
            <div style="margin-bottom: 10px;">
                <a href="index.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">Home</a>
                <a href="chat.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">AI Chat</a>
                <a href="games.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">Games</a>
                <a href="proxy.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">Online Games</a>
                <a href="feedback.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">Feedback</a>
                <a href="policy.html" style="color: #60a5fa; margin: 0 10px; text-decoration: none;">Policy</a>
            </div>
            <p>&copy; 2024 Synapse AI - Best Unblocked Games Platform</p>
        </footer>""", play)
        

# Inject completely safe
play = play.replace('<div id="topSection" class="pt-20 container mx-auto px-4 max-w-[2000px]">',
                    f'<div id="topSection" class="pt-20 container mx-auto px-4 max-w-[2000px]">\n{html_728x90}\n')

play = play.replace('<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->',
                    f'{html_300x250}\n<!-- TOP TOOLS SECTION (AI CHAT & INFO) -->')

play = play.replace('<!-- Full Width Game Container (No max-w constraint) -->',
                    f'{html_728x90}\n{native_banner}\n<!-- Full Width Game Container (No max-w constraint) -->')

# Right before footer
play = play.replace('<footer', f'{html_300x250}\n{html_160x600}\n<footer')

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)



# CHATROOM HTML
with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = wipe(chat)

# Restore footer cleanly
chat = re.sub(r'<footer[^>]*>[\s\S]*?</footer>', """<footer class="mt-16 border-t border-white/10 bg-black/40 backdrop-blur-md">
        <div class="container mx-auto px-4 py-12">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 text-center md:text-left mb-8">
                <div>
                    <h4 class="text-white font-orbitron font-bold mb-4">Synapse AI</h4>
                    <p class="text-gray-500 text-sm">The leading edge of unblocked gaming and AI assistance.</p>
                </div>
                <div>
                    <h4 class="text-white font-orbitron font-bold mb-4">Quick Links</h4>
                    <ul class="text-gray-500 text-sm space-y-2">
                        <li><a href="index.html" class="hover:text-primary transition-colors">Home</a></li>
                        <li><a href="games.html" class="hover:text-primary transition-colors">Games List</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="text-white font-orbitron font-bold mb-4">Support</h4>
                    <ul class="text-gray-500 text-sm space-y-2">
                        <li><a href="articles.html" class="hover:text-primary transition-colors">Articles</a></li>
                        <li><a href="feedback.html" class="hover:text-primary transition-colors">Feedback</a></li>
                    </ul>
                </div>
            </div>
            <div class="pt-8 border-t border-white/5 text-center">
                <p class="text-gray-500 text-xs">© 2026 Synapse AI.</p>
            </div>
        </div>
    </footer>""", chat)
    
chat = chat.replace('<main class="pt-20">', f'{html_728x90}\n<main class="pt-20">')
chat = chat.replace('<!-- Discord Invitation Banner -->', f'{html_300x250}\n<!-- Discord Invitation Banner -->')

chat = chat.replace('</div>\n                        </div>\n                    </div>\n                </div>\n',
                    f'</div>\n                        </div>\n                    </div>\n                </div>\n{html_728x90}\n{html_300x250}\n')

chat = chat.replace('<footer', f'{native_banner}\n<footer')

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("All wiped and fixed safely.")
