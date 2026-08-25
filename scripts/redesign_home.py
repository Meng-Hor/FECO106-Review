import re

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the Dashboard HTML structure
old_dashboard_html = r'<div class="max-w-4xl mx-auto px-4 py-8 relative z-10">\s*<div class="text-center mb-10">\s*<h1 class="text-4xl sm:text-5xl font-extrabold mb-4 font-outfit theme-gradient-text tracking-tight">Interactive Learning</h1>\s*<p class="text-gray-600 text-lg sm:text-xl font-medium">Master your knowledge with dynamically generated quizzes.</p>\s*</div>\s*<!-- Dashboard View -->\s*<div id="dashboard" class="card-container p-4 sm:p-6">\s*<h2 class="text-xl sm:text-2xl font-semibold mb-6 text-gray-800"><i class="fa-solid fa-layer-group \n?mr-3"></i>Available Quiz Sets</h2>\s*<div id="quiz-sets-container" class="grid gap-3 sm:gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 mb-8">\s*<!-- Dynamically populated -->\s*</div>\s*<h2 class="text-xl sm:text-2xl font-semibold mb-6 text-gray-800 mt-10"><i class="fa-solid fa-book-open \n?mr-3"></i>Study Materials \(PDFs\)</h2>\s*<div id="pdf-container" class="grid gap-3 sm:gap-4 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">\s*<!-- Dynamically populated -->\s*</div>\s*</div>'

new_dashboard_html = '''<div class="max-w-6xl mx-auto px-4 sm:px-6 py-12 relative z-10">
        
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
        </div>'''

html = re.sub(old_dashboard_html, new_dashboard_html, html, flags=re.DOTALL)

# 2. Fix the Javascript inside index.html
old_js = r'''link\.innerHTML = `
\s*<div class="flex items-center min-w-0 flex-1"><i class="fa-solid fa-file-pdf text-theme-danger mr-3 text-xl flex-shrink-0"></i><h3 class="text-lg font-bold text-gray-800 group-hover:text-theme-danger truncate mr-4">\$\{pdf\.name\}</h3></div>
\s*<i class="fa-solid fa-download text-gray-400 group-hover:text-theme-danger transition-colors flex-shrink-0 ml-2"></i>`;'''

new_js = '''link.innerHTML = `
                        <div class="flex items-center min-w-0 flex-1"><i class="fa-solid fa-file-pdf text-theme-danger mr-3 text-2xl flex-shrink-0"></i><h3 class="text-lg font-bold group-hover:text-theme-danger truncate mr-4 transition-colors" style="color: var(--text-main)">${pdf.name}</h3></div>
                        <div class="w-10 h-10 rounded-full flex items-center justify-center transition-all group-hover:scale-110" style="background: var(--nav-bg); border: 1px solid var(--glass-border)"><i class="fa-solid fa-download" style="color: var(--danger-color)"></i></div>`;'''

html = re.sub(old_js, new_js, html, flags=re.DOTALL)

old_quiz_js = r'''<h3 class="text-lg font-bold text-gray-800 group-hover:text-theme-primary mb-2 truncate">\$\{cleanName\}</h3>
\s*<p class="text-sm text-gray-500">\$\{set\.questions\.length\} Questions</p>`;'''

new_quiz_js = '''<h3 class="text-lg font-bold group-hover:text-theme-primary mb-2 truncate transition-colors" style="color: var(--text-main)">${cleanName}</h3>
                        <p class="text-sm font-medium flex items-center gap-2" style="color: var(--text-muted)"><i class="fa-solid fa-clipboard-question opacity-70"></i> ${set.questions.length} Questions</p>`;'''

html = re.sub(old_quiz_js, new_quiz_js, html, flags=re.DOTALL)

# Update styling on the buttons in Javascript so they look more like modern cards
html = html.replace("btn.className = 'btn-secondary p-4 sm:p-6 text-left group';", "btn.className = 'btn-secondary p-5 sm:p-6 text-left group flex flex-col justify-between h-full min-h-[140px] relative overflow-hidden';")
html = html.replace("link.className = 'btn-secondary p-4 sm:p-6 text-left group flex items-center justify-between';", "link.className = 'btn-secondary p-5 sm:p-6 text-left group flex items-center justify-between relative overflow-hidden';")


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print("Redesigned the Dashboard homepage")
