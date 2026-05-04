import os

dir_path = r'C:\Users\genna\.gemini\antigravity\scratch\eu-citizenship'
html_files = [f for f in os.listdir(dir_path) if f.endswith('.html')]

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # fix invalid escapes: onclick=\"window.location.href='/something'\" -> onclick="window.location.href='/something'"
    content = content.replace('onclick=\\"window.location.href=', 'onclick="window.location.href=')
    content = content.replace('\\"', '"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for h in html_files:
    process_file(os.path.join(dir_path, h))

print("Done fixing quotes.")
