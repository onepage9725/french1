import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Smooth scroll
if 'scroll-behavior: smooth' not in text:
    text = text.replace('<style>', '<style>\n        html { scroll-behavior: smooth; }')

# 2. Add IDs to the main sections based on their headers
text = text.replace('<!-- Hero Section -->', '<!-- Hero Section -->\n    <div id="accueil"></div>')
text = text.replace('<!-- About Us Section -->', '<!-- About Us Section -->\n    <div id="apropos" class="pt-6"></div>')
text = text.replace('<!-- Open Positions Section -->\n    <section class="container mx-auto px-4 py-16 mb-12">', '<!-- Open Positions Section -->\n    <section id="offres" class="container mx-auto px-4 pt-16 pb-12 mb-4">')
# wait, there are two "container mx-auto px-4 py-16 mb-12" according to grep.
