import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up card-container
content = re.sub(r'/\* Notebook lined paper effect \*/.*?(?=/\* Overriding text colors \*/)', '', content, flags=re.DOTALL)

# 2. Add back the closing brace for card-container that might have been lost
content = content.replace('box-shadow: var(--water-shadow);\n    \n    ', 'box-shadow: var(--water-shadow);\n}\n\n')

# 3. Clean up headings
heading_replacement = """/* Headings */
h1, h2, h3, h4 {
    color: var(--primary-blue) !important;
    font-weight: 700;
    line-height: 1.3;
}

header h1, header p {
    padding: 0;
}"""
content = re.sub(r'/\* Headings \*/.*?(?=header p {)', heading_replacement + '\n', content, flags=re.DOTALL)
content = content.replace('header p {\n    color: var(--text-main) !important;\n}\n', 'header p {\n    color: var(--text-main) !important;\n}\n')


# 4. Clean up textarea
content = re.sub(r"font-family: 'Caveat', cursive; /\* Handwriting font for notes \*/\n    font-size: 1.4rem; /\* Larger for handwriting \*/", "", content)


with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Notebook theme removed.")
