import re

html_728x90 = """
<div class="flex justify-center my-4 w-full">
<script>
  atOptions = {
    'key' : '24d82a14f251de0b584c1c1878965100',
    'format' : 'iframe',
    'height' : 90,
    'width' : 728,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/24d82a14f251de0b584c1c1878965100/invoke.js"></script>
</div>
"""

html_160x600 = """
<div class="flex justify-center my-4 w-full">
<script>
  atOptions = {
    'key' : '81f56b1bdcad21cd55ab223c4f4c2c92',
    'format' : 'iframe',
    'height' : 600,
    'width' : 160,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/81f56b1bdcad21cd55ab223c4f4c2c92/invoke.js"></script>
</div>
"""

html_300x250 = """
<div class="flex justify-center my-4 w-full">
<script>
  atOptions = {
    'key' : 'cf6a125c26299b4a476c85e2b484cb3a',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://www.highperformanceformat.com/cf6a125c26299b4a476c85e2b484cb3a/invoke.js"></script>
</div>
"""

native_banner = """
<div class="flex justify-center my-4 w-full">
<script async="async" data-cfasync="false" src="https://pl28788345.effectivegatecpm.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
<div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
</div>
"""

row_mixed = f"""
<div class="flex flex-col md:flex-row gap-8 justify-center items-center my-8 w-full max-w-full overflow-hidden">
    {html_300x250}
    <div class="hidden lg:block">{html_728x90}</div>
</div>
"""

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'r', encoding='utf-8') as f:
    chat = f.read()

# Clean up empty divs
# the empty grid: <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">\n                    <div class="flex justify-center">\n                        \n                    </div>\n ...
chat = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">[\s\S]*?</div>(\s*</div>)?\s*<div class="flex justify-center my-8">\s*<div>\s*</div>\s*</div>', '', chat)
# Also just a general wipe of it
chat = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 my-12 px-4">\s*(<div class="flex justify-center">\s*</div>\s*){0,6}</div>', '', chat)
# also remove remaining wrapper bits
chat = re.sub(r'<div class="flex justify-center my-8">\s*<div>\s*</div>\s*</div>', '', chat)

chat = re.sub(r'</main>\s*<footer', f'</main>\n    <div class="container mx-auto px-4">\n        {row_mixed}\n        {native_banner}\n    </div>\n    <footer', chat)

with open('c:\\Users\\abhil\\Desktop\\website\\chatroom.html', 'w', encoding='utf-8') as f:
    f.write(chat)
