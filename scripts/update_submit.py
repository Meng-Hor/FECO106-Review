import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change button text
content = content.replace('Reveal Answer', 'Submit Answer')

# 2. Update keyboard logic to use Enter (without Shift) instead of Ctrl+Enter
content = content.replace(
    "if (e.key === 'Enter' && (e.ctrlKey || e.shiftKey || !isTyping)) {",
    "if (e.key === 'Enter' && !e.shiftKey) {"
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Button text and shortcut updated!")
