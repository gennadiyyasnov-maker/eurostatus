import os
import glob
import re

base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

nav_regex = re.compile(r'(<li><a\s*href="/about(?:.html)?">\s*О компании\s*</a></li>)', re.IGNORECASE)

footer_nav_regex = re.compile(r'(<li><a href="/reviews">Отзывы клиентов</a></li>)', re.IGNORECASE)

nav_addition = '\n<li><a href="/blog.html">Блог</a></li>'

for file_path in html_files:
    # Skip files that don't need the header
    filename = os.path.basename(file_path)
    if filename.startswith("recovered_") or filename in ["temp_img.html", "invoice_template.html", "receipt_template.html", "font_test.html"]:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    modified = False
    
    # Check if blog is already in nav
    if 'href="/blog.html"' not in content:
        # 1. Main Navigation
        if nav_regex.search(content):
            content = nav_regex.sub(r'\1' + nav_addition, content)
            modified = True
            
        # 2. Footer Navigation
        if footer_nav_regex.search(content):
            content = footer_nav_regex.sub(nav_addition + r'\n\1', content)
            modified = True
            
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated nav in {filename}")
    else:
        print(f"Skipped {filename}")
