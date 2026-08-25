import re

css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the universal font family
replacement = """* {
    font-family: 'Inter', sans-serif;
}

h1, h2, h3, h4 {
    font-family: 'Outfit', sans-serif;
}

.btn-primary, .btn-secondary, .btn-danger, .option-btn, textarea, #time, #score-display {
    font-family: 'JetBrains Mono', monospace;
}
"""

content = re.sub(r'\* \{\s*font-family: \'JetBrains Mono\', monospace;\s*\}', replacement, content)

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Typography updated!")
