import os
import glob

html_files = glob.glob(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\*.html')

fouc_script = """<script>
    if (document.cookie.includes('googtrans=/ru/en')) {
        document.documentElement.style.visibility = 'hidden';
    }
</script>"""

count = 0
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If already injected, skip
    if "document.documentElement.style.visibility = 'hidden';" in content:
        continue
        
    # Inject right after <head>
    new_content = content.replace('<head>', '<head>\n    ' + fouc_script, 1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    count += 1
    
print(f"Injected FOUC preventer into {count} files.")
