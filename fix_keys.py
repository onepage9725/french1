import re

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract the config block
match = re.search(r'(const firebaseConfig = \{.*?\};)', index_content, re.DOTALL)
if match:
    config_block = match.group(1)
    
    with open('admin.html', 'r', encoding='utf-8') as f:
        admin_content = f.read()
        
    admin_content = re.sub(r'const firebaseConfig = \{.*?\};', config_block, admin_content, flags=re.DOTALL)
    
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(admin_content)
    print("Fixed admin.html keys!")
else:
    print("Could not find keys in index.html")
