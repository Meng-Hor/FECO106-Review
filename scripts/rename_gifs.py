import os
import re

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

rename_map = {
    "custom_1.gif": "amazed_mind_blown.gif",
    "custom_5.gif": "nice_borat.gif",
    "custom_6.gif": "nice_key_and_peele.gif",
    "custom_7.gif": "nice_michael_rosen.gif",
    "custom_8.gif": "goodjob_koolaid_man.gif",
    "custom_9.gif": "goodjob_thumbs_up.gif",
    "custom_10.gif": "goodjob_spongebob.gif",
    "custom_11.gif": "goodjob_office.gif",
    "custom_12.gif": "very_nice_borat.gif",
    "custom_13.gif": "cool_kitty_sunglasses.gif",
    "custom_14.gif": "reaction_user_added_1.gif",
    "custom_15.gif": "reaction_user_added_2.gif",
    "custom_16.gif": "reaction_user_added_3.gif",
    "custom_17.gif": "reaction_user_added_4.gif",
    "custom_18.gif": "reaction_user_added_5.gif"
}

added_files = []

for old_name, new_name in rename_map.items():
    old_path = os.path.join(dest_dir, old_name)
    new_path = os.path.join(dest_dir, new_name)
    if os.path.exists(old_path):
        if os.path.exists(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)
        added_files.append(f"'assets/gifs/{new_name}'")

# Clean up any missed custom_*.gif files just to be safe
for f in os.listdir(dest_dir):
    if f.startswith("custom_"):
        os.remove(os.path.join(dest_dir, f))

# Update Javascript
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r"const availableGifs = \[(.*?)\];", html)
if match:
    new_array = "const availableGifs = [" + ", ".join(added_files) + "];"
    html = html.replace(match.group(0), new_array)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully renamed files and updated JS!")
