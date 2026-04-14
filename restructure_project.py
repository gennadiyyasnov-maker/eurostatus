import os
import shutil
import re

base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
assets_dir = os.path.join(base_dir, "assets")
css_dir = os.path.join(assets_dir, "css")
js_dir = os.path.join(assets_dir, "js")
img_dir = os.path.join(assets_dir, "images")

for d in [assets_dir, css_dir, js_dir, img_dir]:
    os.makedirs(d, exist_ok=True)

# 1. Gather files
image_extensions = {".png", ".jpg", ".jpeg", ".svg", ".ico", ".gif", ".webp"}

files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
images_to_move = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
css_to_move = [f for f in files if f.endswith('.css')]
js_to_move = [f for f in files if f.endswith('.js')]

# Move root files
for f in images_to_move:
    shutil.move(os.path.join(base_dir, f), os.path.join(img_dir, f))
for f in css_to_move:
    shutil.move(os.path.join(base_dir, f), os.path.join(css_dir, f))
for f in js_to_move:
    shutil.move(os.path.join(base_dir, f), os.path.join(js_dir, f))

# Move public files
public_dir = os.path.join(base_dir, "public")
public_images = []
if os.path.exists(public_dir):
    for root, dirs, pub_files in os.walk(public_dir):
        for f in pub_files:
            if os.path.splitext(f)[1].lower() in image_extensions:
                src_path = os.path.join(root, f)
                dest_path = os.path.join(img_dir, f)
                if not os.path.exists(dest_path):
                    shutil.move(src_path, dest_path)
                public_images.append(f)

# 2. Update files
html_files = [f for f in files if f.endswith('.html')]

all_images = set(images_to_move + public_images)
all_css = set(css_to_move)
all_js = set(js_to_move)

def fix_html_content(content):
    # Regex replaces
    for img in all_images:
        # Match src="/myimg.png", src="./myimg.png", src="myimg.png", href="..."
        pattern_attr = r'(src|href)=[\'\"](?:\.|/)?(' + re.escape(img) + r')(?:\?v=[0-9]+)?[\'\"]'
        content = re.sub(pattern_attr, r'\1="./assets/images/\2"', content, flags=re.IGNORECASE)
        
        # Match url('/myimg.png') in inline style
        pattern_url = r'url\([\'\"]?(?:\.|/)?(' + re.escape(img) + r')(?:\?v=[0-9]+)?[\'\"]?\)'
        content = re.sub(pattern_url, r"url('./assets/images/\1')", content, flags=re.IGNORECASE)

    for css in all_css:
        pattern_attr = r'(src|href)=[\'\"](?:\.|/)?(' + re.escape(css) + r')(?:\?v=[0-9]+)?[\'\"]'
        content = re.sub(pattern_attr, r'\1="./assets/css/\2"', content, flags=re.IGNORECASE)
        
    for js in all_js:
        pattern_attr = r'(src|href)=[\'\"](?:\.|/)?(' + re.escape(js) + r')(?:\?v=[0-9]+)?[\'\"]'
        content = re.sub(pattern_attr, r'\1="./assets/js/\2"', content, flags=re.IGNORECASE)

    return content

for hf in html_files:
    hf_path = os.path.join(base_dir, hf)
    if os.path.exists(hf_path):
        with open(hf_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_html_content(content)
        
        with open(hf_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

for cf in all_css:
    cf_path = os.path.join(css_dir, cf)
    if os.path.exists(cf_path):
        with open(cf_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        for img in all_images:
            pattern_url = r'url\([\'\"]?(?:\.|/)?(' + re.escape(img) + r')(?:\?v=[0-9]+)?[\'\"]?\)'
            css_content = re.sub(pattern_url, r"url('../images/\1')", css_content, flags=re.IGNORECASE)
            
        with open(cf_path, 'w', encoding='utf-8') as f:
            f.write(css_content)

print(f"Moved {len(images_to_move) + len(public_images)} images, {len(css_to_move)} css, {len(js_to_move)} js files.")
print(f"Updated paths in {len(html_files)} HTML files and associated CSS.")
