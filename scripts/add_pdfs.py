import os
import json
import re

html_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\index.html'
material_dir = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\material'

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add the pdf-container back to the HTML if it's missing
if 'id="pdf-container"' not in content:
    pdf_container_html = """
            </div>
            
            <h2 class="text-2xl font-semibold mb-6">Study Materials (PDFs)</h2>
            <div id="pdf-container" class="grid gap-4 md:grid-cols-2">
                <!-- Dynamically populated -->
            </div>
        </div>
"""
    content = content.replace('            </div>\n        </div>', pdf_container_html)

# 2. Add pdfData and its rendering logic back to JS if it's missing
# Find all PDFs in material_dir
pdf_files = [f for f in os.listdir(material_dir) if f.endswith('.pdf')]
pdf_data = [{'name': f, 'path': 'material/' + f} for f in pdf_files]

pdf_data_str = json.dumps(pdf_data)

# Ensure const pdfData exists or insert it
if 'const pdfData' in content:
    content = re.sub(r'const pdfData = \[.*?\];', f"const pdfData = {pdf_data_str};", content, flags=re.DOTALL)
else:
    # Insert it right after quizData
    content = re.sub(r'(const quizData = \[.*?\];)', r'\1\n        const pdfData = ' + pdf_data_str + ';', content, flags=re.DOTALL)

# Add logic to render PDFs in initDashboard
render_logic = """
            pdfContainer.innerHTML = '';
            if (pdfData.length === 0) {
                pdfContainer.innerHTML = '<p class="text-gray-500">No PDF materials found.</p>';
            } else {
                pdfData.forEach((pdf) => {
                    const link = document.createElement('a');
                    link.href = encodeURI(pdf.path);
                    link.target = '_blank';
                    link.className = 'p-6 bg-white border-2 border-gray-100 rounded-xl hover:border-red-500 hover:shadow-md transition-all text-left group flex items-center justify-between';
                    link.innerHTML = `
                        <h3 class="text-lg font-bold text-gray-800 group-hover:text-red-600 truncate mr-4">${pdf.name}</h3>
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                        </svg>
                    `;
                    pdfContainer.appendChild(link);
                });
            }
"""

if 'pdfContainer.innerHTML' not in content:
    # We need to add const pdfContainer = document.getElementById('pdf-container');
    content = content.replace("const setsContainer = document.getElementById('quiz-sets-container');", "const setsContainer = document.getElementById('quiz-sets-container');\n        const pdfContainer = document.getElementById('pdf-container');")
    
    # We need to add the render logic inside initDashboard()
    # Find initDashboard function
    content = content.replace("setsContainer.innerHTML = '';", "setsContainer.innerHTML = '';\n" + render_logic)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored PDF container and added new PDFs to the dashboard!")
