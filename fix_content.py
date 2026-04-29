import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix location
text = text.replace("Zurich, Switzerland", "Casablanca, Morocco")
text = text.replace("Zurich, Suisse", "Casablanca, Morocco")
text = text.replace("123 rue principale", "Casablanca, Morocco") # fallback if it was something else?

# Let's fix image paths
text = text.replace('href="RecruteMaroc.png"', 'href="image/RecruteMaroc.png"')
text = text.replace('content="RecruteMaroc.png"', 'content="image/RecruteMaroc.png"')
text = text.replace('src="recrutemaroc-nbg.png"', 'src="image/recrutemaroc-nbg.png"')
text = text.replace('src="RecruteMaroc.png"', 'src="image/RecruteMaroc.png"')
text = text.replace('src="image/image/recrutemaroc-nbg.png"', 'src="image/recrutemaroc-nbg.png"')

# For the section image specifically:
# User said: the "Votre prochain chapitre commence ici !" section image is not showing
# Let's see what the image src was there, wait, I don't know the exact HTML for that image.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
