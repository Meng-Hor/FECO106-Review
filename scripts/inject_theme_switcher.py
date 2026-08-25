import re

def add_theme_switcher(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Create the sleek dropdown HTML
    dropdown_html = '''
                <select id="theme-selector" class="bg-white/50 border border-purple-200/50 text-purple-600 text-sm rounded-lg focus:ring-purple-500 focus:border-purple-500 block p-2 backdrop-blur-sm cursor-pointer transition-colors hover:bg-white/80 outline-none ml-2">
                    <option value="aura">✨ Pastel Aura</option>
                    <option value="sunset">🌅 Peach Sunset</option>
                    <option value="glacial">❄️ Glacial Mint</option>
                </select>'''

    # Insert it at the end of the nav links
    html = re.sub(r'(<a href="index\.html#pdf-container".*?</a>)', r'\1' + dropdown_html, html)

    # Clean up hardcoded bg-white/70 in nav, since CSS now handles it via var(--nav-bg)
    html = html.replace('class="bg-white/70 backdrop-blur-xl border-b border-white sticky top-0 z-50 shadow-sm"', 'class="backdrop-blur-xl sticky top-0 z-50 shadow-sm"')

    # Add the JavaScript to handle the theme switching and localStorage
    js_code = '''
    <script>
        // Theme Switcher Logic
        const themeSelector = document.getElementById('theme-selector');
        
        // Load saved theme or default
        const savedTheme = localStorage.getItem('selectedTheme') || 'aura';
        document.documentElement.setAttribute('data-theme', savedTheme);
        if (themeSelector) themeSelector.value = savedTheme;

        // Listen for changes
        if (themeSelector) {
            themeSelector.addEventListener('change', (e) => {
                const newTheme = e.target.value;
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('selectedTheme', newTheme);
            });
        }
    </script>
</body>'''
    html = html.replace('</body>', js_code)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

add_theme_switcher(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
add_theme_switcher(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Injected theme switcher into HTML")
