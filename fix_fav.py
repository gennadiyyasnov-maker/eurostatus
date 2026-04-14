import os
import re

base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
for f in os.listdir(base_dir):
    if f.endswith('.html'):
        p = os.path.join(base_dir, f)
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # fix favicon
        content = re.sub(r'href=[\'\"]\./favicon\.png[\'\"]', 'href="./assets/images/favicon.png"', content)
        
        with open(p, 'w', encoding='utf-8') as file:
            file.write(content)
print("Fix applied to favicons.")
