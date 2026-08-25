import re

path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Reduce options-container gap on mobile
html = html.replace(
    'id="options-container" class="grid gap-4"',
    'id="options-container" class="grid gap-2 sm:gap-4"'
)

# 2. Shrink timer ring on mobile (w-16 h-16 -> w-12 h-12 on mobile)
html = html.replace(
    'class="w-16 h-16 rounded-full border-4 border-blue-500 flex items-center justify-center relative transition-colors duration-300"',
    'class="w-12 h-12 sm:w-16 sm:h-16 rounded-full border-4 border-blue-500 flex items-center justify-center relative transition-colors duration-300"'
)

# 3. Shrink timer text on mobile
html = html.replace(
    '<span id="time-left" class="text-xl font-bold">20</span>',
    '<span id="time-left" class="text-base sm:text-xl font-bold">20</span>'
)

# 4. Reduce question text size & margin on mobile
html = html.replace(
    'id="question-text" class="text-xl sm:text-2xl font-semibold mb-6"',
    'id="question-text" class="text-base sm:text-xl font-semibold mb-3 sm:mb-6"'
)

# 5. Reduce card padding on mobile (quiz view wrapper)
html = html.replace(
    'class="card-container p-4 sm:p-6 mb-6 relative"',
    'class="card-container p-3 sm:p-6 mb-4 sm:mb-6 relative"'
)

# 6. Reduce top header section gap on mobile
html = html.replace(
    'class="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4 mb-4 sm:mb-6 border-b pb-4"',
    'class="flex flex-row justify-between items-center gap-2 mb-3 sm:mb-6 border-b pb-3 sm:pb-4"'
)

# 7. Reduce set-title text size on mobile
html = html.replace(
    'id="current-set-title" class="text-lg sm:text-xl font-bold text-gray-800 mb-1 font-outfit"',
    'id="current-set-title" class="text-sm sm:text-xl font-bold mb-0.5 sm:mb-1 font-outfit truncate max-w-[180px] sm:max-w-none"'
)

# 8. Textarea rows smaller on mobile
html = html.replace(
    'id="open-ended-answer" rows="4"',
    'id="open-ended-answer" rows="3"'
)

# 9. Bottom action bar: less top margin + padding on mobile
html = html.replace(
    'class="flex justify-between items-center mt-8 border-t pt-4"',
    'class="flex justify-between items-center mt-4 sm:mt-8 border-t pt-3 sm:pt-4"'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied mobile optimizations to quiz.html")
