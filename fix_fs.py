import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# add a console.error if onSnapshot fails
content = content.replace(
"""        // Listen to numbers in real-time
        onSnapshot(collection(db, "whatsapp_numbers"), (snapshot) => {
            storedNumbers = [];
            snapshot.forEach((doc) => {
                storedNumbers.push({ id: doc.id, ...doc.data() });
            });
        });""",
"""        // Listen to numbers in real-time
        onSnapshot(collection(db, "whatsapp_numbers"), (snapshot) => {
            storedNumbers = [];
            snapshot.forEach((doc) => {
                storedNumbers.push({ id: doc.id, ...doc.data() });
            });
            console.log("Firebase numbers fetched:", storedNumbers);
        }, (error) => {
            console.error("Firebase permission or read error: ", error);
        });""")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
