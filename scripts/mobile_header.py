import re

def update_header(path, is_quiz=False):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # New header that is single-row on mobile, full on desktop
    quit_warning = ' id="smart-header"' if not is_quiz else ' id="smart-header"'
    
    new_header = '''  <!-- Smart Header -->
  <div id="smart-header" class="px-2 sm:px-4 pt-2 sm:pt-6 sticky top-0 z-50" style="transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);">
    <nav class="max-w-6xl mx-auto rounded-2xl sm:rounded-3xl px-3 sm:px-6 py-2 sm:py-3 flex flex-row justify-between items-center border border-white/20" style="gap: 0;">

      <!-- Logo (always visible) -->
      <a href="index.html" class="flex items-center space-x-2 group flex-shrink-0">
        <div class="nav-btn w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl overflow-hidden flex items-center justify-center shadow-sm">
          <img src="dog_icon.png" alt="Dog Icon" class="w-full h-full object-cover">
        </div>
        <span class="font-outfit font-extrabold text-lg sm:text-2xl theme-gradient-text tracking-tighter">GoodLuck :D</span>
      </a>

      <!-- Desktop Nav Links (hidden on mobile) -->
      <div class="hidden md:flex items-center gap-1 sm:gap-2 md:gap-4">
        <a href="index.html" class="nav-link font-outfit font-bold tracking-wide flex items-center"><i class="fa-solid fa-house mr-2 text-sm"></i>Home</a>
        <a href="index.html#dashboard" class="nav-link font-outfit font-bold tracking-wide flex items-center"><i class="fa-solid fa-layer-group mr-2 text-sm"></i>Quizzes</a>
        <a href="index.html#pdf-container" class="nav-link font-outfit font-bold tracking-wide flex items-center"><i class="fa-solid fa-file-pdf mr-2 text-sm"></i>Materials</a>
      </div>

      <!-- Right Controls -->
      <div class="flex items-center gap-1 sm:gap-2">
        <!-- Theme selector: compact on mobile -->
        <select id="theme-selector" class="nav-btn text-xs sm:text-sm font-medium rounded-lg sm:rounded-xl font-outfit px-1.5 sm:px-3 p-1.5 sm:p-2 backdrop-blur-sm cursor-pointer outline-none max-w-[80px] sm:max-w-none">
          <option value="aura">✨ Pastel Aura</option>
          <option value="sunset">🌅 Peach Sunset</option>
          <option value="glacial">❄️ Glacial Mint</option>
        </select>
        <!-- Mode toggle -->
        <button id="mode-toggle" class="nav-btn w-8 h-8 sm:w-10 sm:h-10 rounded-lg sm:rounded-xl flex items-center justify-center focus:outline-none shadow-sm transition-transform hover:rotate-12">
          <i id="mode-icon" class="fa-solid fa-moon text-sm sm:text-base"></i>
        </button>
        <!-- Mobile hamburger (visible on mobile only) -->
        <button id="mobile-menu-btn" class="nav-btn w-8 h-8 rounded-lg flex items-center justify-center md:hidden focus:outline-none shadow-sm" aria-label="Open menu">
          <i id="hamburger-icon" class="fa-solid fa-bars text-sm"></i>
        </button>
      </div>
    </nav>

    <!-- Mobile Dropdown Menu -->
    <div id="mobile-menu" class="hidden md:hidden max-w-6xl mx-auto mt-1 rounded-2xl border border-white/20 px-4 py-3 flex flex-col gap-2" style="background: var(--nav-bg); backdrop-filter: blur(24px);">
      <a href="index.html" class="nav-link font-outfit font-bold tracking-wide flex items-center py-2 border-b border-white/10"><i class="fa-solid fa-house mr-3"></i>Home</a>
      <a href="index.html#dashboard" class="nav-link font-outfit font-bold tracking-wide flex items-center py-2 border-b border-white/10"><i class="fa-solid fa-layer-group mr-3"></i>Quizzes</a>
      <a href="index.html#pdf-container" class="nav-link font-outfit font-bold tracking-wide flex items-center py-2"><i class="fa-solid fa-file-pdf mr-3"></i>Materials</a>
    </div>
  </div>'''

    # Replace old header block
    old_header_pattern = r'  <!-- Navigation Bar -->.*?  </div>\s*(?=\s*<div class="max-w-6xl)'
    html = re.sub(old_header_pattern, new_header + '\n', html, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated header in {path}")

update_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
update_header(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html', is_quiz=True)
