import glob
import os

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('<script src="./assets/js/lang.js"></script>', '')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
