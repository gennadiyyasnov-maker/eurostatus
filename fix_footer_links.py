import glob

html_files = glob.glob('*.html')

for file_path in html_files:
    if file_path.startswith('temp_') or file_path.startswith('recovered_'):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix Russian links
    content = content.replace('href="#">Гражданство ЕС</a>', 'href="citizenship-eu.html">Гражданство ЕС</a>')
    content = content.replace('href="#">ВНЖ / ПМЖ</a>', 'href="residency.html">ВНЖ / ПМЖ</a>')
    
    # Fix English links (en.html, index-en.html)
    content = content.replace('href="#">EU Citizenship</a>', 'href="citizenship-eu.html">EU Citizenship</a>')
    content = content.replace('href="#">Residency (VNJ/PMJ)</a>', 'href="residency.html">Residency (VNJ/PMJ)</a>')

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed footer links in {file_path}')

print('Done fixing footer links!')
