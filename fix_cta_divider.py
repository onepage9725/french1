import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add luxury divider
divider_html = """    <!-- Luxury Divider -->
    <div class="container mx-auto px-4 mb-24 flex justify-center items-center opacity-80">
        <div class="h-px w-32 md:w-64 bg-gradient-to-r from-transparent via-gray-300 to-transparent"></div>
        <div class="mx-6 flex flex-col items-center gap-1.5 opacity-60">
            <div class="w-1 h-1 rounded-full bg-[#3f8a3e]"></div>
            <div class="w-1.5 h-1.5 rounded-full bg-[#08265c] transform rotate-45"></div>
            <div class="w-1 h-1 rounded-full bg-[#3f8a3e]"></div>
        </div>
        <div class="h-px w-32 md:w-64 bg-gradient-to-r from-transparent via-gray-300 to-transparent"></div>
    </div>

    <!-- Registration Form Section -->"""

text = text.replace('    <!-- Registration Form Section -->', divider_html)

# 2. Update CTA links 
# Find buttons with bg-[#3f8a3e] and an href that isn't #inscription
# For example: <a href="#" class="bg-[#3f8a3e]... -> <a href="#inscription" ...
# also <a href="#contact" class="mobile-link ... bg-[#3f8a3e]... -> <a href="#inscription"

text = re.sub(r'<a href="#"(.*?)bg-\[#3f8a3e\]', r'<a href="#inscription"\1bg-[#3f8a3e]', text)
text = re.sub(r'<a href="#contact"(.*?)bg-\[#3f8a3e\]', r'<a href="#inscription"\1bg-[#3f8a3e]', text)

# Find floating chat button / Postuler button and change just in case? Or only <a> tags.
# We handled the <a> tags. Do we need to update any JS navigation? They behave as standard anchor links.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
