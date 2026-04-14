from bs4 import BeautifulSoup
import json
import re

ru_doc = open(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\index.html', encoding='utf-8').read()
en_doc = open(r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\index-en.html', encoding='utf-8').read()

ru_soup = BeautifulSoup(ru_doc, 'html.parser')
en_soup = BeautifulSoup(en_doc, 'html.parser')

def extract_texts(soup):
    # Remove script and style
    for script in soup(["script", "style"]):
        script.extract()
    texts = []
    # Only keep visible text
    for string in soup.stripped_strings:
        if len(string.strip()) > 1 and not string.isnumeric():
            texts.append(string.strip())
    return texts

ru_texts = extract_texts(ru_soup)
en_texts = extract_texts(en_soup)

# Let's inspect length
print(f"RU texts: {len(ru_texts)}, EN texts: {len(en_texts)}")

dictionary = {}
min_len = min(len(ru_texts), len(en_texts))
for i in range(min_len):
    dictionary[ru_texts[i]] = en_texts[i]

with open('translations.json', 'w', encoding='utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=2)

print("Generated translations.json")
