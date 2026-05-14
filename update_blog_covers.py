import os
import shutil

brain_dir = r"C:\Users\genna\.gemini\antigravity\brain\95c24219-2be4-4424-9152-dfe06efccaa5"
site_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
img_dest_dir = os.path.join(site_dir, "assets", "images")

images = {
    "blog_cover_romania_1778745149034.png": "blog_cover_romania.png",
    "blog_cover_bulgaria_1778745173943.png": "blog_cover_bulgaria.png",
    "blog_cover_benefits_1778745189757.png": "blog_cover_benefits.png"
}

os.makedirs(img_dest_dir, exist_ok=True)

for src_name, dst_name in images.items():
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(img_dest_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)

blog_path = os.path.join(site_dir, "blog.html")
with open(blog_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the cover images
html = html.replace("url('/assets/images/romania_card.png')", "url('/assets/images/blog_cover_romania.png')")
html = html.replace("url('/assets/images/europe_residency_card.png')", "url('/assets/images/blog_cover_bulgaria.png')")
html = html.replace("url('/assets/images/1.jpg')", "url('/assets/images/blog_cover_benefits.png')")

with open(blog_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Blog covers updated.")
