import re

# 1. Update CSS to include .stat-card
css_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_classes = '''
.stat-card {
    background: var(--nav-bg);
    border: 1px solid var(--glass-border);
    box-shadow: 0 4px 15px var(--water-shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.stat-card:hover {
    transform: translateY(-3px);
    border-color: var(--primary-color);
    box-shadow: 0 8px 25px var(--water-shadow);
}
'''
if '.stat-card' not in css:
    css = css + new_classes
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

# 2. Rewrite HTML for result-view
html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

old_result_view = r'<div id="result-view" class="hidden card-container p-5 sm:p-8 text-center">.*?<button id="home-btn" class="btn-primary px-6 py-3 w-full max-w-sm mx-auto"><i class="fa-solid fa-house \n?mr-2"></i>Back to Dashboard</button>\s*</div>'

new_result_view = '''<div id="result-view" class="hidden card-container p-6 sm:p-10 text-center relative overflow-hidden">
            <!-- Theme-adaptive ambient background glow -->
            <div class="absolute -top-20 -right-20 w-64 h-64 rounded-full blur-3xl opacity-20 pointer-events-none" style="background: var(--primary-color)"></div>
            <div class="absolute -bottom-20 -left-20 w-64 h-64 rounded-full blur-3xl opacity-10 pointer-events-none" style="background: var(--danger-color)"></div>
            
            <img src="quiz_complete.png" alt="Quiz Complete Celebration" class="w-40 sm:w-56 h-auto mx-auto mb-8 drop-shadow-2xl rounded-2xl relative z-10 border-4 border-white/10">
            
            <h2 class="text-3xl sm:text-5xl font-extrabold mb-8 font-outfit theme-gradient-text tracking-tight relative z-10">Quiz Completed!</h2>
            
            <div class="grid grid-cols-2 gap-4 sm:gap-6 max-w-md mx-auto mb-10 relative z-10">
                
                <!-- Correct Stat Card -->
                <div class="stat-card p-5 sm:p-6 rounded-2xl flex flex-col items-center justify-center relative overflow-hidden group">
                    <div class="absolute inset-0 opacity-10 bg-gradient-to-br from-transparent to-[var(--success-color)] group-hover:opacity-20 transition-opacity duration-500"></div>
                    <i class="fa-solid fa-medal text-3xl sm:text-4xl mb-3 drop-shadow-md" style="color: var(--success-color)"></i>
                    <p class="text-xs sm:text-sm font-bold uppercase tracking-wider mb-2" style="color: var(--text-muted)">Correct</p>
                    <p id="correct-count" class="text-4xl sm:text-5xl font-black font-outfit drop-shadow-sm" style="color: var(--success-color)">0</p>
                </div>
                
                <!-- Incorrect Stat Card -->
                <div class="stat-card p-5 sm:p-6 rounded-2xl flex flex-col items-center justify-center relative overflow-hidden group">
                    <div class="absolute inset-0 opacity-10 bg-gradient-to-br from-transparent to-[var(--danger-color)] group-hover:opacity-20 transition-opacity duration-500"></div>
                    <i class="fa-solid fa-circle-xmark text-3xl sm:text-4xl mb-3 drop-shadow-md" style="color: var(--danger-color)"></i>
                    <p class="text-xs sm:text-sm font-bold uppercase tracking-wider mb-2" style="color: var(--text-muted)">Incorrect</p>
                    <p id="incorrect-count" class="text-4xl sm:text-5xl font-black font-outfit drop-shadow-sm" style="color: var(--danger-color)">0</p>
                </div>
                
            </div>

            <button id="home-btn" class="btn-primary px-8 py-4 w-full max-w-sm mx-auto text-lg rounded-xl relative z-10 shadow-xl transition-all"><i class="fa-solid fa-house mr-2"></i>Back to Dashboard</button>
        </div>'''

html = re.sub(old_result_view, new_result_view, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Redesigned quiz completion screen")
