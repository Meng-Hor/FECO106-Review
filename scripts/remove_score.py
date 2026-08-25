import os
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Score display from header
content = re.sub(
    r'<div class="text-right">\s*<p class="text-sm text-gray-500">Score</p>\s*<p id="current-score" class="text-xl font-bold text-blue-600">0</p>\s*</div>',
    '',
    content
)

# 2. Remove Final Score display from results
content = re.sub(
    r'<div class="mb-8">\s*<p class="text-gray-600 mb-2 text-lg">Your final score</p>\s*<p id="final-score" class="text-5xl font-bold text-blue-600 drop-shadow-sm">0</p>\s*</div>',
    '',
    content
)

# 3. Remove score logic from self-correct
content = re.sub(
    r'const points = parseInt\(q\.points\) \|\| 1000;\s*const maxTime = parseInt\(q\.timeLimit\) \|\| 30;\s*const timeBonus = Math\.floor\(points \* \(Math\.max\(0, timeLeft\) / maxTime\) \* 0\.5\);\s*score \+= points \+ timeBonus;\s*correctAnswers\+\+;\s*scoreEl\.textContent = score;',
    'correctAnswers++;',
    content
)

# 4. Remove score logic from multiple choice correct
content = re.sub(
    r'correctAnswers\+\+;\s*const maxTime = parseInt\(q\.timeLimit\) \|\| 30;\s*const timeBonus = Math\.floor\(points \* \(timeLeft / maxTime\) \* 0\.5\);\s*score \+= points \+ timeBonus;\s*scoreEl\.textContent = score;',
    'correctAnswers++;',
    content
)

# 5. Remove final score update
content = re.sub(
    r'document\.getElementById\(\'final-score\'\)\.textContent = score;',
    '',
    content
)

# 6. Remove scoreEl update in loadQuestion
content = re.sub(
    r'scoreEl\.textContent = score;',
    '',
    content
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Score system removed successfully.")
