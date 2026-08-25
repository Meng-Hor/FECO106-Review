import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add FontAwesome link
if 'font-awesome' not in content:
    content = content.replace(
        '<link rel="stylesheet" href="styles.css">',
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n    <link rel="stylesheet" href="styles.css">'
    )

# 2. Remove Neo-Brutalist elements
content = content.replace(
    '<div class="decor-wrapper">\n        <div class="decor-circle"></div>\n        <div class="decor-square"></div>\n        <div class="decor-triangle"></div>\n        <div class="max-w-4xl mx-auto px-4 py-8 relative z-10">',
    '<div class="max-w-4xl mx-auto px-4 py-8 relative z-10">'
)
content = content.replace('</div>\n</body>', '</body>')

# 3. Add icons to buttons in JS
content = content.replace(
    "`\n                    <h3 class=\"text-lg font-bold text-gray-800 group-hover:text-blue-600 mb-2\">${cleanName}</h3>`",
    "`\n                    <i class=\"fa-solid fa-gamepad text-indigo-500 mb-3 text-2xl group-hover:scale-110 transition-transform\"></i>\n                    <h3 class=\"text-lg font-bold text-gray-800 mb-2\">${cleanName}</h3>`"
)

content = content.replace(
    "`\n                        <span class=\"font-medium text-gray-800\">${pdf.name}</span>`",
    "`\n                        <div class=\"flex items-center\"><i class=\"fa-solid fa-file-pdf text-red-500 mr-3 text-xl\"></i><span class=\"font-medium text-gray-800\">${pdf.name}</span></div>`"
)

# 4. Add icons to HTML elements
# Header
content = content.replace('<h1 class="text-4xl font-bold text-blue-800 mb-2">FECO106 Mid-Term Review</h1>', '<h1 class="text-4xl font-bold text-indigo-900 mb-2"><i class="fa-solid fa-graduation-cap mr-3"></i>FECO106 Mid-Term Review</h1>')

# Dashboard Titles
content = content.replace('<h2 class="text-2xl font-semibold mb-6">Available Quiz Sets</h2>', '<h2 class="text-2xl font-semibold mb-6 text-indigo-900"><i class="fa-solid fa-layer-group mr-3"></i>Available Quiz Sets</h2>')
content = content.replace('<h2 class="text-2xl font-semibold mb-6">Study Materials (PDFs)</h2>', '<h2 class="text-2xl font-semibold mb-6 text-indigo-900 mt-10"><i class="fa-solid fa-book-open mr-3"></i>Study Materials (PDFs)</h2>')

# Quit / Next Buttons
content = content.replace('Quit Quiz</button>', '<i class="fa-solid fa-xmark mr-2"></i>Quit Quiz</button>')
content = content.replace('Next Question</button>', 'Next Question <i class="fa-solid fa-arrow-right ml-2"></i></button>')
content = content.replace('Submit Answer</button>', '<i class="fa-solid fa-paper-plane mr-2"></i>Submit Answer</button>')

# Back to Dashboard
content = content.replace('Back to Dashboard</button>', '<i class="fa-solid fa-house mr-2"></i>Back to Dashboard</button>')

# Timer
content = content.replace('<div class="text-gray-500 font-medium">Time left: <span id="time" class="font-bold"></span>s</div>', '<div class="text-gray-600 font-medium"><i class="fa-regular fa-clock mr-2"></i><span id="time" class="font-bold"></span>s</div>')

# Self Grade Buttons
content = content.replace('I Got It Right</button>', '<i class="fa-solid fa-check mr-2"></i>I Got It Right</button>')
content = content.replace('I Got It Wrong</button>', '<i class="fa-solid fa-xmark mr-2"></i>I Got It Wrong</button>')

# Fix the button color texts
content = content.replace('text-blue-800', 'text-indigo-900')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML structure updated for Glassmorphism!")
