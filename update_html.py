import os
import re

dir_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove existing favicon links
        content = re.sub(r'[ \t]*<link[^>]*rel=[\'\"](?:shortcut icon|icon)[\'\"][^>]*>\n?', '', content, flags=re.IGNORECASE)

        # Insert new favicon right before </head>
        favicon_tag = '    <link rel="icon" type="image/png" href="./favicon.png">\n'
        content = content.replace('</head>', f'{favicon_tag}</head>')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print('Successfully added the favicon to all HTML files.')
