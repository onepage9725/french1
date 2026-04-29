import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add standard form ID and update names
text = text.replace('<form class="space-y-6">', '<form id="regForm" class="space-y-6">')
text = text.replace('id="fullName" class="', 'id="fullName" name="fullName" class="')
text = text.replace('id="email" class="', 'id="email" name="email" class="')
text = text.replace('id="whatsapp" class="', 'id="whatsapp" name="whatsapp" class="')
text = text.replace('id="age" min="18" class="', 'id="age" name="age" min="18" class="')
text = text.replace('id="jobType" class="', 'id="jobType" name="jobType" class="')
text = text.replace('id="over21" class="', 'id="over21" name="over21" value="Oui" class="')

# Change button type to submit
text = text.replace('<button type="button" class="w-full bg-[#3f8a3e]', '<button type="submit" class="w-full bg-[#3f8a3e]')

# Add the frontend JS handler before the closing script / form section
js_handler = """                <button type="submit" class="w-full bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-8 py-4 rounded-xl font-bold text-lg transition-colors shadow-lg shadow-green-200 mt-4" id="submitBtn">
                    S'inscrire maintenant
                </button>
                <div id="formMessage" class="hidden text-center font-bold mt-4 p-4 rounded-xl"></div>
            </form>

            <script>
                document.getElementById("regForm").addEventListener("submit", function(e) {
                    e.preventDefault();
                    
                    const btn = document.getElementById("submitBtn");
                    const msg = document.getElementById("formMessage");
                    btn.innerText = "Envoi en cours...";
                    btn.disabled = true;

                    // REMPLACEZ L'URL CI-DESSOUS PAR VOTRE PROPRE URL GOOGLE APPS SCRIPT
                    const scriptURL = "VOTRE_URL_GOOGLE_APPS_SCRIPT_ICI";
                    
                    const formData = new FormData(this);
                    
                    fetch(scriptURL, { method: "POST", body: formData })
                        .then(response => {
                            msg.innerText = "Inscription réussie ! Nous vous contacterons bientôt.";
                            msg.classList.remove("hidden", "bg-red-100", "text-red-700");
                            msg.classList.add("bg-green-100", "text-green-700");
                            this.reset();
                            btn.innerText = "S'inscrire maintenant";
                            btn.disabled = false;
                        })
                        .catch(error => {
                            msg.innerText = "Une erreur s'est produite. Veuillez réessayer.";
                            msg.classList.remove("hidden", "bg-green-100", "text-green-700");
                            msg.classList.add("bg-red-100", "text-red-700");
                            btn.innerText = "S'inscrire maintenant";
                            btn.disabled = false;
                        });
                });
            </script>"""

text = re.sub(r'<button type="submit" class="w-full bg-\[#3f8a3e\](.*?)S\'inscrire maintenant\n                </button>\n            </form>', js_handler, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
