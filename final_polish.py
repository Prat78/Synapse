import os
import re

def final_polish():
    # 1. Clean script.js - remove the entire pop-under section
    if os.path.exists('script.js'):
        with open('script.js', 'r', encoding='utf-8') as f:
            js_content = f.read()
        
        # Remove the code from canFire up to the firePopUnder function call
        # We search for the function firePopUnder and we'll just empty it.
        js_content = re.sub(r'function firePopUnder\(\)\s*\{.*?\}\n\n', 'function firePopUnder() {}\n\n', js_content, flags=re.DOTALL)
        
        with open('script.js', 'w', encoding='utf-8') as f:
            f.write(js_content)
        print("Cleaned script.js")

    # 2. Clean HTML files - remove empty script blocks or variables left behind
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove leftover "directLink" definitions and empty listeners
        content = re.sub(r'\s*const\s+directLink\s*=\s*"\s*";', '', content)
        content = re.sub(r'\s*window\.open\(directLink,\s*\'_blank\'\);', '', content)
        
        # Remove script blocks that are now essentially empty
        content = re.sub(r'<script>\s*\(function\s*\(\)\s*\{\s*\}\)\(\);\s*</script>', '', content)
        
        # Remove the specific empty loop/if in index.html line 129
        content = content.replace('if (NOW - LAST_POP > FIVE_MIN) {\n                        ;\n                        localStorage.setItem(\'synapse_last_pop\', NOW);\n                    }', '')

        # Remove double comment lines or single tags that were cut off
        content = re.sub(r'<!--\s*-->', '', content)
        content = re.sub(r' +', ' ', content) # Clean double spaces
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Polished {file}")

if __name__ == "__main__":
    final_polish()
    # Cleanup temp scripts
    for tmp in ['safe_clean.py', 'final_purge.py', 'safe_clean.py']:
        if os.path.exists(tmp):
            os.remove(tmp)
