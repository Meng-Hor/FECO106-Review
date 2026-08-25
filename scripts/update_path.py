import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the PDF paths in the pdfData array
content = re.sub(
    r'"path": "(.*?\.pdf)"',
    r'"path": "material/\1"',
    content
)

# Avoid double-prepending if it was already updated or ran twice
content = content.replace('material/material/', 'material/')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated PDF links to point to the material folder.")
