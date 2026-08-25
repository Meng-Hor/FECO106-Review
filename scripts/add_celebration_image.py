import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Insert the image into the result view
old_result = r'<div id="result-view" class="hidden card-container p-8 text-center">\s*<h2 class="text-3xl font-bold mb-4 text-gray-800">Quiz Completed!</h2>'
new_result = r'''<div id="result-view" class="hidden card-container p-8 text-center">
            <img src="quiz_complete.png" alt="Quiz Complete Celebration" class="w-48 h-auto mx-auto mb-6 drop-shadow-md">
            <h2 class="text-3xl font-bold mb-4 text-gray-800">Quiz Completed!</h2>'''
html = re.sub(old_result, new_result, html)

# While I'm here, I see in the HTML that the Back to Dashboard button has duplicate padding classes:
# <button id="home-btn" class="px-8 py-3 btn-primary px-8 py-3">
# I'll clean that up quickly.
html = html.replace('class="px-8 py-3 btn-primary px-8 py-3"', 'class="btn-primary w-full max-w-sm mx-auto"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added quiz_complete.png to the completion screen")
