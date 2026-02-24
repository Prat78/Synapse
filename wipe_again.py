import re

def wipe(content):
    # Match any <div class="flex justify-center... w-full"> that contains "highperformanceformat" or "effectivegatecpm"
    # To be extremely safe and broad, we find the index of invoke.js and remove its parent div.
    
    # Approach 1: Regex
    # A div that has 'flex justify-center'. Inside it we see invoke.js.
    # We can match '<div class="flex justify-center my-4 w-full">\n<script>\n  atOptions' and just wipe it.
    out = content
    # Remove atOptions format
    out = re.sub(r'<div class="flex[^>]*?>\s*<script>\s*atOptions[\s\S]*?invoke\.js"></script>\s*</div>', '', out)
    # Remove async format
    out = re.sub(r'<div class="flex[^>]*?>\s*<script async="async"[\s\S]*?invoke\.js"></script>\s*<div[^>]*?></div>\s*</div>', '', out)
    
    # Let's handle the grid grids
    out = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">[\s\S]*?</div>(\s*</div>\s*</div>\s*<div class="flex justify-center my-8">)?', '', out)
    
    # also remove any lingering row_mixed
    out = re.sub(r'<div class="flex flex-col md:flex-row gap-8 justify-center items-center my-8 w-full max-w-full overflow-hidden">[\s\S]*?(<div class="hidden lg:block">[\s\S]*?</div>\s*</div>)', '', out)

    return out

with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'r', encoding='utf-8') as f:
    play = f.read()

play = wipe(play)
with open('c:\\Users\\abhil\\Desktop\\website\\play.html', 'w', encoding='utf-8') as f:
    f.write(play)

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

chat = wipe(chat)
with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("Wiped using better regex!")
