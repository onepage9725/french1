with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the outer container itself the gradient
text = text.replace(
    '<section id="inscription" class="container mx-auto px-4 py-16 mb-16 overflow-hidden relative">',
    """<section id="inscription" class="container mx-auto px-4 py-16 mb-16 relative">
        <div class="bg-gradient-to-br from-[#08265c] via-[#103b87] to-[#3f8a3e] rounded-[40px] px-4 md:px-12 py-16 shadow-2xl relative overflow-hidden">"""
)

# And add the closing div before </section>
text = text.replace(
    """        </div>
    </section>

    <!-- Footer -->""",
    """        </div>
        </div>
    </section>

    <!-- Footer -->"""
)

# Change text color inside the gradient block but outside the form box
text = text.replace(
    '<h2 class="text-3xl md:text-5xl font-black text-[#1f2937] leading-[1.1] mb-4">Rejoignez-nous</h2>',
    '<h2 class="text-3xl md:text-5xl font-black text-white leading-[1.1] mb-4">Rejoignez-nous</h2>'
)
text = text.replace(
    '<p class="text-gray-600">Remplissez le formulaire ci-dessous pour démarrer votre nouveau parcours.</p>',
    '<p class="text-white/80">Remplissez le formulaire ci-dessous pour démarrer votre nouveau parcours.</p>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
