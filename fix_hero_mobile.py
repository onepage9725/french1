import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Left Content z-index so it's above image
text = text.replace('<div class="lg:w-1/2 z-10 flex flex-col items-start pt-8 pb-16">', 
                    '<div class="lg:w-1/2 relative z-20 flex flex-col items-start lg:items-start pt-8 pb-16">')

# Fix Right Content Image to prevent overflow upwards
text = text.replace('class="object-cover h-[90%] z-10 rounded-b-lg mask-image-bottom h-auto mix-blend-multiply opacity-90"', 
                    'class="object-cover w-full h-full lg:h-[90%] z-0 rounded-b-lg mask-image-bottom mix-blend-multiply opacity-90"')

# Fix POURQUOI section alignment for mobile
text = text.replace('<div class="lg:w-[40%] flex flex-col justify-center items-start">',
                    '<div class="lg:w-[40%] flex flex-col justify-center items-center lg:items-start text-center lg:text-left">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
