import os
import glob

html_files = glob.glob('*.html')
script_tag = '<script src="https://whistlemiddletrains.com/6d/a5/11/6da511cea846b2c71c4de947ddb4dc61.js"></script>'

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if script_tag not in content:
        content = content.replace('</body>', f'    {script_tag}\n</body>')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

# Fix games.html sidebars to have 40 units each
with open('games.html', 'r', encoding='utf-8') as file:
    lines = file.readlines()

new_lines = []
skip = False
for line in lines:
    if '<!-- Left Sidebar:' in line:
        new_lines.append(line)
        new_lines.append('        <div class="hidden sm:flex flex-shrink-0 w-[160px] flex-col items-center py-4 bg-black/10 border-r border-white/5 space-y-8">\n')
        for _ in range(40):
            new_lines.append('            <div class="my-4 sp-unit" data-sp-k="81f56b1bdcad21cd55ab223c4f4c2c92" data-sp-w="160" data-sp-h="600"></div>\n')
        new_lines.append('        </div>\n')
        skip = True
        continue
    if '<!-- Right Sidebar -->' in line:
        new_lines.append(line)
        new_lines.append('        <div class="hidden sm:flex flex-shrink-0 w-[160px] flex-col overflow-x-hidden gap-8 items-center py-4 bg-black/10 border-l border-white/5 space-y-8">\n')
        new_lines.append('            <div class="my-4 sp-unit" data-sp-k="412228ce3f7e514eff0e088bc88dd0a7" data-sp-w="468" data-sp-h="60"></div>\n')
        new_lines.append('            <div class="my-4 sp-unit" data-sp-k="4f27449c855a63c1993335475e8b0253" data-sp-w="160" data-sp-h="300"></div>\n')
        new_lines.append('            <div class="my-4 sp-unit" data-sp-k="cf6a125c26299b4a476c85e2b484cb3a" data-sp-w="300" data-sp-h="250"></div>\n')
        for _ in range(37):
            new_lines.append('            <div class="my-4 sp-unit" data-sp-k="81f56b1bdcad21cd55ab223c4f4c2c92" data-sp-w="160" data-sp-h="600"></div>\n')
        new_lines.append('        </div>\n')
        skip = True
        continue
        
    if skip:
        if '</div>' in line and (('</main>' in lines[lines.index(line)+1] if lines.index(line)+1 < len(lines) else False) or ('</div>' in lines[lines.index(line)+1] if lines.index(line)+1 < len(lines) else False) or ('<footer' in lines[lines.index(line)+2] if lines.index(line)+2 < len(lines) else False)):
            skip = False
        continue
        
    new_lines.append(line)

with open('test.py', 'w') as f:
    pass
