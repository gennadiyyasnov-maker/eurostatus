import json

f = open('translations.json', 'r', encoding='utf-8')
d = json.load(f)
f.close()

# The translation file might have a different format, checking keys
if 'Паспорт Евросоюза за 12 месяцев' in d:
    val = d.pop('Паспорт Евросоюза за 12 месяцев')
    d['Паспорт Евросоюза за 5-12 месяцев'] = val
elif 'en' in d and 'Паспорт Евросоюза за 12 месяцев' in d['en']:
    val = d['en'].pop('Паспорт Евросоюза за 12 месяцев')
    d['en']['Паспорт Евросоюза за 5-12 месяцев'] = 'EU Passport in 5-12 months'

f = open('translations.json', 'w', encoding='utf-8')
json.dump(d, f, ensure_ascii=False, indent=2)
f.close()
