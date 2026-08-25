import re

def safe_update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inject the Moon button next to the theme-selector
    old_dropdown = r'<select id="theme-selector" class="bg-white/50 border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer transition-colors hover:bg-white/80 outline-none ml-2">.*?<option value="glacial">❄️ Glacial Mint</option>\s*</select>'
    
    new_ui = '''<select id="theme-selector" class="bg-white/50 border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer transition-colors hover:bg-white/80 outline-none ml-2">
                    <option value="aura">✨ Pastel Aura</option>
                    <option value="sunset">🌅 Peach Sunset</option>
                    <option value="glacial">❄️ Glacial Mint</option>
                </select>
                <button id="mode-toggle" class="ml-2 w-10 h-10 rounded-lg flex items-center justify-center text-purple-600 bg-white/50 border border-purple-200/50 hover:bg-white/80 transition-colors focus:outline-none shadow-sm">
                    <i id="mode-icon" class="fa-solid fa-moon"></i>
                </button>'''
    
    html = re.sub(old_dropdown, new_ui, html, flags=re.DOTALL)

    # 2. Safely replace ONLY the specific Theme Switcher JS block at the very end of the file
    old_js = r'<script>\s*// Theme Switcher Logic.*?</script>\s*</body>'
    
    new_js = '''<script>
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

    html = re.sub(old_js, new_js, html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

safe_update_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
safe_update_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Safely injected manual dark mode HTML and JS")
