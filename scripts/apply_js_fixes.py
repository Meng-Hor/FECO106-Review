import re

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. URL parsing fix
old_url = r"const setIndex = params\.get\('set'\);\s*if \(setIndex !== null && quizData\[setIndex\]\)"
new_url = '''const setIndex = params.get('set');
      const parsedIndex = parseInt(setIndex, 10);
      if (setIndex !== null && !Number.isNaN(parsedIndex) && parsedIndex >= 0 && parsedIndex < quizData.length && quizData[parsedIndex])'''
html = re.sub(old_url, new_url, html)
html = html.replace('currentSetIndex = setIndex;', 'currentSetIndex = parsedIndex;')

# 2. Timer clearInterval fixes
html = html.replace('function startQuiz(index) {', 'function startQuiz(index) {\n            if (timer) clearInterval(timer);')
html = html.replace('function cancelQuit() {', 'function cancelQuit() {\n              if (timer) clearInterval(timer);')
html = html.replace('timer = setInterval(updateTimer, 1000);', 'if (timer) clearInterval(timer);\n            timer = setInterval(updateTimer, 1000);')
html = html.replace('function showResults() {', 'function showResults() {\n              if(timer) clearInterval(timer);')

# 3. Add isGraded and isAnswered global variables
html = html.replace('let correctAnswers = 0;', 'let correctAnswers = 0;\n          let isGraded = false;\n          let isAnswered = false;')

# 4. Update loadQuestion to reset them and hide next button correctly
html = html.replace('function loadQuestion() {', 'function loadQuestion() {\n            isGraded = false;\n            isAnswered = false;\n            nextBtn.classList.add("hidden");\n            nextBtn.disabled = false;')

# 5. Fix strict equality and selectOption
old_select = r"const correctOpt = q\.correctOption;"
new_select = "const correctOpt = Number(q.correctOption);"
html = re.sub(old_select, new_select, html)

html = html.replace('function selectOption(selectedOpt) {', 'function selectOption(selectedOpt) {\n              if(isAnswered) return;\n              isAnswered = true;')

# 6. Fix showModelAnswer and self-grading
html = html.replace('function showModelAnswer() {', 'function showModelAnswer() {\n              if(isAnswered) return;\n              isAnswered = true;')

old_self_correct = r"document\.getElementById\('self-correct-btn'\)\.onclick = \(\) => \{"
new_self_correct = "document.getElementById('self-correct-btn').onclick = () => {\n              if(isGraded) return;\n              isGraded = true;"
html = re.sub(old_self_correct, new_self_correct, html)

old_self_wrong = r"document\.getElementById\('self-wrong-btn'\)\.onclick = \(\) => \{"
new_self_wrong = "document.getElementById('self-wrong-btn').onclick = () => {\n              if(isGraded) return;\n              isGraded = true;"
html = re.sub(old_self_wrong, new_self_wrong, html)

# 7. NextBtn click guard
old_next = r"nextBtn\.onclick = \(\) => \{"
new_next = "nextBtn.onclick = () => {\n              if(nextBtn.disabled) return;\n              nextBtn.disabled = true;"
html = re.sub(old_next, new_next, html)

# 8. Keyboard listener improvements
old_key = r"if \(quizView\.classList\.contains\('hidden'\)\) return;"
new_key = '''if (quizView.classList.contains('hidden')) return;
            const quitModal = document.getElementById('quit-modal');
            if (quitModal && !quitModal.classList.contains('hidden')) return;
            if (document.activeElement === oeAnswer && e.key !== 'Enter') return;
            if (e.isComposing) return;
'''
html = html.replace(old_key, new_key)

old_idx_check = r"if \(idx >= 0 && idx < 4\) \{"
new_idx_check = "if (idx >= 0 && idx < quizData[currentSetIndex].questions[currentQuestionIndex].options.length) {"
html = html.replace(old_idx_check, new_idx_check)


with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied strict Javascript logic fixes to quiz.html")
