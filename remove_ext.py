import os
import re

dir_path = r'C:\Users\genna\.gemini\antigravity\scratch\eu-citizenship'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

pages = ['about', 'citizenship-eu', 'residency', 'investment', 'visas', 'reviews', 'faq', 'contact', 'terms', 'privacy', 'refund']

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for p in pages:
        # replace href="p.html" with href="/p"
        content = re.sub(r'href=[\'\"]\/?' + p + r'\.html[\'\"]', f'href="/{p}"', content)
        # replace window.location.href='p.html'
        content = re.sub(r'window\.location\.href=[\'\"]\/?' + p + r'\.html[\'\"]', f'window.location.href="/{p}"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for h in html_files:
    process_file(os.path.join(dir_path, h))

print("Done replacing .html extensions.")
