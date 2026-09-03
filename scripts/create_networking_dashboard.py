import re

feco_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\feco106.html'
net_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\networking.html'

with open(feco_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update title and hero
html = html.replace('<title>FECO106: Mid-Term Review</title>', '<title>Networking: OSI and TCP/IP Review</title>')
html = html.replace('<h1 class="text-5xl sm:text-6xl font-extrabold mb-6 font-outfit theme-gradient-text tracking-tight relative z-10">FECO106 Algorithm III</h1>',
                    '<h1 class="text-5xl sm:text-6xl font-extrabold mb-6 font-outfit theme-gradient-text tracking-tight relative z-10">Networking Basics</h1>')

# The scripts at the bottom load the quiz sets
# We need to replace all `<script src="sets/.../data.js"></script>` with just our new networking one
script_pattern = re.compile(r'(<script src="sets/.*?>\s*)+')
new_script = '<script src="sets/Networking_OSI_TCP_IP/data.js"></script>\n  '
html = script_pattern.sub(new_script, html)

# The FECO106 page also has pdfData hardcoded in it (unless it's in a JS file, let's check).
# Actually, pdfData is hardcoded in feco106.html's inline script.
pdf_pattern = re.compile(r'const pdfData = \[.*?\];', re.DOTALL)
html = pdf_pattern.sub('const pdfData = [];', html)

with open(net_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Created networking.html")
