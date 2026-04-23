import os, glob
for ext in ['*.html']:
    for f in glob.glob(ext):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        content = content.replace('"./assets/js/main.js"', '"./assets/js/main.js?v=tg2"')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
