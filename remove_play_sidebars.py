import re

file_path = r"c:\Users\abhil\Desktop\website\play.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace LEFT SIDEBAR block
# Find everything from "<!-- LEFT SIDEBAR: Multiple Long Ads -->" to its closing div (the one right before <!-- CENTRE: main content -->)
new_content = re.sub(
    r'(<!-- LEFT SIDEBAR: Multiple Long Ads -->[\s\S]*?)(?=<!-- CENTRE: main content -->)',
    '',
    content
)

# Replace RIGHT SIDEBAR block
# Find everything from "<!-- RIGHT SIDEBAR: Multiple Long Ads -->" up to "<!-- end six-ad outer flex -->" or "</body>"
new_content = re.sub(
    r'<!-- RIGHT SIDEBAR: Multiple Long Ads -->[\s\S]*?(?=</div><!-- end six-ad outer flex -->|</body>)',
    '',
    new_content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Sidebars removed successfully")
