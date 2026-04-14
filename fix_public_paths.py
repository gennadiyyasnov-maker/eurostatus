import glob
import os

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

replacements = {
    "/public/team/": "./assets/images/team/",
    "/public/Certificat Constatator_wm.jpg": "./assets/images/Certificat Constatator_wm.jpg",
    "/public/Certificat de înregistrare_wm.jpg": "./assets/images/Certificat de inregistrare_wm.jpg",
    "/public/": "./assets/images/"
}

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    new_content = content
    # Do specific replacements first
    for old, new in replacements.items():
        if old == "/public/": # Only do this after others are handled
            continue
        new_content = new_content.replace(old, new)
    
    # Do general /public/ fallback
    new_content = new_content.replace("/public/", "./assets/images/")
    
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Fixed paths in {os.path.basename(file_path)}")

print(f"Total files updated: {count}")
