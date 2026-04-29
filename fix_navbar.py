import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add smooth scrolling
text = text.replace('html, body {', 'html { scroll-behavior: smooth; }\n        html, body {')

# Add IDs to sections
text = text.replace('<main class="container mx-auto px-4 pb-12">', '<main id="accueil" class="container mx-auto px-4 pb-12">')

# About Us
text = text.replace('<!-- About Us Section -->\n    <section class="container mx-auto px-4 py-8 mb-12">', '<!-- About Us Section -->\n    <section id="apropos" class="container mx-auto px-4 py-8 mb-12">')

# Features/POURQUOI (Why we stand out)
text = text.replace('<!-- Open Positions Section -->\n    <section class="container mx-auto px-4 py-16 mb-12">', '<!-- Features/Why Us -->\n    <section id="fonctionnalites" class="container mx-auto px-4 py-16 mb-12">')

# CTA/Contact
text = text.replace('<!-- CTA Section -->\n    <section class="container mx-auto px-4 py-8 mb-16">', '<!-- CTA/Contact Section -->\n    <section id="contact" class="container mx-auto px-4 py-8 mb-16">')

# Jobs/Open Positions
text = text.replace('<!-- Open Positions Section -->\n    <section class="container mx-auto px-4 py-16 mb-12">', '<!-- Open Positions Section -->\n    <section id="offres" class="container mx-auto px-4 py-16 mb-12">')
# Wait, let's just do it dynamically by searching for the headers.
