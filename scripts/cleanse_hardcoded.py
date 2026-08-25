import re

# ==========================================
# FIX INDEX.HTML DASHBOARD
# ==========================================
index_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    idx_html = f.read()

# Replace the old dashboard block
old_dash = r'<div class="max-w-4xl mx-auto px-4 py-8 relative z-10">.*?</div>\s*<script>'
new_dash = '''<div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 relative z-10">
        <!-- Hero Section -->
        <div class="text-center mb-16 relative">
            <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-64 h-64 rounded-full blur-[100px] opacity-30 pointer-events-none" style="background: var(--primary-color)"></div>
            <h1 class="text-5xl sm:text-6xl font-extrabold mb-6 font-outfit theme-gradient-text tracking-tight relative z-10">Interactive Learning</h1>
            <p class="text-lg sm:text-xl font-medium max-w-2xl mx-auto relative z-10" style="color: var(--text-muted)">Master your knowledge with dynamically generated quizzes and curated study materials.</p>
        </div>

        <!-- Dashboard View -->
        <div id="dashboard">
            <!-- Quiz Section -->
            <div class="mb-16">
                <div class="flex items-center mb-8">
                    <div class="w-12 h-12 rounded-xl flex items-center justify-center mr-4 shadow-sm" style="background: var(--nav-bg); border: 1px solid var(--glass-border)">
                        <i class="fa-solid fa-layer-group text-2xl" style="color: var(--primary-color)"></i>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold font-outfit tracking-tight" style="color: var(--text-main)">Available Quizzes</h2>
                </div>
                <div id="quiz-sets-container" class="grid gap-4 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
                    <!-- Dynamically populated -->
                </div>
            </div>
            
            <!-- Materials Section -->
            <div class="mb-12">
                <div class="flex items-center mb-8">
                    <div class="w-12 h-12 rounded-xl flex items-center justify-center mr-4 shadow-sm" style="background: var(--nav-bg); border: 1px solid var(--glass-border)">
                        <i class="fa-solid fa-file-pdf text-2xl" style="color: var(--danger-color)"></i>
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold font-outfit tracking-tight" style="color: var(--text-main)">Study Materials</h2>
                </div>
                <div id="pdf-container" class="grid gap-4 sm:gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
                    <!-- Dynamically populated -->
                </div>
            </div>
        </div>
    </div>
    <script>'''
idx_html = re.sub(old_dash, new_dash, idx_html, flags=re.DOTALL)

# Also fix the JS inside index.html for the button generation
old_js_pdf = r'''link\.innerHTML = `
\s*<div class="flex items-center min-w-0 flex-1"><i class="fa-solid fa-file-pdf text-theme-danger mr-3 text-xl flex-shrink-0"></i><h3 class="text-lg font-bold text-gray-800 group-hover:text-theme-danger truncate mr-4">\$\{pdf\.name\}</h3></div>
\s*<i class="fa-solid fa-download text-gray-400 group-hover:text-theme-danger transition-colors flex-shrink-0 ml-2"></i>`;'''
new_js_pdf = '''link.innerHTML = `
    <div class="flex items-center min-w-0 flex-1"><i class="fa-solid fa-file-pdf text-theme-danger mr-3 text-2xl flex-shrink-0"></i><h3 class="text-lg font-bold group-hover:text-theme-danger truncate mr-4 transition-colors" style="color: var(--text-main)">${pdf.name}</h3></div>
    <div class="w-10 h-10 rounded-xl flex items-center justify-center transition-all group-hover:scale-110" style="background: var(--nav-bg); border: 1px solid var(--glass-border)"><i class="fa-solid fa-download" style="color: var(--danger-color)"></i></div>`;'''
idx_html = re.sub(old_js_pdf, new_js_pdf, idx_html, flags=re.DOTALL)

old_js_quiz = r'''<h3 class="text-lg font-bold text-gray-800 group-hover:text-theme-primary mb-2 truncate">\$\{cleanName\}</h3>
\s*<p class="text-sm text-gray-500">\$\{set\.questions\.length\} Questions</p>`;'''
new_js_quiz = '''<h3 class="text-lg font-bold group-hover:text-theme-primary mb-2 truncate transition-colors" style="color: var(--text-main)">${cleanName}</h3>
    <p class="text-sm font-medium flex items-center gap-2" style="color: var(--text-muted)"><i class="fa-solid fa-clipboard-question opacity-70"></i> ${set.questions.length} Questions</p>`;'''
idx_html = re.sub(old_js_quiz, new_js_quiz, idx_html, flags=re.DOTALL)

idx_html = idx_html.replace("btn.className = 'btn-secondary p-4 sm:p-6 text-left group';", "btn.className = 'btn-secondary p-5 sm:p-6 text-left group flex flex-col justify-between h-full min-h-[140px] relative overflow-hidden';")
idx_html = idx_html.replace("link.className = 'btn-secondary p-4 sm:p-6 text-left group flex items-center justify-between';", "link.className = 'btn-secondary p-5 sm:p-6 text-left group flex items-center justify-between relative overflow-hidden';")

# Clean up nav border line in index
idx_html = idx_html.replace('border-gray-300/30', 'border-white/20')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx_html)


# ==========================================
# FIX QUIZ.HTML HEADER & TIMER
# ==========================================
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    qz_html = f.read()

# Clean up nav border line
qz_html = qz_html.replace('border-gray-300/30', 'border-white/20')

# Fix Quiz Header
old_quiz_header = r'<div class="flex justify-between items-center mb-6 border-b pb-6">.*?<span id="time-left" class="text-xl font-bold">20</span>\s*</div>\s*</div>\s*</div>'
new_quiz_header = '''<div class="flex justify-between items-center mb-6 border-b pb-6 border-white/10">
    <div>
        <h3 id="current-set-title" class="text-lg sm:text-xl font-bold mb-2 font-outfit" style="color: var(--text-main)">Set Title</h3>
        <p class="text-sm font-medium" style="color: var(--text-muted)">Question <span id="current-question-num" class="font-bold" style="color: var(--primary-color)">1</span> of <span id="total-questions" style="color: var(--text-main)">10</span></p>
    </div>
    <div class="flex items-center gap-4">
        <div class="w-16 h-16 rounded-2xl flex items-center justify-center relative transition-colors duration-300 shadow-sm" style="background: var(--nav-bg); border: 2px solid var(--primary-color);">
            <span id="time-left" class="text-2xl font-black font-outfit" style="color: var(--primary-color)">20</span>
        </div>
    </div>
</div>'''
qz_html = re.sub(old_quiz_header, new_quiz_header, qz_html, flags=re.DOTALL)

# Fix Question Text and Quit Modal
qz_html = qz_html.replace('text-xl sm:text-2xl font-semibold mb-6 text-gray-800', 'text-xl sm:text-2xl font-semibold mb-6' + ' style="color: var(--text-main)"')
qz_html = qz_html.replace('text-xl sm:text-2xl font-bold mb-3 font-outfit text-gray-800', 'text-xl sm:text-2xl font-bold mb-3 font-outfit' + ' style="color: var(--text-main)"')

# Fix Timer Javascript Logic
qz_html = qz_html.replace("timeEl.parentElement.classList.remove('border-red-500');", "timeEl.parentElement.style.borderColor = 'var(--primary-color)';")
qz_html = qz_html.replace("timeEl.parentElement.classList.add('border-blue-500');", "timeEl.style.color = 'var(--primary-color)';")
qz_html = qz_html.replace("timeEl.parentElement.classList.add('border-red-500');", "timeEl.parentElement.style.borderColor = 'var(--danger-color)'; timeEl.style.color = 'var(--danger-color)';")

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(qz_html)

print("Massively cleansed hardcoded tailwind colors")
