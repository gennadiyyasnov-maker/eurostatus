import os
import glob

html_files = glob.glob('*.html') + glob.glob('dist/**/*.html', recursive=True)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Replace article links
        content = content.replace('href="/article-romania.html"', 'href="/article-romania"')
        content = content.replace('href="/article-bulgaria.html"', 'href="/article-bulgaria"')
        content = content.replace('href="/article-benefits.html"', 'href="/article-benefits"')
        content = content.replace('href="/article-fears.html"', 'href="/article-fears"')
        content = content.replace('href="/article-news-schengen.html"', 'href="/article-news-schengen"')
        
        # Also handle potential lack of slash
        content = content.replace('href="article-romania.html"', 'href="/article-romania"')
        content = content.replace('href="article-bulgaria.html"', 'href="/article-bulgaria"')
        content = content.replace('href="article-benefits.html"', 'href="/article-benefits"')
        content = content.replace('href="article-fears.html"', 'href="/article-fears"')
        content = content.replace('href="article-news-schengen.html"', 'href="/article-news-schengen"')

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated articles links in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Done removing .html from article links")
