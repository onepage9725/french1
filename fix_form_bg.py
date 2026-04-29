with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove Chinese characters
text = text.replace('<option value="part-time">Emploi à temps partiel / 兼职工作</option>', '<option value="part-time">Emploi à temps partiel</option>')
text = text.replace('<option value="full-time">Emploi à temps plein / 全职工作</option>', '<option value="full-time">Emploi à temps plein</option>')
text = text.replace('Emploi à temps partiel /  兼职工作', 'Emploi à temps partiel')
text = text.replace('Emploi à temps plein / 全 职工作', 'Emploi à temps plein')
text = text.replace('Emploi à temps partiel / 兼职工作', 'Emploi à temps partiel')
text = text.replace('Emploi à temps plein / 全职工作', 'Emploi à temps plein')


# 2. Fix the gradient background
# Let's completely replace the <section id="inscription" ... to the <form> to make sure it looks right
old_top = '''    <!-- Registration Form Section -->
    <section id="inscription" class="container mx-auto px-4 py-16 mb-16 bg-white overflow-hidden relative">
        <div class="max-w-3xl mx-auto bg-gray-50 rounded-3xl p-8 md:p-12 shadow-[0_0_40px_rgba(0,0,0,0.05)] border border-gray-100">
            <div class="text-center mb-10">
                <h2 class="text-3xl md:text-5xl font-black text-white leading-[1.1] mb-4">Rejoignez-nous</h2>
                <p class="text-white/80">Remplissez le formulaire ci-dessous pour démarrer votre nouveau parcours.</p>
            </div>'''

new_top = '''    <!-- Registration Form Section -->
    <section id="inscription" class="container mx-auto px-4 py-16 mb-16 relative">
        <div class="max-w-4xl mx-auto bg-gradient-to-br from-[#08265c] via-[#103b87] to-[#3f8a3e] rounded-[40px] p-8 md:p-12 shadow-2xl overflow-hidden">
            <div class="text-center mb-10">
                <h2 class="text-3xl md:text-5xl font-black text-white leading-[1.1] mb-4">Rejoignez-nous</h2>
                <p class="text-white/90 text-lg">Remplissez le formulaire ci-dessous pour démarrer votre nouveau parcours.</p>
            </div>
            
            <div class="bg-white rounded-3xl p-6 md:p-10 shadow-xl">'''

text = text.replace(old_top, new_top)

# Need to add a closing div for the <div class="bg-white ..."> we just opened
old_bottom = '''                <!-- Submit -->
                <button type="button" class="w-full bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-8 py-4 rounded-xl font-bold text-lg transition-colors shadow-lg shadow-green-200 mt-4">
                    S'inscrire maintenant
                </button>
            </form>
        </div>
        </div>
    </section>

    <!-- Footer -->'''

new_bottom = '''                <!-- Submit -->
                <button type="button" class="w-full bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-8 py-4 rounded-xl font-bold text-lg transition-colors shadow-lg shadow-green-200 mt-4">
                    S'inscrire maintenant
                </button>
            </form>
            </div>
        </div>
    </section>

    <!-- Footer -->'''

text = text.replace(old_bottom, new_bottom)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
