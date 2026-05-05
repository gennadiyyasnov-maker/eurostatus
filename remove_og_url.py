import glob, os, re
files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(r'<meta property="og:url" content="https://eurostatus.online/" />\n?', '', content)
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Done")
