import glob

html_files = glob.glob('*.html')
sticky_ad = '''
    <!-- Sticky Bottom Ad -->
    <div id="stickyAdBanner" style="position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; background: rgba(0,0,0,0.9); text-align: center; padding: 10px 0; border-top: 2px solid #3b82f6; display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <button onclick="document.getElementById('stickyAdBanner').style.display='none'" style="position: absolute; top: -25px; right: 20px; background: #ef4444; color: white; border: none; padding: 4px 12px; border-radius: 6px 6px 0 0; cursor: pointer; font-family: 'Orbitron', sans-serif; font-size: 10px; font-weight: bold; letter-spacing: 1px;">CLOSE AD</button>
        <div class="hidden md:flex justify-center sp-unit" data-sp-k="24d82a14f251de0b584c1c1878965100" data-sp-w="728" data-sp-h="90"></div>
        <div class="flex md:hidden justify-center sp-unit" data-sp-k="3b778bf9b4ac85cd02fc7e17f000d8d5" data-sp-w="320" data-sp-h="50"></div>
    </div>
'''

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'id="stickyAdBanner"' not in content:
            content = content.replace('</body>', sticky_ad + '\n</body>')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Added sticky ad to {f}')
    except Exception as e:
        print(f'Error processing {f}: {e}')
