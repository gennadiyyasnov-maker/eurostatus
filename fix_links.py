import os
import glob

# Search for all HTML files
html_files = glob.glob('*.html')
links_to_fix = [
    ('href="/citizenship-eu"', 'href="citizenship-eu.html"'),
    ('href="/residency"', 'href="residency.html"'),
    ('href="/investment"', 'href="investment.html"'),
    ('href="/visas"', 'href="visas.html"'),
    ('href="/reviews"', 'href="reviews.html"'),
    ('href="/faq"', 'href="faq.html"'),
    ('href="/about"', 'href="about.html"'),
    ('href="/contact"', 'href="contact.html"'),
    ('href="/terms"', 'href="terms.html"'),
    ('href="/privacy"', 'href="privacy.html"'),
    ('href="/refund"', 'href="refund.html"')
]

for file_path in html_files:
    if file_path.startswith('temp_') or file_path.startswith('recovered_'):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for old_link, new_link in links_to_fix:
        content = content.replace(old_link, new_link)
        
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Fixed links in {file_path}')
print('Done!')
