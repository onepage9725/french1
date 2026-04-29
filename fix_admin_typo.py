with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('renderRender();', 'renderTable();')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)
