import re

path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

new_card = """
      <!-- Networking Subject Card -->
      <a href="networking.html" class="card-container rounded-2xl p-6 relative group overflow-hidden block transition-all duration-300 hover:-translate-y-1" style="border: 1px solid var(--glass-border)">
        <div class="absolute inset-0 opacity-0 group-hover:opacity-10 transition-opacity duration-500 bg-gradient-to-br from-transparent" style="background-color: var(--success-color)"></div>
        <div class="flex items-start justify-between mb-4 relative z-10">
          <div class="w-12 h-12 rounded-xl flex items-center justify-center shadow-sm" style="background: var(--nav-bg); border: 1px solid var(--glass-border)">
            <i class="fa-solid fa-network-wired text-2xl" style="color: var(--success-color)"></i>
          </div>
          <span class="px-3 py-1 rounded-full text-xs font-bold" style="background: var(--success-color); color: white;">Active</span>
        </div>
        <h3 class="text-xl font-bold mb-2 font-outfit" style="color: var(--text-main)">Networking Basics</h3>
        <p class="text-sm line-clamp-2" style="color: var(--text-muted)">OSI Model, TCP/IP, and fundamental networking concepts.</p>
        <div class="mt-4 pt-4 border-t flex justify-between items-center" style="border-color: var(--glass-border)">
          <span class="text-sm font-semibold" style="color: var(--success-color)">Enter Subject <i class="fa-solid fa-arrow-right ml-1"></i></span>
        </div>
      </a>

      <!-- Placeholder Subject Card -->"""

html = html.replace('<!-- Placeholder Subject Card -->', new_card)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Added Networking card to index.html")
