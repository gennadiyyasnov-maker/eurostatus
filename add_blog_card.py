import re

with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_card = '''            <!-- Article 4 (Fears) -->
            <a href="/article-fears.html" style="text-decoration: none; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid rgba(11,32,70,0.05);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='none'">
                <div style="height: 200px; background: url('/assets/images/legal_security_eu.png') center/cover;"></div>
                <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                    <div style="color: #c9a050; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 10px;">Разбор мифов</div>
                    <h3 style="color: #0B2046; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Times New Roman', serif;">6 главных страхов при получении гражданства ЕС: разбор от юристов</h3>
                    <p style="color: #4a5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1;">Разбираем главные страхи россиян при оформлении европейского паспорта: отказы, налоги, армия, присяга и утечка данных.</p>
                    <div style="color: #0B2046; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;">Читать статью <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                </div>
            </a>
            
'''

text = text.replace('<!-- Article 1 -->', new_card + '<!-- Article 1 -->')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated blog.html")
