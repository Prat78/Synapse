
import os, re, glob
for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the parent flex container from md:flex-row to sm:flex-row
    content = re.sub(r'flex flex-col md:flex-row justify-between min-h-screen', 'flex flex-col sm:flex-row justify-between min-h-screen', content)
    
    # 2. Update the left and right sidebars from hidden md:flex to hidden sm:flex
    content = re.sub(r'hidden md:flex flex-shrink-0 w-\[180px\]', 'hidden sm:flex flex-shrink-0 w-[160px]', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Updated breakpoints for Chromebooks.')

