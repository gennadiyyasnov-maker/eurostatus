import glob
import re
import os

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

count = 0
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace links like href="page.html#section"
    def repl_link_hash(match):
        page = match.group(1)
        hash_val = match.group(2)
        if page == 'index':
            return f'href="/{hash_val}"'
        return f'href="/{page}{hash_val}"'
        
    new_content = re.sub(r'href="([a-zA-Z0-9_\-]+)\.html(#[a-zA-Z0-9_\-]+)"', repl_link_hash, content)
    
    # 2. Replace links like href="page.html"
    def repl_link(match):
        page = match.group(1)
        if page == 'index':
            return 'href="/"'
        return f'href="/{page}"'

    new_content = re.sub(r'href="([a-zA-Z0-9_\-]+)\.html"', repl_link, new_content)
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {os.path.basename(file)}")

print(f"Updated {count} files.")
