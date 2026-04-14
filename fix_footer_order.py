import os
import re

dir_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship'

# We want to swap:
# <li class="footer-socials" ...>...</li> (which spans multiple lines)
# with:
# <li><span class="icon">... Пн-Пт: 10:00 - 19:00</li>

# The regex matches footer-socials block and the next <li> block
# Group 1: <li class="footer-socials" ...>...</li>
# Group 2: \n
# Group 3: <li>...Пн-Пт:...</li>
regex = re.compile(
    r'(<li class="footer-socials".*?</li>)(\s*)(<li><span class="icon"><svg[^>]*>.*?<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></span> Пн-Пт: 10:00 - 19:00</li>)', 
    re.DOTALL | re.IGNORECASE
)

for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        filepath = os.path.join(dir_path, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        def replacer(match):
            socials = match.group(1)
            space = match.group(2)
            hours = match.group(3)
            # Add a larger top margin to the socials so it visually separates from the list
            socials = socials.replace('margin-top: 15px;', 'margin-top: 25px;')
            return hours + space + socials

        new_content = regex.sub(replacer, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
