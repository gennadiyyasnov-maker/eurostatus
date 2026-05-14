import os
import glob

def fix_favicons():
    # Fix all HTML files
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace relative favicon with absolute
        if 'href="./assets/images/favicon.png' in content:
            content = content.replace('href="./assets/images/favicon.png', 'href="/assets/images/favicon.png')
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
                print(f"Fixed relative favicon path in {file}")

    # Inject favicon into gen_article_noroots.py
    with open('gen_article_noroots.py', 'r', encoding='utf-8') as f:
        py_content = f.read()
    
    if '<link rel="icon"' not in py_content:
        py_content = py_content.replace(
            '<link rel="stylesheet" href="./assets/css/style.css">',
            '<link rel="stylesheet" href="/assets/css/style.css">\n    <link rel="icon" type="image/png" href="/assets/images/favicon.png">'
        )
        with open('gen_article_noroots.py', 'w', encoding='utf-8') as f:
            f.write(py_content)
            print("Injected favicon into gen_article_noroots.py")

if __name__ == '__main__':
    fix_favicons()
