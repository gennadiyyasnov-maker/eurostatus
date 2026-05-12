import os
from datetime import datetime

base_url = "https://eurostatus.online"
directory = 'c:/Users/genna/.gemini/antigravity/scratch/eu-citizenship/'

valid_files = [
    'about.html', 'anketa.html', 'contact.html', 'index-en.html', 
    'faq.html', 'residency.html', 'reviews.html', 'visas.html', 
    'privacy.html', 'terms.html', 'refund.html', 'citizenship-eu.html', 'investment.html'
]

sitemap_path = os.path.join(directory, 'sitemap.xml')
robots_path = os.path.join(directory, 'robots.txt')

date_str = datetime.now().strftime("%Y-%m-%d")

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

# Index
sitemap_content += f'''  <url>
    <loc>{base_url}/</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
'''

for file in valid_files:
    if os.path.exists(os.path.join(directory, file)):
        priority = "0.8"
        
        sitemap_content += f'''  <url>
    <loc>{base_url}/{file}</loc>
    <lastmod>{date_str}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>
'''

sitemap_content += '</urlset>'

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

robots_content = f'''User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
'''

with open(robots_path, 'w', encoding='utf-8') as f:
    f.write(robots_content)

print(f"Generated sitemap.xml for EuroStatus and robots.txt")
