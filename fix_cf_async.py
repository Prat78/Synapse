import os
import re

def add_cf_async(html_content):
    # Regex to find script tags for ads that don't have data-cfasync="false"
    # We target effectivegatecpm.com and highperformanceformat.com and invoke.js
    
    # Pattern to match <script ... src="...ad-url..." ...></script>
    # We want to insert data-cfasync="false" if it's missing.
    
    ad_domains = [
        'effectivegatecpm.com',
        'highperformanceformat.com',
        'invoke.js'
    ]
    
    # Find all script tags with src
    script_src_pattern = re.compile(r'(<script[^>]*src=["\'][^"\']*(?:' + '|'.join(ad_domains) + r')[^"\']*["\'][^>]*>)')
    
    def replacement(match):
        tag = match.group(1)
        if 'data-cfasync="false"' in tag:
            return tag
        # Insert it after '<script'
        return tag.replace('<script', '<script data-cfasync="false"')
    
    new_content = script_src_pattern.sub(replacement, html_content)
    
    return new_content

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content = add_cf_async(content)
        
        if content != updated_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {file}")
        else:
            print(f"No changes needed for {file}")
