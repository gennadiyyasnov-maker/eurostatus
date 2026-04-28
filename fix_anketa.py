with open('anketa.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# 1. Replace the long form with the short form
start_marker = "<!-- 1. Заявитель -->"
end_marker = "<!-- 6. Пакет услуг -->"
new_form = """<!-- 1. Заявитель -->
                    <div class="form-section">
                        <h3>1. Ваши данные</h3>
                        <div class="person-block">
                            <div class="grid-2-col">
                                <div class="input-group">
                                    <label>ФИО *</label>
                                    <input type="text" name="applicant_fio" required placeholder="Иванов Иван Иванович">
                                </div>
                                <div class="input-group">
                                    <label>Телефон для связи *</label>
                                    <input type="tel" name="phone" required placeholder="+7 (999) 000-00-00">
                                </div>
                                <div class="input-group" style="grid-column: 1 / -1;">
                                    <label>Что известно о корнях? *</label>
                                    <textarea name="great_grandparents_info" rows="4" required placeholder="Напишите кратко, что известно о происхождении предков (например: дедушка родился в Болгарии/Румынии, или 'пока ничего не известно')"></textarea>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 2. Пакет услуг -->\n                    """

content = content.split(start_marker)[0] + new_form + content.split(end_marker)[1]

# 2. Rename headings
content = content.replace('<h3>6. Пакет услуг</h3>', '<h3>2. Пакет услуг</h3>')
content = content.replace('<!-- 7. Загрузка файлов -->', '<!-- 3. Загрузка файлов -->')
content = content.replace('<h3>7. Прикрепление файлов</h3>', '<h3>3. Прикрепление файлов</h3>')

# 3. Replace the JS part
js_start = "// Сбор чекбоксов"
js_end = "try {"
new_js = """// Формирование текста
                let text = `📋 <b>БЫСТРАЯ АНКЕТА НА ГРАЖДАНСТВО</b>\\n\\n`;
                text += `👤 <b>ЗАЯВИТЕЛЬ:</b> ${fd.get('applicant_fio')}\\n`;
                text += `Телефон: ${fd.get('phone')}\\n\\n`;
                text += `📜 <b>ИЗВЕСТНО О КОРНЯХ:</b>\\n${fd.get('great_grandparents_info')}\\n\\n`;
                text += `💼 <b>ПАКЕТ УСЛУГ:</b>\\n${fd.get('selected_package')}\\n\\n`;

                try {"""

content = content.split(js_start)[0] + new_js + content.split(js_end)[1]

with open('anketa.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
