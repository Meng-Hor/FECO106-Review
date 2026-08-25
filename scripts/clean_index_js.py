import re

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove dead DOM elements
dead_code_pattern = r"const quizView = document\.getElementById\('quiz-view'\);\s*const resultView = document\.getElementById\('result-view'\);\s*const setsContainer = document\.getElementById\('quiz-sets-container'\);\s*const pdfContainer = document\.getElementById\('pdf-container'\);\s*const setTitle = document\.getElementById\('current-set-title'\);\s*const qNum = document\.getElementById\('current-question-num'\);\s*const totalQ = document\.getElementById\('total-questions'\);\s*const timeEl = document\.getElementById\('time-left'\);\s*const qText = document\.getElementById\('question-text'\);\s*const optionsContainer = document\.getElementById\('options-container'\);\s*const openEndedContainer = document\.getElementById\('open-ended-container'\);\s*const oeAnswer = document\.getElementById\('open-ended-answer'\);\s*const revealBtn = document\.getElementById\('reveal-btn'\);\s*const answerFeedback = document\.getElementById\('answer-feedback'\);\s*const modelAnswerText = document\.getElementById\('model-answer-text'\);\s*const nextBtn = document\.getElementById\('next-btn'\);\s*const quitBtn = document\.getElementById\('quit-btn'\);"

# We must keep setsContainer and pdfContainer !
replacement = '''const setsContainer = document.getElementById('quiz-sets-container');
    const pdfContainer = document.getElementById('pdf-container');'''

html = re.sub(dead_code_pattern, replacement, html, flags=re.MULTILINE)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleaned index.html JS")
