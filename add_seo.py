import os
import glob
import re
from datetime import datetime

project_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
public_dir = os.path.join(project_dir, "public")
os.makedirs(public_dir, exist_ok=True)

# 1. Create robots.txt
robots_content = """User-agent: *
Allow: /

Sitemap: https://eurostatus.online/sitemap.xml
"""
with open(os.path.join(public_dir, "robots.txt"), 'w', encoding='utf-8') as f:
    f.write(robots_content)
print("Created robots.txt")

# 2. Add meta description and get valid pages for sitemap
html_files = glob.glob(os.path.join(project_dir, "*.html"))
valid_pages = []
ignore_prefixes = ['recovered_', 'temp_', 'font_test', 'template']

for file_path in html_files:
    basename = os.path.basename(file_path)
    
    # Skip ignored files for sitemap
    if any(basename.startswith(p) for p in ignore_prefixes):
        continue
        
    valid_pages.append(basename)

    # Inject <meta name="description">
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if we already have it
        if '<meta name="description"' not in content.lower():
            # Extract title to make a slightly dynamic description or just use standard
            # Let's use standard one
            desc_tag = '\n<meta name="description" content="Официальное и полностью легальное оформление гражданства Евросоюза. Работаем строго по договору. Бесплатная консультация миграционных юристов." />'
            
            # Insert after <head> or <title>
            if '<title>' in content:
                content = re.sub(r'(<title>.*?</title>)', r'\1' + desc_tag, content, flags=re.IGNORECASE)
            else:
                content = re.sub(r'(<head[^>]*>)', r'\1' + desc_tag, content, flags=re.IGNORECASE)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added description to {basename}")
    except Exception as e:
        print(f"Error processing {basename}: {e}")

# 3. Create sitemap.xml
today = datetime.now().strftime("%Y-%m-%d")
sitemap_urls = []

for page in valid_pages:
    # If index.html, URL is root
    if page == 'index.html':
        url = 'https://eurostatus.online/'
        priority = '1.0'
    else:
        # e.g. about.html -> https://eurostatus.online/about/ or https://eurostatus.online/about
        # Since the user used /reviews/ in WebpageBot, they likely strip .html and serve without it.
        name = page.replace('.html', '')
        url = f'https://eurostatus.online/{name}'
        priority = '0.8'
        
    sitemap_urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>""")

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_urls)}
</urlset>"""

with open(os.path.join(public_dir, "sitemap.xml"), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
print("Created sitemap.xml")
