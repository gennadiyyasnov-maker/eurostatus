import glob
import re

for f in glob.glob('*.html'):
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # We look for exactly two blog items in a row
        new_content = re.sub(
            r'<li><a href="/blog\.html">Блог</a></li>\s*<li><a href="/blog\.html">Блог</a></li>',
            r'<li><a href="/blog.html">Блог</a></li>',
            content
        )
        
        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Fixed {f}")
    except Exception as e:
        print(f"Error on {f}: {e}")
