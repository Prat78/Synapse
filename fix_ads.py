import re

try:
    with open('games.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Left sidebar expansion
    left_target = '<div class="hidden sm:flex flex-shrink-0 w-[160px] flex-col items-center py-4 bg-black/10 border-r border-white/5 space-y-8">'
    left_ads = '\n'.join(['            <div class="my-4 sp-unit" data-sp-k="81f56b1bdcad21cd55ab223c4f4c2c92" data-sp-w="160" data-sp-h="600"></div>'] * 45)
    
    # Right sidebar expansion
    right_target = '''<div class="hidden sm:flex flex-shrink-0 w-[160px] flex-col overflow-x-hidden gap-8 items-center py-4 bg-black/10 border-l border-white/5 space-y-8">\n            <div class="my-4 sp-unit" data-sp-k="412228ce3f7e514eff0e088bc88dd0a7" data-sp-w="468" data-sp-h="60"></div>\n            <div class="my-4 sp-unit" data-sp-k="4f27449c855a63c1993335475e8b0253" data-sp-w="160" data-sp-h="300"></div>\n            <div class="my-4 sp-unit" data-sp-k="cf6a125c26299b4a476c85e2b484cb3a" data-sp-w="300" data-sp-h="250"></div>'''
    right_ads = '\n'.join(['            <div class="my-4 sp-unit" data-sp-k="81f56b1bdcad21cd55ab223c4f4c2c92" data-sp-w="160" data-sp-h="600"></div>'] * 45)

    if '<!-- Left Sidebar: Ad 2' in content:
        content = re.sub(
            r'<div class="hidden sm:flex flex-shrink-0 w-\[160px\] flex-col items-center py-4 bg-black/10 border-r border-white/5 space-y-8">.*?(?=</div>\s*<main)',
            left_target + '\n' + left_ads + '\n        ',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'<div class="hidden sm:flex flex-shrink-0 w-\[160px\] flex-col overflow-x-hidden gap-8 items-center py-4 bg-black/10 border-l border-white/5 space-y-8">.*?(?=</div>\s*</div>\s*<footer)',
            right_target + '\n' + right_ads + '\n        ',
            content,
            flags=re.DOTALL
        )

        with open('games.html', 'w', encoding='utf-8') as file:
            file.write(content)
        print('games.html sidebars extended successfully')
except Exception as e:
    print('Error applying extended sidebars:', e)
