import os
import urllib.request
import time

gif_ids = [
    "26ufdipQqU2lhNA4g", "xT0xeJpnrWC4XWblEk", "3o6Zt8rGMqVwjYAlsA", # Amazed
    "O2K7wIcw3CoeY", "pCO5tKdP22RCU", "3o7abKhOpu0NwenH3O", "yJFeycRK2DB4c", # Nice
    "111ebonMs90YLu", "3oz8xAFtjouK9ScjEN", "l41JRsph73VokN6ik", "3otPoS81loriI9sO8o", # Goodjob
    "SW5kO6tYByfzI", "10waEVPveLqKEE", "TIGP3k4gIGdzy", # Shrek
    "Lq22P1k9QZJ3a", "Oa9oYNcObaHeg", # Yeah boi
    "3oFzmf97Qkvw7vwuic", "26n6R5HOYPbekK0YE", "l2Sq29cFXoF80ADlK", "5wWf7H0qoWaNnkV3O22" # Yay
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

valid_count = 0

for gid in gif_ids:
    url = f"https://media.giphy.com/media/{gid}/giphy.gif"
    filename = f"custom_{valid_count + 1}.gif"
    filepath = os.path.join(dest_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        if os.path.getsize(filepath) == 239321:
            os.remove(filepath)
        else:
            print(f"Downloaded {filename}")
            valid_count += 1
            
    except Exception as e:
        print(f"Failed {gid}: {e}")
    time.sleep(0.1)

print(f"Total valid custom GIFs: {valid_count}")
