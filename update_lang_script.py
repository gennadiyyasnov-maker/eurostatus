import os
import re

dir_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship'

# 1. Regex to remove inline onclick from lang-switcher
# example: <a href="en.html" onclick="console.log('Navigating to EN...'); window.location.href='en.html'; return false;">EN</a> -> <a href="en.html">EN</a>
onclick_regex = re.compile(r'(\<a[^>]*href="[^"]*"\s*)onclick="[^"]*"([^>]*\>)', re.IGNORECASE)

# 2. Regex to inject the script at the end of body if not already there
script_tag = '<script src="./assets/js/lang.js"></script>\n</body>'

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Only affect a tags in .lang-switch
        # Wait, the best way to specifically target lang-switch is string replacement or precise regex
        # Since the links have 'active' class sometimes, let's just use string replace for known patterns
        
        # Actually doing a regex replace on the entire file for onclick="" is safe IF we only target window.location or console.log
        content = re.sub(r' onclick="console\.log\([^)]*\);\s*window\.location\.href=[^"]*;\s*return false;"', '', content)
        content = re.sub(r' onclick="window\.location\.href=[^"]*;\s*return false;"', '', content)

        if '<script src="./assets/js/lang.js"></script>' not in content:
            content = content.replace('</body>', script_tag)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
