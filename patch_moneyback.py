import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_chunk = """<div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Риск: Получить отказ и испортить визовую историю навсегда
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Только 100% законная прозрачная репатриация</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Мы не восстанавливаем корни "из воздуха" и не используем поддельные справки. Если вы не имеете законных оснований — мы откажем вам еще на первичном аудите. Все документы проходят трехкратную закрытую независимую проверку перед подачей в Минюст.</p>"""

new_chunk = """<div style="color: #e53e3e; font-weight: 600; font-size: 0.95rem; margin-bottom: 10px; display: inline-flex; align-items: center; gap: 8px; background: rgba(229, 62, 62, 0.1); padding: 4px 12px; border-radius: 20px;">
               Прямой риск: Получить отказ Минюста и навсегда потерять вложенные деньги
            </div>
            <h3 style="color: #0B2046; font-size: 1.5rem; font-family: 'Times New Roman', serif; margin-bottom: 15px;">Официальная гарантия возврата средств по договору</h3>
            <p style="color: #4a5568; line-height: 1.6; margin: 0;">Мы уверены в легальности досье на 100%, поэтому берем все риски отказов на себя. В нашем официальном договоре <strong>прямым текстом прописан пункт о возврате средств</strong>: если по каким-либо причинам вы не получите европейский паспорт, мы вернем вам деньги в полном объеме. Вы защищены юридически.</p>"""

if old_chunk in content:
    content = content.replace(old_chunk, new_chunk)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Success")
else:
    print("Chunk not found!")
