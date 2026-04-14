import glob

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace(
        '<a class="btn-primary" href="#consultation">Консультация</a>',
        '<a href="#" onclick="openServiceModal(\'Индивидуальная консультация\'); return false;" class="btn-primary">Консультация</a>'
    )
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Total files updated: {count}")
