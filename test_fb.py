import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the fallback logic in index.html to throw an alert
text = text.replace(
"""                    if (activeNumbers.length === 0) {
                        // Default fallback backup number if admin dashboard is empty/never used or Firebase is loading
                        window.open('https://wa.me/212600000000', '_blank');
                        return;
                    }""",
"""                    if (activeNumbers.length === 0) {
                        alert("Error: No active WhatsApp numbers found from Firebase.\\nPlease check that you updated your Firestore Database Rules to allow read/write access.");
                        window.open('https://wa.me/212600000000', '_blank');
                        return;
                    }""")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
