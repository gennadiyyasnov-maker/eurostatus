import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = content.replace('href="/privacy"', 'href="/privacy.html"').replace('href="/terms"', 'href="/terms.html"')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
