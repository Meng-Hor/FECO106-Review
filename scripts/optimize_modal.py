import re

filepath = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# The old modal inner container:
old_modal_inner = r'<div class="bg-white/70 backdrop-blur-2xl border border-gray-200/50 p-5 sm:p-8 rounded-2xl shadow-2xl \nmax-w-sm w-full text-center border border-gray-100">'

# Let's just do a regex replace for the modal
old_modal = r'<div id="quit-modal" class="hidden fixed inset-0 bg-black bg-opacity-50 z-50 flex items-center justify-center \n?backdrop-blur-sm transition-opacity">\s*<div class="bg-white/70 backdrop-blur-2xl border border-gray-200/50 p-5 sm:p-8 rounded-2xl shadow-2xl \n?max-w-sm w-full text-center border border-gray-100">\s*<div class="text-red-500 mb-4 text-5xl">\s*<i class="fa-solid fa-triangle-exclamation"></i>\s*</div>\s*<h3 class="text-xl sm:text-2xl font-bold text-gray-800 mb-2 font-outfit ">Quit Quiz\?</h3>\s*<p class="text-gray-500 mb-8">All your current progress will be lost. Are you sure you want to return to \n?the dashboard\?</p>\s*<div class="flex flex-col space-y-3">\s*<button id="confirm-quit-btn" class="btn-danger px-4 sm:px-6 py-2 sm:py-3 w-full">Yes, Quit \n?Quiz</button>\s*<button id="cancel-quit-btn" class="btn-secondary px-4 sm:px-6 py-2 sm:py-3 w-full">Cancel</button>\s*</div>\s*</div>\s*</div>'

# Since regex across multiple lines with potential newlines from powershell is messy, let's just replace class names globally on the modal.
# We know the modal is inside <div id="quit-modal"

start_idx = html.find('<div id="quit-modal"')
end_idx = html.find('</div>\n    </div>\n\n\n    <script>', start_idx)
if end_idx == -1:
    end_idx = html.find('</div>\n    </div>', start_idx)

if start_idx != -1 and end_idx != -1:
    modal_html = html[start_idx:end_idx + 14]
    
    # Replace the hardcoded background with card-container
    # Be careful not to replace the outer overlay
    
    new_modal = '''<div id="quit-modal" class="hidden fixed inset-0 bg-black/60 z-50 flex items-center justify-center backdrop-blur-md transition-opacity">
        <div class="card-container p-6 sm:p-8 max-w-sm w-full mx-4 text-center">
            <div class="mb-5 text-5xl" style="color: var(--danger-color)">
                <i class="fa-solid fa-triangle-exclamation"></i>
            </div>
            <h3 class="text-xl sm:text-2xl font-bold mb-3 font-outfit text-gray-800">Quit Quiz?</h3>
            <p class="text-gray-600 mb-8 leading-relaxed">All your current progress will be lost. Are you sure you want to return to the dashboard?</p>
            <div class="flex flex-col space-y-3">
                <button id="confirm-quit-btn" class="btn-danger px-4 sm:px-6 py-2 sm:py-3 w-full font-bold">Yes, Quit Quiz</button>
                <button id="cancel-quit-btn" class="btn-secondary px-4 sm:px-6 py-2 sm:py-3 w-full font-bold">Cancel</button>
            </div>
        </div>
    </div>'''
    
    html = html[:start_idx] + new_modal + html[end_idx+14:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated Quit Modal")
else:
    print("Could not find modal bounds accurately")
