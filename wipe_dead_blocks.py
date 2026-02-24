import re

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

# Aggressive clean up of empty grid blocks in chatroom.html
chat = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">\n(\s*<div class="flex justify-center">\s*</div>\n)*\s*</div>', '', chat)
chat = re.sub(r'<div class="flex justify-center my-8">\s*<div>\s*</div>\s*</div>', '', chat)

# Clean excessive newlines to physically shrink doc
chat = re.sub(r'(\n\s*){3,}', '\n\n', chat)

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)

print("Targeted dead layout blocks removed.")
