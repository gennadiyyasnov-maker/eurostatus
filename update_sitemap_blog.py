import os

base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
sitemap_path = os.path.join(base_dir, "sitemap.xml")

new_urls = """
  <url>
    <loc>https://eurostatus.online/blog</loc>
    <lastmod>2026-05-14</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://eurostatus.online/article-romania</loc>
    <lastmod>2026-05-14</lastmod>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://eurostatus.online/article-bulgaria</loc>
    <lastmod>2026-05-14</lastmod>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://eurostatus.online/article-benefits</loc>
    <lastmod>2026-05-14</lastmod>
    <priority>0.7</priority>
  </url>
"""

with open(sitemap_path, "r", encoding="utf-8") as f:
    content = f.read()

if "<loc>https://eurostatus.online/blog</loc>" not in content:
    content = content.replace("</urlset>", new_urls + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Sitemap updated.")
else:
    print("Sitemap already updated.")
