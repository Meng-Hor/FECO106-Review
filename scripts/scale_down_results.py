import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the image smaller: w-40 sm:w-56 -> w-32 sm:w-48, mb-8 -> mb-6
html = html.replace('class="w-40 sm:w-56 h-auto mx-auto mb-8 drop-shadow-2xl rounded-2xl relative z-10 border-4 border-white/10"', 
                    'class="w-32 sm:w-48 h-auto mx-auto mb-6 drop-shadow-xl rounded-2xl relative z-10 border-2 border-white/20"')

# Make the title smaller: text-3xl sm:text-5xl -> text-2xl sm:text-4xl, mb-8 -> mb-6
html = html.replace('class="text-3xl sm:text-5xl font-extrabold mb-8 font-outfit theme-gradient-text tracking-tight relative z-10"',
                    'class="text-2xl sm:text-4xl font-extrabold mb-6 font-outfit theme-gradient-text tracking-tight relative z-10"')

# Reduce stat card padding: p-5 sm:p-6 -> p-4 sm:p-5, mb-10 -> mb-8
html = html.replace('class="grid grid-cols-2 gap-4 sm:gap-6 max-w-md mx-auto mb-10 relative z-10"',
                    'class="grid grid-cols-2 gap-4 sm:gap-5 max-w-sm mx-auto mb-8 relative z-10"')
html = html.replace('class="stat-card p-5 sm:p-6 rounded-2xl flex flex-col items-center justify-center relative overflow-hidden group"',
                    'class="stat-card p-4 sm:p-5 rounded-xl flex flex-col items-center justify-center relative overflow-hidden group"')

# Reduce stat card icons: text-3xl sm:text-4xl -> text-2xl sm:text-3xl, mb-3 -> mb-2
html = html.replace('class="fa-solid fa-medal text-3xl sm:text-4xl mb-3 drop-shadow-md"',
                    'class="fa-solid fa-medal text-2xl sm:text-3xl mb-2 drop-shadow-md"')
html = html.replace('class="fa-solid fa-circle-xmark text-3xl sm:text-4xl mb-3 drop-shadow-md"',
                    'class="fa-solid fa-circle-xmark text-2xl sm:text-3xl mb-2 drop-shadow-md"')

# Reduce stat card numbers: text-4xl sm:text-5xl -> text-3xl sm:text-4xl
html = html.replace('class="text-4xl sm:text-5xl font-black font-outfit drop-shadow-sm"',
                    'class="text-3xl sm:text-4xl font-black font-outfit drop-shadow-sm"')

# Reduce the Back to Dashboard button size: px-8 py-4 text-lg -> px-6 py-3 text-base
html = html.replace('class="btn-primary px-8 py-4 w-full max-w-sm mx-auto text-lg rounded-xl relative z-10 shadow-xl transition-all"',
                    'class="btn-primary px-6 py-3 w-full max-w-xs mx-auto text-base rounded-xl relative z-10 shadow-lg transition-all"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Scaled down the completion screen components")
