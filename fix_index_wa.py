import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Modify the floating chat button
btn_code = """        <!-- Floating Chat Icon -->
        <button id="floatingWaBtn" class="fixed bottom-8 right-8 bg-[#3f8a3e] hover:bg-[#2e682d] text-white p-4 rounded-full shadow-lg transition-transform hover:scale-105 z-50">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="w-7 h-7">
                <path fill-rule="evenodd" d="M3 4.5A2.5 2.5 0 015.5 2h13A2.5 2.5 0 0121 4.5v11A2.5 2.5 0 0118.5 18H14v4l-4-4H5.5A2.5 2.5 0 013 15.5v-11zM6 8a1 1 0 011-1h10a1 1 0 110 2H7a1 1 0 01-1-1zm0 4a1 1 0 011-1h10a1 1 0 110 2H7a1 1 0 01-1-1z" clip-rule="evenodd" />
            </svg>
        </button>"""

text = re.sub(r'        <!-- Floating Chat Icon -->\n        <button class="fixed bottom-8 right-8 bg-\[#3f8a3e\].*?</button>', btn_code, text, flags=re.DOTALL)

js_integration = """        });

        // WhatsApp Floating Button Randomizer Logic
        const floatingWaBtn = document.getElementById('floatingWaBtn');
        floatingWaBtn.addEventListener('click', () => {
            const storedNumbers = JSON.parse(localStorage.getItem('whatsapp_numbers')) || [];
            const activeNumbers = storedNumbers.filter(n => n.active !== false); // active defaults to true
            
            if (activeNumbers.length === 0) {
                // Default fallback backup number if admin dashboard is empty/never used
                window.open('https://wa.me/212600000000', '_blank');
                return;
            }
            
            const randomItem = activeNumbers[Math.floor(Math.random() * activeNumbers.length)];
            window.open('https://wa.me/' + randomItem.number, '_blank');
        });"""

text = text.replace('        });\n\n        mobileLinks.forEach', js_integration + '\n\n        mobileLinks.forEach')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
