with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove Chinese characters
text = text.replace('Emploi à temps partiel / 兼职工作', 'Emploi à temps partiel')
text = text.replace('Emploi à temps plein / 全职工作', 'Emploi à temps plein')

# Change background to gradient
text = text.replace('<section id="inscription" class="container mx-auto px-4 py-16 mb-16 bg-white overflow-hidden relative">',
                    '<section id="inscription" class="container mx-auto px-4 py-16 mb-16 overflow-hidden relative">')

# The form wrapper is max-w-3xl mx-auto bg-gray-50
# If the user wants the section background to be gradient, we can wrap the container contents in a gradient background, or add it to the section. 
# To follow the container-style of the rest of the site (which has rounded-[40px] boxes), 
# let's change the max-w-3xl background OR wrap it. Currently, it's just a section.
