import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the Floating Chat Icon area
chatbox_html = """
        <!-- Chatbox Form Container -->
        <div id="waChatbox" class="fixed bottom-28 right-8 w-80 md:w-96 bg-white rounded-2xl shadow-2xl z-50 hidden flex-col overflow-hidden border border-gray-100">
            <div class="bg-[#08265c] text-white p-4 flex justify-between items-center rounded-t-2xl">
                <div>
                    <h4 class="font-bold text-lg">Discutons-en</h4>
                    <p class="text-xs text-blue-100 opacity-90">Veuillez remplir pour commencer</p>
                </div>
                <button id="closeWaChatbox" class="text-white hover:text-gray-300 focus:outline-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
            
            <div class="p-5 max-h-[60vh] overflow-y-auto">
                <form id="chatRegForm" class="space-y-4">
                    <div>
                        <label class="block text-xs font-semibold text-gray-700 mb-1">Nom complet</label>
                        <input type="text" name="fullName" class="w-full px-3 py-2 text-sm rounded-lg border border-gray-200 focus:border-[#3f8a3e] focus:ring-1 focus:ring-[#3f8a3e] outline-none" placeholder="Votre nom" required>
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-gray-700 mb-1">Adresse e-mail</label>
                        <input type="email" name="email" class="w-full px-3 py-2 text-sm rounded-lg border border-gray-200 focus:border-[#3f8a3e] focus:ring-1 focus:ring-[#3f8a3e] outline-none" placeholder="votre@email.com" required>
                    </div>
                    <div>
                        <label class="block text-xs font-semibold text-gray-700 mb-1">Numéro WhatsApp</label>
                        <input type="tel" name="whatsapp" class="w-full px-3 py-2 text-sm rounded-lg border border-gray-200 focus:border-[#3f8a3e] focus:ring-1 focus:ring-[#3f8a3e] outline-none" placeholder="+212 ..." required>
                    </div>
                    <div class="grid grid-cols-2 gap-3">
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1">Âge</label>
                            <input type="number" name="age" min="18" class="w-full px-3 py-2 text-sm rounded-lg border border-gray-200 focus:border-[#3f8a3e] focus:ring-1 focus:ring-[#3f8a3e] outline-none" placeholder="Âge" required>
                        </div>
                        <div>
                            <label class="block text-xs font-semibold text-gray-700 mb-1">Emploi</label>
                            <select name="jobType" class="w-full px-3 py-2 text-sm rounded-lg border border-gray-200 focus:border-[#3f8a3e] focus:ring-1 focus:ring-[#3f8a3e] outline-none" required>
                                <option value="" disabled selected>Option</option>
                                <option value="part-time">Temps partiel</option>
                                <option value="full-time">Temps plein</option>
                            </select>
                        </div>
                    </div>
                    <div class="flex items-start gap-2 pt-1">
                        <input type="checkbox" name="over21" value="Oui" class="mt-1 w-4 h-4 text-[#3f8a3e] border-gray-300 rounded focus:ring-[#3f8a3e]" required>
                        <label class="text-xs text-gray-600 leading-tight">Je confirme avoir 21 ans ou plus.</label>
                    </div>
                    
                    <button type="submit" id="chatSubmitBtn" class="w-full bg-[#3f8a3e] hover:bg-[#2e682d] text-white px-4 py-3 rounded-xl font-bold text-sm transition-colors shadow-md mt-2">
                        Démarrer la discussion
                    </button>
                    <div id="chatFormMessage" class="hidden text-center text-xs font-bold mt-2 p-2 rounded-lg"></div>
                </form>
            </div>
        </div>

        <!-- Floating Chat Icon -->"""

text = text.replace('        <!-- Floating Chat Icon -->', chatbox_html)

# 2. Modify the old floatingWaBtn listener in the main script area
old_listener = """        window.addEventListener('DOMContentLoaded', () => {
            const floatingWaBtn = document.getElementById('floatingWaBtn');
            if (floatingWaBtn) {
                floatingWaBtn.addEventListener('click', async () => {
                    // Try fetching numbers directly on click
                    try {
                        const { getDocs } = await import("https://www.gstatic.com/firebasejs/10.11.0/firebase-firestore.js");
                        const querySnapshot = await getDocs(collection(db, "whatsapp_numbers"));
                        
                        let currentNumbers = [];
                        querySnapshot.forEach((doc) => {
                            currentNumbers.push({ id: doc.id, ...doc.data() });
                        });
                        
                        const activeNumbers = currentNumbers.filter(n => n.active !== false);
                        
                        if (activeNumbers.length === 0) {
                            alert("Database connected, but no ACTIVE numbers were found in 'whatsapp_numbers' collection.\\nMake sure you added numbers in the Admin Panel and checked 'Active'.");
                            window.open('https://wa.me/212600000000', '_blank');
                            return;
                        }
                        
                        const randomItem = activeNumbers[Math.floor(Math.random() * activeNumbers.length)];
                        window.open('https://wa.me/' + randomItem.number, '_blank');
                    } catch (error) {
                        alert("Firebase connection error: " + error.message);
                        window.open('https://wa.me/212600000000', '_blank');
                    }
                });
            }
        });"""

new_listener = """        window.addEventListener('DOMContentLoaded', () => {
            const floatingWaBtn = document.getElementById('floatingWaBtn');
            const waChatbox = document.getElementById('waChatbox');
            const closeWaChatbox = document.getElementById('closeWaChatbox');
            
            if (floatingWaBtn && waChatbox) {
                floatingWaBtn.addEventListener('click', () => {
                    waChatbox.classList.toggle('hidden');
                    waChatbox.classList.toggle('flex');
                });
                
                closeWaChatbox.addEventListener('click', () => {
                    waChatbox.classList.add('hidden');
                    waChatbox.classList.remove('flex');
                });
            }
        });"""

text = text.replace(old_listener, new_listener)

# 3. Add JS handler for #chatRegForm right after the #regForm handler logic
# We look for the closing script tag for the #regForm handler.
# Wait, let's see how much we can just use the DOM elements via the module.
# Let's add the submission logic for `#chatRegForm` to the module script.

old_script_start = """                document.getElementById("regForm").addEventListener("submit", function(e) {"""

new_script_start = """                
                // Chatbox Registration Form Logic
                const chatForm = document.getElementById("chatRegForm");
                if (chatForm) {
                    chatForm.addEventListener("submit", function(e) {
                        e.preventDefault();
                        
                        const btn = document.getElementById("chatSubmitBtn");
                        const msg = document.getElementById("chatFormMessage");
                        btn.innerText = "Envoi...";
                        btn.disabled = true;

                        const scriptURL = "https://script.google.com/macros/s/AKfycbzsgFw8Jb3_8ezdpJMYSDI11kVTn8MjHJNMrZOp902ZZ-82za9P5eaz1mKMoTdKOp-1/exec";
                        const formData = new FormData(this);
                        
                        fetch(scriptURL, { method: "POST", body: formData })
                            .then(async response => {
                                msg.innerText = "Redirection WhatsApp...";
                                msg.classList.remove("hidden", "bg-red-100", "text-red-700");
                                msg.classList.add("bg-green-100", "text-green-700");
                                
                                try {
                                    const querySnapshot = await getDocs(collection(db, "whatsapp_numbers"));
                                    let currentNumbers = [];
                                    querySnapshot.forEach((doc) => { currentNumbers.push({ id: doc.id, ...doc.data() }); });
                                    
                                    const activeNumbers = currentNumbers.filter(n => n.active !== false);
                                    let targetNumber = "212600000000";
                                    if (activeNumbers.length > 0) {
                                        targetNumber = activeNumbers[Math.floor(Math.random() * activeNumbers.length)].number;
                                    }

                                    const waMessage = `Recrute Maroc Application FORM\\n\\nName: ${formData.get("fullName") || ""}\\nEmail: ${formData.get("email") || ""}\\nWhatsapp Number: ${formData.get("whatsapp") || ""}\\nAge: ${formData.get("age") || ""}\\nFulltime/Partime: ${formData.get("jobType") || ""}\\n21 Years old or above: ${formData.get("over21") ? "Yes" : "No"}`;
                                    
                                    window.open('https://wa.me/' + targetNumber + '?text=' + encodeURIComponent(waMessage), '_blank');
                                } catch (err) {
                                    const fallbackMsg = `Recrute Maroc Application FORM\\n\\nName: ${formData.get("fullName") || ""}\\nEmail: ${formData.get("email") || ""}\\nWhatsapp Number: ${formData.get("whatsapp") || ""}\\nAge: ${formData.get("age") || ""}\\nFulltime/Partime: ${formData.get("jobType") || ""}\\n21 Years old or above: ${formData.get("over21") ? "Yes" : "No"}`;
                                    window.open('https://wa.me/212600000000?text=' + encodeURIComponent(fallbackMsg), '_blank');
                                }

                                this.reset();
                                btn.innerText = "Démarrer la discussion";
                                btn.disabled = false;
                                document.getElementById('waChatbox').classList.add('hidden');
                                document.getElementById('waChatbox').classList.remove('flex');
                            })
                            .catch(error => {
                                msg.innerText = "Erreur. Veuillez réessayer.";
                                msg.classList.remove("hidden", "bg-green-100", "text-green-700");
                                msg.classList.add("bg-red-100", "text-red-700");
                                btn.innerText = "Démarrer la discussion";
                                btn.disabled = false;
                            });
                    });
                }

                document.getElementById("regForm").addEventListener("submit", function(e) {"""

text = text.replace(old_script_start, new_script_start)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done")
