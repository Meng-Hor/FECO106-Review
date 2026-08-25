import re

quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_results = r'''const availableGifs = \[.*?\];
\s*const randomGif = availableGifs\[Math\.floor\(Math\.random\(\) \* availableGifs\.length\)\];
\s*document\.getElementById\('completion-img'\)\.src = 'assets/gifs/success_' \+ randomGif \+ '\.gif';'''

new_results = '''const availableGifs = ['assets/gifs/success_1.gif', 'assets/gifs/success_11.gif', 'assets/gifs/success_12.gif', 'assets/gifs/success_14.gif', 'assets/gifs/success_17.gif', 'assets/gifs/success_19.gif', 'assets/gifs/success_2.gif', 'assets/gifs/success_20.gif', 'assets/gifs/success_21.gif', 'assets/gifs/success_3.gif', 'assets/gifs/success_4.gif', 'assets/gifs/success_8.gif', 'assets/gifs/success_9.gif', 'assets/gifs/yesno_0.gif', 'assets/gifs/yesno_1.gif', 'assets/gifs/yesno_2.gif', 'assets/gifs/yesno_3.gif'];
            const randomGifPath = availableGifs[Math.floor(Math.random() * availableGifs.length)];
            document.getElementById('completion-img').src = randomGifPath;'''

html = re.sub(old_results, new_results, html)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Javascript to use exact paths of all valid GIFs")
