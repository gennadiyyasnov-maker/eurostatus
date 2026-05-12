import base64
import os
import re

img_path = r'C:\Users\genna\.gemini\antigravity\brain\a9224eb0-7d40-4c1f-b25c-790f90685f9b\media__1777961845508.png'
with open(img_path, 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

css_watermark = """        /* Watermark Logo */
        .watermark {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 70%;
            opacity: 0.12;
            mix-blend-mode: multiply;
            pointer-events: none;
            z-index: 0;
        }"""

html_watermark = f'        <!-- Image Watermark -->\n        <img class="watermark" src="data:image/png;base64,{b64}" alt="Logo">'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace CSS
    content = re.sub(r'        /\* Watermark Logo \*/.*?        }', css_watermark, content, flags=re.DOTALL)
    # Replace HTML
    content = re.sub(r'        <!-- Text Watermark -->\n\s*<div class="watermark">EUROSTATUS</div>', html_watermark, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('invoice_template.html')
update_file('receipt_template.html')
print('Done!')
