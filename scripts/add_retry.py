import re

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace single home button with two side-by-side buttons
old_btn = '<button id="home-btn" class="btn-primary px-6 py-3 w-full max-w-xs mx-auto text-base rounded-xl relative z-10 shadow-lg transition-all"><i class="fa-solid fa-house mr-2"></i>Back to Dashboard</button>'
new_btns = '''<div class="flex flex-col sm:flex-row gap-3 max-w-xs mx-auto w-full relative z-10">
                  <button id="retry-btn" class="btn-secondary px-6 py-3 w-full text-base rounded-xl shadow-lg transition-all flex items-center justify-center gap-2"><i class="fa-solid fa-rotate-right"></i>Retry Quiz</button>
                  <button id="home-btn" class="btn-primary px-6 py-3 w-full text-base rounded-xl shadow-lg transition-all flex items-center justify-center gap-2"><i class="fa-solid fa-house"></i>Dashboard</button>
              </div>'''

html = html.replace(old_btn, new_btns)

# 2. Add retry button JS logic next to home-btn onclick
old_js = "document.getElementById('home-btn').onclick = () => window.location.href = 'index.html';"
new_js = """document.getElementById('home-btn').onclick = () => window.location.href = 'index.html';
          document.getElementById('retry-btn').onclick = () => {
              resultView.classList.add('hidden');
              startQuiz(currentSetIndex);
          };"""

html = html.replace(old_js, new_js)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added Retry Quiz button to result screen")
