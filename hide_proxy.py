import os, glob, re

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Comment out all <a href="proxy.html"> tags
    content = re.sub(r'(<a[^>]+href=\"proxy\.html\"[^>]*>.*?</a>)', r'<!-- \1 -->', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Proxy links hidden in all HTML files.')
