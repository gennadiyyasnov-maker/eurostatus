import os
import re
import glob
import shutil

project_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
source_image = r"C:\Users\genna\.gemini\antigravity\brain\a9224eb0-7d40-4c1f-b25c-790f90685f9b\og_image_premium_1777970880149.png"
target_image = os.path.join(project_dir, "assets", "images", "og_image.png")

# Copy the image to assets
if os.path.exists(source_image):
    os.makedirs(os.path.dirname(target_image), exist_ok=True)
    shutil.copy2(source_image, target_image)
    print("Image copied to assets/images/og_image.png")

# Process all HTML files
html_files = glob.glob(os.path.join(project_dir, "*.html"))

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
        page_title = title_match.group(1) if title_match else "EuroStatus | Международная юридическая компания"

        # Check if OG tags already exist
        if 'property="og:image"' in content:
            # Remove old OG/Twitter tags
            content = re.sub(r'<meta property="og:.*?>\n?', '', content)
            content = re.sub(r'<meta name="twitter:.*?>\n?', '', content)

        og_tags = f"""
<meta property="og:title" content="{page_title}" />
<meta property="og:description" content="Официальное и полностью легальное оформление гражданства Евросоюза. Работаем строго по договору." />
<meta property="og:image" content="https://eurostatus.online/assets/images/og_image.png" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://eurostatus.online/" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{page_title}" />
<meta name="twitter:description" content="Официальное и полностью легальное оформление гражданства Евросоюза." />
<meta name="twitter:image" content="https://eurostatus.online/assets/images/og_image.png" />
"""

        # Insert after <head> or <title>
        if '<title>' in content:
            content = re.sub(r'(<title>.*?</title>)', r'\1' + og_tags, content, flags=re.IGNORECASE)
        else:
            content = re.sub(r'(<head[^>]*>)', r'\1' + og_tags, content, flags=re.IGNORECASE)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated OG tags in {os.path.basename(file_path)}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
