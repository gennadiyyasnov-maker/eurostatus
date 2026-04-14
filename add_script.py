f = 'reviews.html'
with open(f, 'r', encoding='utf-8') as file:
    c = file.read()
c = c.replace('</body>', '<script type="module" src="./assets/js/main.js"></script>\n</body>')
with open(f, 'w', encoding='utf-8') as file:
    file.write(c)
