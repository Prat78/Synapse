import glob

html_files = glob.glob('*.html')
banner_html = '''
    <div style="text-align: center; margin: 20px auto;">
        <script async="async" data-cfasync="false" src="https://whistlemiddletrains.com/cb54d1e3a7a7a676c81b222b316e2f9d/invoke.js"></script>
        <div id="container-cb54d1e3a7a7a676c81b222b316e2f9d"></div>
    </div>
'''

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'container-cb54d1e3a7a7a676c81b222b316e2f9d' not in content:
            if '<footer' in content:
                content = content.replace('<footer', banner_html + '\n    <footer')
            else:
                content = content.replace('</body>', banner_html + '\n</body>')
                
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print('Added native banner to ' + f)
    except Exception as e:
        print('Error processing ' + f + ': ' + str(e))

