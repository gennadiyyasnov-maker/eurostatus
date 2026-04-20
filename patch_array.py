import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_array = 'const countries = ["Евросоюза", "Румынии", "Болгарии", "Словении", "Польши", "Армении", "Испании"];'
new_array = 'const countries = ["Евросоюза", "Румынии", "Болгарии", "Словении", "Польши", "Турции", "Австрии", "Израиля", "Германии", "Венгрии", "Армении", "Испании"];'

if old_array in content:
    content = content.replace(old_array, new_array)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Array updated successfully.")
else:
    print("Array not found. Please review index.html manually.")
