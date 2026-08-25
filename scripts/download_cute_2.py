import os
import urllib.request
import time

gif_ids = [
    "BwPIFhEUfW6x6a6d34", "R6gvnAxj2ISzJdbA63", "tN06gZ8Ke2g3c", "dzaUX7CAG0Ihi",
    "14urMYvPnI1Try", "vguZeRhhG1hC", "Vbs1hM0N4r419nQ1uG", "H8lT8C3J6lOzm",
    "7rBjbXJmYm10w", "k8pbfX3uXHV0KPf6FS", "52qma5le4j0M8", "X3Yj4XXXieKYM",
    "jT21h7H9H9Bza", "3oriO0OEd9QlcPmJ7C", "mGK1g88HZRa2FlKGbz", "K1tgb1IUeBOgw",
    "mlvseq9yvZhba", "Nm8RcgOecoNjO", "3NtY188QAXCbK", "Lq0h93752f6J9tijrh",
    "VpW1rUa0q6Tvi", "fV4zE5H9V5mP0lYpIn", "MDJ9IbxxvDUQM", "xT0xeJpnrWC4XWblEk",
    "wbcMnfHqOJX9K", "111ebonMs90YLu"
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

# Count existing valid files
valid_count = len([f for f in os.listdir(dest_dir) if f.startswith('cute_')])

for gid in gif_ids:
    if valid_count >= 20:
        break
        
    url = f"https://media.giphy.com/media/{gid}/giphy.gif"
    filename = f"cute_{valid_count + 1}.gif"
    filepath = os.path.join(dest_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        if os.path.getsize(filepath) == 239321:
            os.remove(filepath)
            print(f"Skipped {gid}")
        else:
            print(f"Downloaded cute_{valid_count + 1}.gif")
            valid_count += 1
            
    except Exception as e:
        print(f"Failed {gid}: {e}")
    time.sleep(0.1)

print(f"Total valid cute GIFs: {valid_count}")
