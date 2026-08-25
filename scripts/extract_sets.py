import json
import os
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
sets_dir = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\sets'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract quizData
match = re.search(r'const quizData = (\[.*?\]);\s*const pdfData', content, re.DOTALL)
if not match:
    print("Could not find quizData")
    exit()

quiz_data = json.loads(match.group(1))

os.makedirs(sets_dir, exist_ok=True)

script_tags = "<script>\n        window.quizData = [];\n    </script>\n"

for s in quiz_data:
    set_name = s['set']
    # Create folder for the set
    set_folder = os.path.join(sets_dir, set_name)
    os.makedirs(set_folder, exist_ok=True)
    
    # Create data.js inside the folder
    set_file = os.path.join(set_folder, 'data.js')
    
    js_content = f"window.quizData.push({json.dumps(s, indent=4)});"
    with open(set_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    script_tags += f'    <script src="sets/{set_name}/data.js"></script>\n'

# Replace quizData in index.html
new_content = content[:match.start()] + script_tags + "    const pdfData" + content[match.end():]

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Extraction complete!")
