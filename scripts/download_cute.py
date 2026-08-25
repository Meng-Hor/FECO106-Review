import os
import urllib.request
import time

gif_ids = [
    "l41JRsph73VokN6ik", # Spongebob
    "11sBLVxNs7v6WA", # Minions
    "26n6R5HOYPbekK0YE", # Pikachu
    "3oFzmf97Qkvw7vwuic", # Kermit
    "Lndtxw3ztLhNC", # Monkey
    "VbnUQpnihPSIgIXuZv", # Cat thumbs up
    "YJjvTqoRFgZaM", # Snoopy
    "JpG2A9P3dPHHoVJCce", # Dog smile
    "MDJ9IbxxvDUQM", # Cat happy
    "8rFgvQvqEQQA1PKLoI", # Dog happy
    "chzz1FQgqhytG", # Red panda
    "Z5xk7fGO5FjjTElnpT", # Dog dance
    "55pXU6R2C1s52", # Cat
    "110Go1B0pES86Y", # Dog high five
    "uUAMzF6Cg2oE", # Pug
    "O4zR8z7P4jFqE", # Husky
    "3oEduO4hD4KjTLhj2g", # Baby Groot
    "Me0esTjGzB1v2", # Baymax
    "xT4uQulxzV39haRFjG", # Pusheen
    "l0HlO3HjXv0V9c6vS", # Pusheen dance
    "B3gZHW2bYjV84", # Cat typing
    "JIX9t2j0ZTN9S", # Cat
    "yBwgXMUvciZ2g", # Cat fast
    "W9PqETL76rK4E", # Happy dog
    "52eT0O6P63c7u" # Corgi
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"
valid_count = 0

for gid in gif_ids:
    if valid_count >= 20:
        break
        
    url = f"https://media.giphy.com/media/{gid}/giphy.gif"
    filename = f"cute_{valid_count + 1}.gif"
    filepath = os.path.join(dest_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        # Check if it's the "Content Not Available" placeholder (239321 bytes)
        if os.path.getsize(filepath) == 239321:
            os.remove(filepath)
            print(f"Skipped {gid} (Placeholder)")
        else:
            print(f"Successfully downloaded cute_{valid_count + 1}.gif")
            valid_count += 1
            
    except Exception as e:
        print(f"Failed {gid}: {e}")
    time.sleep(0.1)

print(f"Finished! Downloaded {valid_count} valid cute GIFs.")
