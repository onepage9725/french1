import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to extract imports and move them to the top of the script tag.
# Also fix the stray braces

script_pattern = re.compile(r'(<script type="module">)(.*?)(</script>)', re.DOTALL)
match = script_pattern.search(text)
if match:
    script_content = match.group(2)
    
    # 1. remove stray braces that were mistakenly left behind:
    # "            }\n        });\n\n        mobileLinks" -> "        mobileLinks"
    script_content = script_content.replace("            }\n        });\n\n        mobileLinks", "        mobileLinks")
    
    # 2. Extract imports
    imports = []
    def replacer(m):
        imports.append(m.group(0))
        return ""
    
    script_content = re.sub(r'^\s*import\s+.*?;', replacer, script_content, flags=re.MULTILINE)
    
    final_script_content = "\n" + "\n".join(imports) + "\n" + script_content
    
    new_text = text[:match.start()] + match.group(1) + final_script_content + match.group(3) + text[match.end():]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Fixed formatting!")
else:
    print("Could not find module script")
