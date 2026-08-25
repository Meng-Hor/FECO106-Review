import urllib.request
import re
import os

queries = [
    "amazed-reaction",
    "michael-rosen-nice",
    "thumbs-up-good-job",
    "shrek-smirk",
    "ainsley-harriott-yeah-boi",
    "pikachu-yay"
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"
for f in os.listdir(dest_dir):
    os.remove(os.path.join(dest_dir, f))

valid_count = 0
for q in queries:
    url = f"https://giphy.com/search/{q}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # Regex to find gif IDs
        ids = list(set(re.findall(r'href="/gifs/[^"]*-([a-zA-Z0-9]+)"', html)))
        
        for gid in ids[:4]:  # Take up to 4 per category
            gif_url = f"https://media.giphy.com/media/{gid}/giphy.gif"
            filepath = os.path.join(dest_dir, f"custom_{valid_count + 1}.gif")
            
            try:
                g_req = urllib.request.Request(gif_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(g_req) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
                    
                if os.path.getsize(filepath) == 239321:
                    os.remove(filepath)
                else:
                    valid_count += 1
                    print(f"Downloaded custom_{valid_count}.gif for {q}")
            except Exception:
                pass
    except Exception as e:
        print(f"Failed to scrape {q}: {e}")

print(f"Total valid custom GIFs: {valid_count}")
