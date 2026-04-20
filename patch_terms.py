import os

def replace_in_file(filepath, old_text, new_text):
    if not os.path.exists(filepath):
        print(f"{filepath} not found")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} - text not found")

# 1. index.html
replace_in_file('index.html', 'Паспорт Евросоюза за 12 месяцев', 'Паспорт Евросоюза за 5-12 месяцев')

# 2. citizenship-eu.html
# Let's read and replace all 'От X месяцев' tags for citizenship
with open('citizenship-eu.html', 'r', encoding='utf-8') as f:
    c_content = f.read()

import re
# Look for pattern: >От XX месяцев< or >От X-XX месяцев< inside spans in citizenship cards
c_content = re.sub(r'>От 12 месяцев<', '>От 5 до 12 месяцев<', c_content)
c_content = re.sub(r'>От 12-15 месяцев<', '>От 5 до 12 месяцев<', c_content)
c_content = re.sub(r'>От 8 месяцев<', '>От 5 до 12 месяцев<', c_content)
c_content = re.sub(r'>От 10 месяцев<', '>От 5 до 12 месяцев<', c_content)

with open('citizenship-eu.html', 'w', encoding='utf-8') as f:
    f.write(c_content)
print("Updated citizenship-eu.html")

# 3. investment.html
replace_in_file('investment.html', 
    'национального развития) за 12 месяцев.</p>',
    'национального развития) от 5 до 12 месяцев.</p>')

# 4. faq.html
replace_in_file('faq.html',
    'Для программ репатриации средний срок от старта до паспорта — 14–24 месяца.',
    'Для программ репатриации средний срок всей процедуры от начала оформления до получения гражданства — 5–12 месяцев.')

