import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

location_html = """<div class="flex items-center gap-3 text-gray-400 text-sm">
                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"></path>
                            <circle cx="12" cy="10" r="3"></circle>
                        </svg>
                        <span>Casablanca, Morocco</span>
                    </div>"""

text = text.replace('<h3 class="font-bold text-xl mb-2">Contact</h3>', f'<h3 class="font-bold text-xl mb-2">Contact</h3>\n                    {location_html}')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
