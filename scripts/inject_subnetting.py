import re

# Update networking.html
net_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\networking.html'
with open(net_path, 'r', encoding='utf-8') as f:
    net_html = f.read()

# Add script just before <script>\n    const pdfData = [];
target = '<script>\n    const pdfData = [];'
new_script = '<script src="sets/Networking_IPv4_Subnetting/data.js"></script>\n    '
if 'Networking_IPv4_Subnetting' not in net_html:
    net_html = net_html.replace(target, new_script + target)
    with open(net_path, 'w', encoding='utf-8') as f:
        f.write(net_html)
    print("Updated networking.html")

# Update quiz_networking.html
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\Lesson-Review\web\quiz_networking.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    quiz_html = f.read()

# Add script just before </script>\n      </div>\n  <script>\n  const pdfData = ... wait!
# No, quiz_networking.html has it at the bottom.
# Let's find exactly where Networking_OSI_TCP_IP/data.js is and append to it
target = '<script src="sets/Networking_OSI_TCP_IP/data.js"></script>'
new_script = '<script src="sets/Networking_IPv4_Subnetting/data.js"></script>'
if 'Networking_IPv4_Subnetting' not in quiz_html:
    quiz_html = quiz_html.replace(target, target + '\n    ' + new_script)
    with open(quiz_path, 'w', encoding='utf-8') as f:
        f.write(quiz_html)
    print("Updated quiz_networking.html")
