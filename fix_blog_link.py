import os
import glob

html_files = glob.glob('*.html') + glob.glob('dist/**/*.html', recursive=True)

for file in html_files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'href="/blog.html"' in content:
            content = content.replace('href="/blog.html"', 'href="/blog"')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("Done replacing /blog.html with /blog")
