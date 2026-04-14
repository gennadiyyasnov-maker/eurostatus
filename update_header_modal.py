import glob
import os

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace(
        '<a href="#consultation" class="btn-primary">Консультация</a>',
        '<a href="#" onclick="openServiceModal(\'Индивидуальная консультация\'); return false;" class="btn-primary">Консультация</a>'
    )
    
    new_content = new_content.replace(
        '<a href="#consultation" class="btn-primary">Consultation</a>',
        '<a href="#" onclick="openServiceModal(\'Individual Consultation\'); return false;" class="btn-primary">Consultation</a>'
    )
    
    if content != new_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {os.path.basename(file_path)}")

print(f"Total files updated: {count}")
