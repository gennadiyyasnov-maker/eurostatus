import re

with open('blog.html', 'r', encoding='utf-8') as f:
    text = f.read()

new_card = '''            <!-- Article 5 (News) -->
            <a href="/article-news-schengen.html" style="text-decoration: none; display: flex; flex-direction: column; background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.05); transition: transform 0.3s; border: 1px solid rgba(11,32,70,0.05);" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='none'">
                <div style="height: 200px; background: url('/assets/images/schengen_border_news.png') center/cover;"></div>
                <div style="padding: 30px; display: flex; flex-direction: column; flex-grow: 1;">
                    <div style="color: #e53e3e; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; margin-bottom: 10px; display: flex; align-items: center; gap: 5px;"><span style="display: inline-block; width: 8px; height: 8px; background: #e53e3e; border-radius: 50%; animation: pulse 2s infinite;"></span> МОЛНИЯ</div>
                    <h3 style="color: #0B2046; font-size: 1.3rem; margin-bottom: 15px; font-family: 'Times New Roman', serif;">Свершилось: Отмена сухопутных границ Шенгена для Румынии и Болгарии</h3>
                    <p style="color: #4a5568; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px; flex-grow: 1;">Историческое событие, которого ждали миллионы: Совет ЕС окончательно утвердил снятие сухопутных границ. Что это значит для репатриантов?</p>
                    <div style="color: #0B2046; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 5px;">Читать статью <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></div>
                </div>
            </a>
            
'''

text = text.replace('<!-- Article 4 (Fears) -->', new_card + '<!-- Article 4 (Fears) -->')

# Add pulse animation style to the head if it's not there
if '@keyframes pulse' not in text:
    style_block = '''<style>
@keyframes pulse {
  0% { box-shadow: 0 0 0 0 rgba(229, 62, 62, 0.7); }
  70% { box-shadow: 0 0 0 10px rgba(229, 62, 62, 0); }
  100% { box-shadow: 0 0 0 0 rgba(229, 62, 62, 0); }
}
</style>
'''
    text = text.replace('</head>', style_block + '</head>')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added news to blog.html")
