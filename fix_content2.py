import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix copyright specifically
text = text.replace("Copyright © 2026 recrutemaroc.com", "Copyright © 2026 Recrute Maroc")
text = text.replace("Copyright &copy; 2026 recrutemaroc.com", "Copyright &copy; 2026 Recrute Maroc")

# Fix the broken section image
old_img = "https://images.unsplash.com/photo-1515378960530-7c0da6229674?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80"
new_img = "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80"
text = text.replace(old_img, new_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
