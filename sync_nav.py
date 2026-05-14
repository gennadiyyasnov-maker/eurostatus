import re
import glob

def sync_headers_footers():
    with open('index.html', 'r', encoding='utf-8') as f:
        idx = f.read()
    
    header_match = re.search(r'<header class="main-header".*?</header>', idx, re.DOTALL)
    footer_match = re.search(r'<footer class="main-footer">.*?</footer>', idx, re.DOTALL)
    
    if header_match and footer_match:
        for file in glob.glob('*.html'):
            if file == 'index.html':
                continue
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = re.sub(r'<header class="main-header".*?</header>', header_match.group(0), content, flags=re.DOTALL)
            new_content = re.sub(r'<footer class="main-footer">.*?</footer>', footer_match.group(0), new_content, flags=re.DOTALL)
            
            if new_content != content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {file}")

sync_headers_footers()
