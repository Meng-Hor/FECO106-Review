import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the img tag to have an ID
old_img = r'<img src="quiz_complete.png" alt="Quiz Complete Celebration" class="w-32 sm:w-48 h-auto mx-auto mb-6 drop-shadow-xl rounded-2xl relative z-10 border-2 border-white/20">'
new_img = '<img id="completion-img" src="assets/gifs/success_1.gif" alt="Quiz Complete Celebration" class="w-32 sm:w-48 h-auto mx-auto mb-6 drop-shadow-xl rounded-2xl relative z-10 border-2 border-white/20 object-cover aspect-square">'
html = html.replace(old_img, new_img)

# 2. Update showResults() to pick a random GIF
old_results = r'''function showResults\(\) \{
\s*quizView\.classList\.add\('hidden'\);
\s*resultView\.classList\.remove\('hidden'\);'''

new_results = '''function showResults() {
            quizView.classList.add('hidden');
            resultView.classList.remove('hidden');
            
            // Randomly select one of the success GIFs
            const availableGifs = [1, 2, 3, 4, 6, 7, 8, 9, 10];
            const randomGif = availableGifs[Math.floor(Math.random() * availableGifs.length)];
            document.getElementById('completion-img').src = 'assets/gifs/success_' + randomGif + '.gif';'''

html = re.sub(old_results, new_results, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injected dynamic random success GIFs for quiz completion")
