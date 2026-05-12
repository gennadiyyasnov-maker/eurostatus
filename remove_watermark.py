import re

def remove_watermark(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove CSS
    content = re.sub(r'\s*/\* Watermark Logo \*/.*?\}\n', '', content, flags=re.DOTALL)
    # Remove HTML
    content = re.sub(r'\s*<!-- Image Watermark -->\n\s*<img class="watermark" src="data:image/png;base64,[^"]+" alt="Logo">\n', '\n', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

remove_watermark('invoice_template.html')
remove_watermark('receipt_template.html')
print('Watermarks removed!')
