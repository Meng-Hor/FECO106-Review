import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the Quit Quiz button duplicates
html = html.replace('class="px-4 py-2 btn-danger px-4 py-2"', 'class="btn-danger px-6 py-3"')

# Fix the Next Question button
html = html.replace('class="btn-primary hidden"', 'class="btn-primary px-6 py-3 hidden"')

# Fix Submit Answer Button
html = html.replace('class="btn-primary w-full"', 'class="btn-primary px-6 py-3 w-full"')

# Fix Self-Grading Buttons
html = html.replace('class="btn-primary"', 'class="btn-primary px-6 py-3"')
# Wait, this might affect Next Question if it's not hidden, but let's be careful.
# The exact string for I Got It Right is: <button class="btn-primary" onclick="gradeSelf(true)">
html = html.replace('class="btn-primary" onclick="gradeSelf(true)"', 'class="btn-primary px-6 py-3" onclick="gradeSelf(true)"')
html = html.replace('class="btn-danger" onclick="gradeSelf(false)"', 'class="btn-danger px-6 py-3" onclick="gradeSelf(false)"')

# Fix Modal Buttons
html = html.replace('class="btn-danger w-full py-3"', 'class="btn-danger px-6 py-3 w-full"')
html = html.replace('class="btn-secondary w-full py-3"', 'class="btn-secondary px-6 py-3 w-full"')


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added safe padding classes to all buttons")
