"""
gentle_trim.py
Remove only duplicate/stacked ad blocks that look broken visually,
while keeping all unique ad placements that are generating impressions.
"""
import re

AD_KEYS = {
    '24d82a14f251de0b584c1c1878965100',  # 728x90
    'cf6a125c26299b4a476c85e2b484cb3a',  # 300x250
    '81f56b1bdcad21cd55ab223c4f4c2c92',  # 160x600
}

def dedup_ads(html):
    """Keep each unique ad key appearing at most twice per page."""
    for key in AD_KEYS:
        # Find all occurrences of this key
        pattern = re.compile(
            r'(<(?:div|script)[^>]*>\s*<script[^>]*>' + 
            r'atOptions\s*=\s*\{[^\}]*' + re.escape(key) + r'[^\}]*\}[\s\S]*?' +
            r'</script>\s*<script[^>]*/invoke\.js[^>]*></script>\s*</div>)',
            re.IGNORECASE)
        
        matches = list(pattern.finditer(html))
        # If more than 2 of the same key, remove extras beyond 2
        if len(matches) > 2:
            # Remove the extras (keep first 2, delete rest)
            for m in reversed(matches[2:]):
                html = html[:m.start()] + html[m.end():]
    return html

def remove_empty_ad_wrappers(html):
    """Remove leftover empty flex divs that held ads."""
    html = re.sub(r'<div class="[^"]*flex justify-center[^"]*my-\d[^"]*">\s*</div>', '', html)
    html = re.sub(r'<div class="[^"]*flex justify-center[^"]*">\s*</div>', '', html)
    html = re.sub(r'(\n\s*){3,}', '\n\n', html)
    return html

files = ['chatroom.html', 'games.html', 'play.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    before = content.count('atOptions')
    content = dedup_ads(content)
    content = remove_empty_ad_wrappers(content)
    after = content.count('atOptions')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'{fname}: {before} → {after} ad instances')

print('\nDone. Duplicates removed, unique placements kept.')
