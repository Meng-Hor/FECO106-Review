import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# I need to change the single gamepad icon logic to a dynamic icon based on the set name.
# It is located here:
# <i class="fa-solid fa-gamepad text-indigo-500 mb-3 text-2xl group-hover:scale-110 transition-transform"></i>

logic_to_replace = """<i class="fa-solid fa-gamepad text-indigo-500 mb-3 text-2xl group-hover:scale-110 transition-transform"></i>"""

new_logic = """
                    ${set.set.includes('PDF_') ? 
                        '<i class="fa-solid fa-pen-to-square text-blue-500 mb-3 text-2xl group-hover:scale-110 transition-transform"></i>' : 
                        (set.set.includes('Revision') ? 
                            '<i class="fa-solid fa-book text-blue-500 mb-3 text-2xl group-hover:scale-110 transition-transform"></i>' :
                            '<i class="fa-solid fa-list-check text-blue-500 mb-3 text-2xl group-hover:scale-110 transition-transform"></i>'
                        )
                    }
"""

content = content.replace(logic_to_replace, new_logic)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Icons logic updated!")
