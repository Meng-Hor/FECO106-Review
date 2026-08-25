import os
import shutil

base_dir = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term'
web_dir = os.path.join(base_dir, 'web')
scripts_dir = os.path.join(base_dir, 'scripts')

os.makedirs(web_dir, exist_ok=True)
os.makedirs(scripts_dir, exist_ok=True)

# 1. Move website components to 'web'
if os.path.exists(os.path.join(base_dir, 'index.html')):
    shutil.move(os.path.join(base_dir, 'index.html'), os.path.join(web_dir, 'index.html'))

if os.path.exists(os.path.join(base_dir, 'data.js')):
    shutil.move(os.path.join(base_dir, 'data.js'), os.path.join(web_dir, 'data.js'))

# 2. Update the paths in index.html to point to ../material/
index_path = os.path.join(web_dir, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace "material/" with "../material/" for the PDF paths
    content = content.replace('"material/', '"../material/')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Move all python scripts to 'scripts' to clean up the root
for f in os.listdir(base_dir):
    if f.endswith('.py'):
        shutil.move(os.path.join(base_dir, f), os.path.join(scripts_dir, f))

print("Cleanup complete! Moved website to 'web' and scripts to 'scripts'.")
