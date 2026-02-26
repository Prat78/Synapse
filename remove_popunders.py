
import os, re
import glob

# Remove pop-unders from HTML
html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove script tags for pop unders
    content = re.sub(r'<script[^>]*src=.*?effectivegatecpm\.com.*?</script>\s*', '', content)
    content = re.sub(r'<script[^>]*src=.*?whistlemiddletrains\.com.*?</script>\s*', '', content)
    
    # Remove the rate limiter block
    content = re.sub(r'<!-- Direct Pop-Under Handler.*?</script>\s*', '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Remove pop-unders from script.js
with open('script.js', 'r', encoding='utf-8') as file:
    js_content = file.read()

# The pop-under logic at the bottom of script.js
js_content = re.sub(r'// ===========================\s*// Pop-Under Ads.*?\}\)\(\);\s*', '', js_content, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as file:
    file.write(js_content)
print('Pop-unders removed successfully.')

