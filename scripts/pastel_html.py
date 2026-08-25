import re

def update_pastel_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Nav Background and Border
    # Was: bg-[#FDE8D0]/90 backdrop-blur-xl border-b border-[#F0D5B5]
    html = re.sub(r'bg-\[#FDE8D0\]/90 backdrop-blur-xl border-b border-\[#F0D5B5\]', 'bg-white/70 backdrop-blur-xl border-b border-white', html)

    # Hover link effects (orange to purple)
    html = html.replace('hover:text-orange-600', 'hover:text-purple-600')

    # Nav icon container
    # Was: border border-orange-200/50 bg-white/50 group-hover:bg-white/80
    html = html.replace('border border-orange-200/50 bg-white/50', 'border border-purple-200/50 bg-white/50')

    # Dashboard icons
    # Was: fa-pen-to-square text-orange-600
    html = html.replace('text-orange-600', 'text-purple-500')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

update_pastel_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
update_pastel_html(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Updated HTML to match Pastel theme")
