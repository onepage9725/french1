with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Change lg:h-[90%] to h-full for the main image
text = text.replace('class="object-cover w-full h-full lg:h-[90%] z-0 rounded-b-lg mask-image-bottom mix-blend-multiply opacity-90"',
                    'class="object-cover w-full h-full lg:h-full z-0 rounded-b-[40px] lg:rounded-[40px] mask-image-bottom mix-blend-multiply opacity-90"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
