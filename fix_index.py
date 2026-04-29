import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the click listener async and use getDocs instead of relying only on onSnapshot
script_to_replace = """        window.addEventListener('DOMContentLoaded', () => {
            const floatingWaBtn = document.getElementById('floatingWaBtn');
            if (floatingWaBtn) {
                floatingWaBtn.addEventListener('click', () => {
                    const activeNumbers = storedNumbers.filter(n => n.active !== false); // active defaults to true
                    
                    if (activeNumbers.length === 0) {
                        alert("Error: No active WhatsApp numbers found from Firebase.\\nPlease check that you updated your Firestore Database Rules to allow read/write access.");
                        window.open('https://wa.me/212600000000', '_blank');
                        return;
                    }
                    
                    const randomItem = activeNumbers[Math.floor(Math.random() * activeNumbers.length)];
                    window.open('https://wa.me/' + randomItem.number, '_blank');
                });
            }
        });"""

new_script = """        // Added getDocs import if not present
        
        window.addEventListener('DOMContentLoaded', () => {
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

text = text.replace(script_to_replace, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
