with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

form_html = """
    <!-- Registration Form Section -->
    <section id="inscription" class="container mx-auto px-4 py-16 mb-16 bg-white overflow-hidden relative">
        <div class="max-w-3xl mx-auto bg-gray-50 rounded-3xl p-8 md:p-12 shadow-[0_0_40px_rgba(0,0,0,0.05)] border border-gray-100">
            <div class="text-center mb-10">
                <h2 class="text-3xl md:text-5xl font-black text-[#1f2937] leading-[1.1] mb-4">Rejoignez-nous</h2>
                <p class="text-gray-600">Remplissez le formulaire ci-dessous pour démarrer votre nouveau parcours.</p>
            </div>
            
            <form class="space-y-6">
                <!-- Full Name -->
                <div>
                    <label for="fullName" class="block text-sm font-semibold text-gray-700 mb-2">Nom complet</label>
                    <input type="text" id="fullName" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#3f8a3e] focus:ring-2 focus:ring-[#3f8a3e]/20 transition-colors bg-white outline-none" placeholder="Votre nom complet" required>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Email -->
                    <div>
                        <label for="email" class="block text-sm font-semibold text-gray-700 mb-2">Adresse e-mail</label>
                        <input type="email" id="email" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#3f8a3e] focus:ring-2 focus:ring-[#3f8a3e]/20 transition-colors bg-white outline-none" placeholder="votre@email.com" required>
                    </div>
                
                    <!-- WhatsApp Number -->
                    <div>
                        <label for="whatsapp" class="block text-sm font-semibold text-gray-700 mb-2">Numéro WhatsApp</label>
                        <input type="tel" id="whatsapp" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#3f8a3e] focus:ring-2 focus:ring-[#3f8a3e]/20 transition-colors bg-white outline-none" placeholder="+212 ..." required>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Age -->
                    <div>
                        <label for="age" class="block text-sm font-semibold text-gray-700 mb-2">Âge</label>
                        <input type="number" id="age" min="18" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#3f8a3e] focus:ring-2 focus:ring-[#3f8a3e]/20 transition-colors bg-white outline-none" placeholder="Votre âge" required>
                    </div>
                    
                    <!-- Job Type Dropdown -->
                    <div>
                        <label for="jobType" class="block text-sm font-semibold text-gray-700 mb-2">Recherchez-vous actuellement un :</label>
                        <select id="jobType" class="w-full px-4 py-3 rounded-xl border border-gray-200 focus:border-[#3f8a3e] focus:ring-2 focus:ring-[#3f8a3e]/20 transition-colors bg-white outline-none text-gray-700" required>
                            <option value="" disabled selected>Sélectionnez une option</option>
                            <option value="part-time">Emploi à temps partiel / 兼职工作</option>
                            <option value="full-time">Emploi à temps plein / 全职工作</option>
                        </select>
                    </div>
                </div>

                <!-- Checkbox 21 years old -->
                <div class="flex items-center gap-3 pt-2">
                    <input type="checkbox" id="over21" class="w-5 h-5 text-[#3f8a3e] border-gray-300 rounded focus:ring-[#3f8a3e] accent-[#3f8a3e]" required>
                    <label for="over21" class="text-sm font-medium text-gray-700 cursor-pointer">Je confirme avoir 21 ans ou plus (I am 21 years old or older)</label>
                </div>
                
                <!-- Submit -->
                <button type="button" class="w-full bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-8 py-4 rounded-xl font-bold text-lg transition-colors shadow-lg shadow-green-200 mt-4">
                    S'inscrire maintenant
                </button>
            </form>
        </div>
    </section>

    <!-- Footer -->"""

text = text.replace('    <!-- Footer -->', form_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
