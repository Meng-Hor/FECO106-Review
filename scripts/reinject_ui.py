import re

def full_inject(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject the UI into the Navbar
    # Find the Materials link to inject after it
    materials_link_pattern = r'(<a href="index\.html#pdf-container"[^>]*>.*?</a>)'
    
    ui_html = '''
                <div class="flex items-center ml-2 border-l border-purple-200/50 pl-2 sm:pl-4">
                    <select id="theme-selector" class="bg-white/50 border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer transition-colors hover:bg-white/80 outline-none">
                        <option value="aura">✨ Pastel Aura</option>
                        <option value="sunset">🌅 Peach Sunset</option>
                        <option value="glacial">❄️ Glacial Mint</option>
                    </select>
                    <button id="mode-toggle" class="ml-2 w-10 h-10 rounded-lg flex items-center justify-center text-purple-600 bg-white/50 border border-purple-200/50 hover:bg-white/80 transition-colors focus:outline-none shadow-sm">
                        <i id="mode-icon" class="fa-solid fa-moon"></i>
                    </button>
                </div>'''
                
    if 'theme-selector' not in html:
        html = re.sub(materials_link_pattern, r'\1' + ui_html, html)

    # Clean up hardcoded bg-white/70 in nav, since CSS now handles it via var(--nav-bg)
    html = html.replace('class="bg-white/70 backdrop-blur-xl border-b border-white sticky top-0 z-50 shadow-sm"', 'class="backdrop-blur-xl sticky top-0 z-50 shadow-sm"')
    html = html.replace('class="bg-[#FDE8D0]/90 backdrop-blur-xl border-b border-[#F0D5B5] sticky top-0 z-50 shadow-sm"', 'class="backdrop-blur-xl sticky top-0 z-50 shadow-sm"')

    # 2. Inject the JS right before </body>
    js_logic = '''
    <script>
        // Theme & Mode Logic
        const themeSelector = document.getElementById('theme-selector');
        const modeToggle = document.getElementById('mode-toggle');
        const modeIcon = document.getElementById('mode-icon');
        
        // Load saved theme
        const savedTheme = localStorage.getItem('selectedTheme') || 'aura';
        document.documentElement.setAttribute('data-theme', savedTheme);
        if (themeSelector) themeSelector.value = savedTheme;

        // Load saved mode or default strictly to light
        let currentMode = localStorage.getItem('colorMode') || 'light';
        document.documentElement.setAttribute('data-color-mode', currentMode);
        updateModeIcon();

        // Listen for Theme changes
        if (themeSelector) {
            themeSelector.addEventListener('change', (e) => {
                const newTheme = e.target.value;
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('selectedTheme', newTheme);
            });
        }
        
        // Listen for Mode changes
        if (modeToggle) {
            modeToggle.addEventListener('click', () => {
                currentMode = currentMode === 'dark' ? 'light' : 'dark';
                document.documentElement.setAttribute('data-color-mode', currentMode);
                localStorage.setItem('colorMode', currentMode);
                updateModeIcon();
            });
        }

        function updateModeIcon() {
            if (modeIcon) {
                if (currentMode === 'dark') {
                    modeIcon.className = 'fa-solid fa-sun';
                } else {
                    modeIcon.className = 'fa-solid fa-moon';
                }
            }
        }
    </script>
</body>'''
    
    if 'themeSelector =' not in html:
        html = html.replace('</body>', js_logic)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

full_inject(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
full_inject(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Successfully injected Theme Switcher UI and JS")
