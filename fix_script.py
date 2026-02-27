import glob

html_files = glob.glob('*.html')
script_tag = '<script src=\"https://whistlemiddletrains.com/6d/a5/11/6da511cea846b2c71c4de947ddb4dc61.js\"></script>'

for f in html_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if script_tag not in content:
            content = content.replace('</body>', '    ' + script_tag + '\n</body>')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print('Added tag to ' + f)
    except Exception as e:
        print('Error processing ' + f + ': ' + str(e))

