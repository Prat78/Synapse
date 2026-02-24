import os
import re

WORKING_BANNER = "\/\/rapid-university.com\/b.XBVBs_d\/G\/lI0KY\/WtcT\/zemmE9euGZ\/U-lmkqPpTSYS4OMLjtEX3\/NwDWUmt\/NVjSgTyBM\/T\/c\/0XOnQg"

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    skip_mode = False
    
    for line in lines:
        # Catch the psffcg block (index.html, play.html, etc.)
        if '(function (psffcg)' in line or '(function(psffcg)' in line:
            skip_mode = True
            continue
        # Catch the direct link force pop
        if 'const directLink = "https://quickwittedconclusion.com' in line:
            continue
        if "window.open(directLink, '_blank');" in line:
            continue
        # Catch the direct pop-under handler
        if '(function(amz)' in line or '(function (amz)' in line:
            skip_mode = True
            continue
        # Catch the background pop-under injection
        if '(function (mnalua)' in line or '(function(mnalua)' in line:
            if 'quickwittedconclusion.com' in line or (len(new_lines) > 0 and 'quickwittedconclusion.com' in "".join(lines[lines.index(line):lines.index(line)+5])):
                 skip_mode = True
                 continue
        
        # Replace the msfr banner blocks
        if 'quickwittedconclusion.com' in line and '(function (msfr)' in line:
            # Replace the entire line with the working banner logic
            new_lines.append(f' <script>(function (vre) {{ var d = document, s = d.createElement(\'script\'), l = d.scripts[d.scripts.length - 1]; s.settings = vre || {{}}; s.src = "{WORKING_BANNER}"; s.async = true; s.referrerPolicy = \'no-referrer-when-downgrade\'; l.parentNode.insertBefore(s, l); }})({{}})</script>\n')
            continue
        
        if skip_mode:
            if '})({})' in line:
                skip_mode = False
            continue
            
        # Extra check for any line containing just the bad domain URL
        if 'quickwittedconclusion.com' in line and 's.src' in line:
            continue

        new_lines.append(line)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
for f in html_files:
    clean_file(f)

if os.path.exists('script.js'):
    clean_file('script.js')

print("Cleanup complete.")
