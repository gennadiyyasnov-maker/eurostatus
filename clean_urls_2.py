import glob
import re

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    def replacer(match):
        page = match.group(1)
        hash_part = match.group(2) if match.group(2) else ''
        if page == 'index':
            return f'href="/{hash_part}"'
        return f'href="/{page}{hash_part}"'

    new_content = re.sub(r'href="(?:\.\/)?([a-zA-Z0-9_\-]+)\.html(#[a-zA-Z0-9_\-]+)?"', replacer, content)
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1

print(f"Updated {count} files.")
