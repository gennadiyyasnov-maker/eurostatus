import os
import shutil

brain_dir = r"C:\Users\genna\.gemini\antigravity\brain\95c24219-2be4-4424-9152-dfe06efccaa5"
site_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
img_dest_dir = os.path.join(site_dir, "assets", "images")

images = {
    "romania_passport_real_1778744758353.png": "romania_passport_real.png",
    "romania_bucharest_street_1778744774096.png": "romania_bucharest_street.png",
    "romania_justice_building_1778744787091.png": "romania_justice_building.png",
    "bulgaria_passport_real_1778744809279.png": "bulgaria_passport_real.png",
    "bulgaria_sofia_city_1778744828846.png": "bulgaria_sofia_city.png",
    "bulgaria_airport_schengen_1778744845379.png": "bulgaria_airport_schengen.png",
    "eu_business_meeting_1778744868984.png": "eu_business_meeting.png",
    "eu_family_travel_1778744883991.png": "eu_family_travel.png",
    "eu_university_1778744899548.png": "eu_university.png"
}

# Ensure destination directory exists
os.makedirs(img_dest_dir, exist_ok=True)

# Copy images
for src_name, dst_name in images.items():
    src_path = os.path.join(brain_dir, src_name)
    dst_path = os.path.join(img_dest_dir, dst_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)

# HTML snippets
img_style = 'style="width: 100%; border-radius: 12px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.1); object-fit: cover;"'

# 1. Update article-romania.html
rom_path = os.path.join(site_dir, "article-romania.html")
with open(rom_path, "r", encoding="utf-8") as f:
    rom_html = f.read()

rom_html = rom_html.replace('<h2>Почему именно Румыния?</h2>', f'<img src="/assets/images/romania_passport_real.png" alt="Паспорт Румынии" {img_style}>\n<h2>Почему именно Румыния?</h2>')
rom_html = rom_html.replace('<h3>1. Генеалогический поиск</h3>', f'<img src="/assets/images/romania_bucharest_street.png" alt="Улицы Бухареста" {img_style}>\n<h3>1. Генеалогический поиск</h3>')
rom_html = rom_html.replace('<h3>4. Выход в приказ и сдача присяги</h3>', f'<img src="/assets/images/romania_justice_building.png" alt="Минюст Румынии" {img_style}>\n<h3>4. Выход в приказ и сдача присяги</h3>')

with open(rom_path, "w", encoding="utf-8") as f:
    f.write(rom_html)

# 2. Update article-bulgaria.html
bulg_path = os.path.join(site_dir, "article-bulgaria.html")
with open(bulg_path, "r", encoding="utf-8") as f:
    bulg_html = f.read()

bulg_html = bulg_html.replace('<h2>Вступление Болгарии в Шенген: что это значит?</h2>', f'<img src="/assets/images/bulgaria_passport_real.png" alt="Паспорт Болгарии" {img_style}>\n<h2>Вступление Болгарии в Шенген: что это значит?</h2>')
bulg_html = bulg_html.replace('<h3>Преимущества болгарского гражданства:</h3>', f'<img src="/assets/images/bulgaria_sofia_city.png" alt="Центр Софии" {img_style}>\n<h3>Преимущества болгарского гражданства:</h3>')
bulg_html = bulg_html.replace('<h2>Альтернатива: ВНЖ в Болгарии через представительство</h2>', f'<img src="/assets/images/bulgaria_airport_schengen.png" alt="Аэропорт Шенген" {img_style}>\n<h2>Альтернатива: ВНЖ в Болгарии через представительство</h2>')

with open(bulg_path, "w", encoding="utf-8") as f:
    f.write(bulg_html)

# 3. Update article-benefits.html
ben_path = os.path.join(site_dir, "article-benefits.html")
with open(ben_path, "r", encoding="utf-8") as f:
    ben_html = f.read()

ben_html = ben_html.replace('<h2>1. Глобальная мобильность без границ</h2>', f'<img src="/assets/images/eu_family_travel.png" alt="Семья в Европе" {img_style}>\n<h2>1. Глобальная мобильность без границ</h2>')
ben_html = ben_html.replace('<h2>2. Бизнес без санкций и блокировок</h2>', f'<img src="/assets/images/eu_business_meeting.png" alt="Бизнес в ЕС" {img_style}>\n<h2>2. Бизнес без санкций и блокировок</h2>')
ben_html = ben_html.replace('<h2>4. Европейское образование для детей</h2>', f'<img src="/assets/images/eu_university.png" alt="Университет в Европе" {img_style}>\n<h2>4. Европейское образование для детей</h2>')

with open(ben_path, "w", encoding="utf-8") as f:
    f.write(ben_html)

print("Images copied and articles updated.")
