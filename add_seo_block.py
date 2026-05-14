import os

base_dir = r"c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship"
index_path = os.path.join(base_dir, "index.html")

seo_block = """
<!-- SEO Text Block -->
<section style="padding: 60px 0; background: #fff; border-top: 1px solid rgba(0,0,0,0.05);">
    <div class="container" style="max-width: 900px; margin: 0 auto; color: #4a5568; font-size: 0.95rem; line-height: 1.6;">
        <h2 style="font-family: 'Times New Roman', serif; color: #0B2046; font-size: 1.5rem; margin-bottom: 20px;">Евростатус (EuroStatus) — ваш надежный проводник к гражданству ЕС</h2>
        <p style="margin-bottom: 15px;">Международная юридическая компания <strong>Евростатус</strong> специализируется на легальном оформлении второго гражданства, видов на жительство (ВНЖ и ПМЖ) и визовой поддержке. За годы работы эксперты <strong>EuroStatus</strong> помогли сотням семей обрести свободу передвижения и уверенность в завтрашнем дне. Мы предлагаем полностью прозрачную процедуру репатриации в страны Европейского Союза (в первую очередь, Румынию и Болгарию), а также сопровождаем инвестиционные программы по всему миру.</p>
        <p style="margin-bottom: 15px;">Почему клиенты выбирают <strong>Евростатус</strong>? В отличие от многих агентств, мы работаем исключительно в легальном поле. Каждое досье проходит строгий внутренний аудит. Если у вас нет законных оснований (корней) для репатриации, юристы <strong>Евростатуса</strong> подберут альтернативную программу — будь то "Цифровой кочевник" (Digital Nomad), виза инвестора или ВНЖ через открытие представительства бизнеса. Все финансовые гарантии прописаны в договоре, включая политику возврата средств.</p>
        <p>Обращаясь в <strong>EuroStatus</strong>, вы получаете комплексное сопровождение "под ключ": от генеалогического поиска и перевода архивных справок до персонального сопровождения адвокатом на подаче документов и присяге. Доверьте свое европейское будущее профессионалам компании Евростатус.</p>
    </div>
</section>
"""

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

if "<!-- SEO Text Block -->" not in content:
    # Insert before closing </main>
    content = content.replace("</main>", seo_block + "\n</main>")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SEO block added to index.html")
else:
    print("SEO block already exists in index.html")
