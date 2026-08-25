import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# The block to remove
block_regex = r'\s*</div>\s*<h2 class="text-2xl font-semibold mb-6">Study Materials \(PDFs\)</h2>\s*<div id="pdf-container" class="grid gap-4 md:grid-cols-2">\s*<!-- Dynamically populated -->\s*</div>'

# We want to keep ONLY the first occurrence (which is in the dashboard)
parts = re.split(block_regex, content)
if len(parts) > 1:
    # First part + block + all remaining parts joined by just </div>
    new_content = parts[0] + '\n            </div>\n            \n            <h2 class="text-2xl font-semibold mb-6">Study Materials (PDFs)</h2>\n            <div id="pdf-container" class="grid gap-4 md:grid-cols-2">\n                <!-- Dynamically populated -->\n            </div>' 
    
    for i in range(1, len(parts)):
        new_content += parts[i]
        if i < len(parts) - 1:
            new_content += '\n            </div>' # Add back the </div> that was matched but strip the Study Materials
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Duplicates removed.")
else:
    print("No duplicates found.")
