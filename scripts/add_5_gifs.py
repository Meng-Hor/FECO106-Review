import os
import urllib.request
import re

urls = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTA1N2RxeW1tMzRhbWlxYzRpMWhmZjBtb3N6NXlmbGVlNXBvczdpeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VRKheDy4DkBMrQm66p/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTA1N2RxeW1tMzRhbWlxYzRpMWhmZjBtb3N6NXlmbGVlNXBvczdpeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Osa136wm7Mg9MSd4zw/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHdwcW0xZTUxZTZhYmp4ZDlpaDR1cG5xbm5tNHJsaXFxYXM2ODRwZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/rVVFWyTINqG7C/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHdwcW0xZTUxZTZhYmp4ZDlpaDR1cG5xbm5tNHJsaXFxYXM2ODRwZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VFDoN1xR2Yvpm/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3h4bzd0am9qOXI4OTVibmFma3pwcXM3eHhucDFxOWtuZGE1MzJ2MyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/O0VBge9U7f8j21UqNj/giphy.gif"
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

added_files = []
current_index = 14

for url in urls:
    filepath = os.path.join(dest_dir, f"custom_{current_index}.gif")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        added_files.append(f"'assets/gifs/custom_{current_index}.gif'")
        print(f"Downloaded custom_{current_index}.gif")
        current_index += 1
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Now update the javascript array
quiz_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html'
with open(quiz_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Current array:
# const availableGifs = ['assets/gifs/custom_1.gif', 'assets/gifs/custom_4.gif', 'assets/gifs/custom_5.gif', 'assets/gifs/custom_6.gif', 'assets/gifs/custom_7.gif', 'assets/gifs/custom_8.gif', 'assets/gifs/custom_9.gif', 'assets/gifs/custom_10.gif', 'assets/gifs/custom_11.gif', 'assets/gifs/custom_12.gif', 'assets/gifs/custom_13.gif'];
match = re.search(r"const availableGifs = \[(.*?)\];", html)
if match:
    existing_items = match.group(1)
    new_items_str = existing_items + ", " + ", ".join(added_files)
    new_array = f"const availableGifs = [{new_items_str}];"
    html = html.replace(match.group(0), new_array)

with open(quiz_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated Javascript array successfully!")
