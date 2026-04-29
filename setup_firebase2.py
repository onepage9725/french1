import re

print("Processing admin.html...")
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_content = f.read()

admin_firebase_script = """    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-app.js";
        import { getFirestore, collection, addDoc, updateDoc, deleteDoc, doc, onSnapshot } from "https://www.gstatic.com/firebasejs/10.11.0/firebase-firestore.js";

        // TODO: Replace with your Firebase config
        const firebaseConfig = {
            apiKey: "YOUR_API_KEY",
            authDomain: "YOUR_AUTH_DOMAIN",
            projectId: "YOUR_PROJECT_ID",
            storageBucket: "YOUR_STORAGE_BUCKET",
            messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
            appId: "YOUR_APP_ID"
        };

        const app = initializeApp(firebaseConfig);
        const db = getFirestore(app);
        const numbersCol = collection(db, "whatsapp_numbers");

        let waNumbers = [];
        
        const tableBody = document.getElementById('numbersTableBody');
        const emptyState = document.getElementById('emptyState');
        const countEl = document.getElementById('count');
        const addForm = document.getElementById('addForm');
        
        const editModal = document.getElementById('editModal');
        const editIdInput = document.getElementById('editId');
        const editNameInput = document.getElementById('editName');
        const editNumberInput = document.getElementById('editNumber');
        const editActiveInput = document.getElementById('editActive');
        const saveEditBtn = document.getElementById('saveEdit');
        const cancelEditBtn = document.getElementById('cancelEdit');
        const testBtn = document.getElementById('testRandomBtn');

        // Real-time listener for Firestore
        onSnapshot(numbersCol, (snapshot) => {
            waNumbers = [];
            snapshot.forEach((docSnap) => {
                waNumbers.push({
                    id: docSnap.id,
                    ...docSnap.data()
                });
            });
            renderTable();
        });

        function renderTable() {
            tableBody.innerHTML = '';
            countEl.innerText = waNumbers.length;
            
            if (waNumbers.length === 0) {
                emptyState.classList.remove('hidden');
                tableBody.parentElement.classList.add('hidden');
                return;
            }
            
            emptyState.classList.add('hidden');
            tableBody.parentElement.classList.remove('hidden');

            waNumbers.forEach((item, index) => {
                const tr = document.createElement('tr');
                tr.className = "border-b border-gray-50 hover:bg-gray-50 transition-colors";
                
                const activeBadge = item.active !== false 
                    ? `<span class="bg-green-100 text-green-700 px-2 py-1 rounded-full text-xs font-bold">Active</span>`
                    : `<span class="bg-gray-100 text-gray-600 px-2 py-1 rounded-full text-xs font-bold">Inactive</span>`;

                tr.innerHTML = `
                    <td class="py-4 px-4 font-semibold text-gray-900">${item.name || 'No Name'}</td>
                    <td class="py-4 px-4 text-[#3f8a3e] font-mono tracking-wider">${item.number}</td>
                    <td class="py-4 px-4">${activeBadge}</td>
                    <td class="py-4 px-4 text-right flex justify-end gap-2">
                        <button class="edit-btn text-blue-500 hover:text-blue-700 p-2 bg-blue-50 rounded-lg transition-colors" title="Edit" data-id="${item.id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"></path></svg>
                        </button>
                        <button class="delete-btn text-red-500 hover:text-red-700 p-2 bg-red-50 rounded-lg transition-colors" title="Delete" data-id="${item.id}">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                        </button>
                    </td>
                `;
                tableBody.appendChild(tr);
            });

            document.querySelectorAll('.edit-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    editNumber(e.currentTarget.getAttribute('data-id'));
                });
            });
            document.querySelectorAll('.delete-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    deleteNumber(e.currentTarget.getAttribute('data-id'));
                });
            });
        }

        // Add
        addForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            if (waNumbers.length >= 20) {
                alert("You have reached the limit of 20 numbers.");
                return;
            }
            
            const name = document.getElementById('waName').value.trim();
            const number = document.getElementById('waNumber').value.trim().replace(/\\D/g, ''); 
            
            if (number.length < 5) {
                alert("Please enter a valid number with country code (e.g: 212600000000)");
                return;
            }
            
            try {
                await addDoc(numbersCol, { name, number, active: true });
                document.getElementById('waName').value = '';
                document.getElementById('waNumber').value = '';
            } catch (err) {
                console.error("Error adding doc:", err);
                alert("Failed to add number. Check console.");
            }
        });

        // Edit
        function editNumber(id) {
            const item = waNumbers.find(n => n.id === id);
            if (!item) return;
            
            editIdInput.value = id;
            editNameInput.value = item.name;
            editNumberInput.value = item.number;
            editActiveInput.checked = item.active !== false;
            editModal.classList.remove('hidden');
        }

        saveEditBtn.addEventListener('click', async () => {
            const id = editIdInput.value;
            const itemRef = doc(db, "whatsapp_numbers", id);
            try {
                await updateDoc(itemRef, {
                    name: editNameInput.value.trim(),
                    number: editNumberInput.value.trim().replace(/\\D/g, ''),
                    active: editActiveInput.checked
                });
                editModal.classList.add('hidden');
            } catch (err) {
                console.error("Error updating doc:", err);
                alert("Failed to update.");
            }
        });

        cancelEditBtn.addEventListener('click', () => {
            editModal.classList.add('hidden');
        });

        // Delete
        function deleteNumber(id) {
            if (confirm("Are you sure you want to delete this number?")) {
                const itemRef = doc(db, "whatsapp_numbers", id);
                deleteDoc(itemRef).catch(err => {
                    console.error("Error deleting doc:", err);
                    alert("Failed to delete.");
                });
            }
        }

        // Test
        testBtn.addEventListener('click', () => {
            const activeNumbers = waNumbers.filter(n => n.active !== false);
            if (activeNumbers.length === 0) {
                alert("No active numbers to choose from!");
                return;
            }
            const randomItem = activeNumbers[Math.floor(Math.random() * activeNumbers.length)];
            alert(`Simulation: System picked -> ${randomItem.name} (${randomItem.number})\\n\\nRedirecting to WhatsApp...`);
            window.open('https://wa.me/' + randomItem.number, '_blank');
        });
    </script>"""

# Find the start of the inline script (which falls after the "</div>\n    </div>\n")
# and substitute it fully. Let's just string split manually.
parts = admin_content.split('<script>')
if len(parts) > 1:
    admin_content = parts[0] + admin_firebase_script + "\n</body>\n</html>"

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(admin_content)

print("Done admin replacing.")
