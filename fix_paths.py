import glob

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Force all image references to be absolute from domain root
    content = content.replace('../assets/images/', '/assets/images/')
    content = content.replace('./assets/images/', '/assets/images/')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
