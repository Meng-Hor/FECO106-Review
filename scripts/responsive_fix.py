import re

def fix_html_file(filepath, is_quiz=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Nav Responsive Fix
    old_nav = r'<div class="max-w-5xl mx-auto px-4 sm:px-4 sm:px-6 py-2 sm:py-3 sm:py-4 flex justify-between items-center">.*?<div class="flex space-x-4 sm:space-x-6">'
    
    new_nav = '''<div class="max-w-5xl mx-auto px-4 sm:px-6 py-3 flex flex-col md:flex-row justify-between items-center gap-3 md:gap-0">
            <a href="index.html" class="flex items-center space-x-3 group">
                <div class="nav-btn w-10 h-10 rounded-lg overflow-hidden flex items-center justify-center shadow-sm ">
                    <img src="dog_icon.png" alt="Dog Icon" class="w-full h-full object-cover">
                </div>
                <span class="font-outfit font-extrabold text-2xl theme-gradient-text tracking-tighter">FECO106</span>
            </a>
            <div class="flex flex-wrap justify-center items-center gap-1 sm:gap-2 md:gap-4 w-full md:w-auto">'''
    
    html = re.sub(old_nav, new_nav, html, flags=re.DOTALL)
    
    # Hide text on mobile for links
    html = html.replace('<i class="fa-solid fa-house mr-2 text-sm"></i> Home', '<i class="fa-solid fa-house sm:mr-2 text-sm"></i> <span class="hidden sm:inline">Home</span>')
    html = html.replace('<i class="fa-solid fa-layer-group mr-2 text-sm"></i> Quizzes', '<i class="fa-solid fa-layer-group sm:mr-2 text-sm"></i> <span class="hidden sm:inline">Quizzes</span>')
    html = html.replace('<i class="fa-solid fa-file-pdf mr-2 text-sm"></i> Materials', '<i class="fa-solid fa-file-pdf sm:mr-2 text-sm"></i> <span class="hidden sm:inline">Materials</span>')
    
    # Fix the border-left and margin on the theme selector div
    html = html.replace('class="flex items-center ml-2 border-l border-purple-200/50 pl-2 sm:pl-4"', 'class="flex items-center ml-1 sm:ml-2 border-l border-gray-300/30 pl-2 sm:pl-4 gap-1 sm:gap-2"')
    html = html.replace('ml-2 w-10 h-10', 'w-10 h-10') # Remove margin left from mode toggle since parent has gap

    if is_quiz:
        # 2. Fix the Quiz Header (Timer & Question count)
        old_q_header = r'<div class="flex justify-between items-center mb-6">\s*<div class="bg-gray-100 px-4 py-2 rounded-lg font-bold text-gray-700">\s*Question <span id="current-question-num" class="text-blue-600">1</span> of <span id="total-questions">10</span>\s*</div>\s*<div class="flex items-center space-x-2 bg-blue-50 px-4 py-2 rounded-lg border border-blue-200">\s*<i class="fa-solid fa-stopwatch text-blue-500"></i>\s*<span id="time-left" class="font-bold text-blue-700 text-lg">30</span><span class="text-blue-500 text-sm font-medium">s</span>\s*</div>\s*</div>'
        
        new_q_header = '''<div class="flex justify-between items-center mb-6 gap-2">
                    <div class="px-4 py-2 rounded-lg font-bold flex-1 text-center sm:text-left stat-card shadow-sm border-0">
                        <span class="hidden sm:inline" style="color: var(--text-muted)">Question</span> 
                        <span id="current-question-num" class="text-lg" style="color: var(--primary-color)">1</span> 
                        <span style="color: var(--text-muted)">/</span> 
                        <span id="total-questions" style="color: var(--text-main)">10</span>
                    </div>
                    <div class="flex justify-center items-center space-x-2 px-5 py-2 rounded-lg stat-card shadow-sm border-0 flex-1 sm:flex-none">
                        <i class="fa-solid fa-stopwatch text-lg" style="color: var(--danger-color)"></i>
                        <span id="time-left" class="font-bold text-xl font-outfit" style="color: var(--danger-color)">30</span><span class="text-sm font-medium opacity-70" style="color: var(--danger-color)">s</span>
                    </div>
                </div>'''
        
        html = re.sub(old_q_header, new_q_header, html, flags=re.DOTALL)
        
        # Also ensure timer logic doesn't add back hardcoded tailwind classes
        # 'border-red-500', 'bg-red-50', 'text-red-600'
        html = html.replace("timeEl.parentElement.classList.add('border-red-500', 'bg-red-50', 'animate-pulse');", "timeEl.parentElement.classList.add('animate-pulse');")
        html = html.replace("timeEl.classList.remove('text-blue-700');", "")
        html = html.replace("timeEl.classList.add('text-red-600');", "")
        
        html = html.replace("timeEl.parentElement.classList.remove('border-blue-500');", "")
        html = html.replace("timeEl.parentElement.classList.remove('bg-blue-50');", "")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html_file(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html', is_quiz=False)
fix_html_file(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html', is_quiz=True)

print("Optimized layout for all devices and fixed remaining hardcoded components")
