import os, glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('>info@eurostatus.com</a></li>', '>eurostatus@ro.ru</a> <span style="font-size: 0.85em; opacity: 0.8;">(Для документов)</span></li>')
    new_content = new_content.replace('mailto:info@eurostatus.com', 'mailto:eurostatus@ro.ru')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
