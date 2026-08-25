import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace inline styles with link
content = re.sub(
    r'<style>.*?</style>',
    '<link rel="stylesheet" href="styles.css">',
    content,
    flags=re.DOTALL
)

# 2. Update body classes
content = content.replace('<body class="bg-gray-50 text-gray-900 min-h-screen p-4 md:p-8">', '<body class="min-h-screen p-4 md:p-8">')

# 3. Add decorative wrapper
content = content.replace(
    '<div class="max-w-4xl mx-auto">',
    '<div class="decor-wrapper">\n        <div class="decor-circle"></div>\n        <div class="decor-square"></div>\n        <div class="decor-triangle"></div>\n        <div class="max-w-4xl mx-auto relative z-10">'
)

# Close the wrapper before scripts
content = content.replace(
    '    <script>',
    '        </div>\n    </div>\n\n    <script>'
)

# 4. Update Cards
content = content.replace('bg-white rounded-xl shadow-lg', 'card-container')

# 5. Update Buttons
content = content.replace('bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-md', 'btn-primary px-8 py-3')
content = content.replace('text-red-600 hover:bg-red-50 rounded-lg transition-colors font-medium', 'btn-danger px-4 py-2')
content = content.replace('bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors font-medium', 'btn-primary w-full p-3 mt-4')
content = content.replace('bg-green-500 text-white rounded-lg hover:bg-green-600 font-medium', 'btn-primary bg-green-500 px-6 py-2')
content = content.replace('bg-red-500 text-white rounded-lg hover:bg-red-600 font-medium', 'btn-primary bg-red-500 px-6 py-2')

# 6. Update JS generated buttons
content = content.replace(
    "btn.className = 'bg-white border rounded-lg hover:shadow-md transition-shadow group p-4 text-left';",
    "btn.className = 'btn-secondary group p-4 text-left';"
)
content = content.replace(
    "link.className = 'bg-white border rounded-lg hover:shadow-md transition-shadow group p-4 flex items-center justify-between';",
    "link.className = 'btn-secondary group p-4 flex items-center justify-between';"
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Theme applied successfully!")
