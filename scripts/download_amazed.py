import os
import urllib.request
import time

gif_ids = [
    "26ufdipQqU2lhNA4g", "5vkDAdM8F980E", "vQqeT3AYg8S5O", "tfUW8mhiFk8NlJhgEh",
    "ToMjGpnXBTw7vnokxhu", "cL4pqu8GGRIihabgSM", "xT0xeJpnrWC4XWblEk", "3o6Zt8rGMqVwjYAlsA",
    "26tn33aiTi1jSqLp6", "8sZXkUPVwka3u", "l0HlHoE2qEACXQcAE", "1pooFlqcmEz9AgNeRZ",
    "3o72F8t9TDi2xVnxOE", "l4Ho0At2UD2d7WyD6", "FbiL9rsmZN3ib2JSGo", "b8RfbQFaOs1rO10ren",
    "5ttRvCRSnVKZeiMWqy", "3o85xwxr06YNoFdSbm", "U2O50cAkpmTjG", "wbcMnfHqOJX9K",
    "xUPGcz2H1TXdCz4suY", "V2AkNZZi9ygbm", "3oEjI6SIIHBdRxXI40", "xT0GqfvuVpNqEf3z2w",
    "l2SpMUEMRSjKk50pG", "3o7btQMdCE56kI", "l2Sq29cFXoF80ADlK", "xT77XWum9yH7zNkFW0",
    "21GCae4djDWtP5soiY", "NnGGHE0muVqpO"
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"
valid_count = 0

for gid in gif_ids:
    if valid_count >= 20:
        break
        
    url = f"https://media.giphy.com/media/{gid}/giphy.gif"
    filename = f"amazed_{valid_count + 1}.gif"
    filepath = os.path.join(dest_dir, filename)
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        # Check if it's the "Content Not Available" placeholder
        if os.path.getsize(filepath) == 239321:
            os.remove(filepath)
            print(f"Skipped {gid} (Placeholder)")
        else:
            print(f"Successfully downloaded amazed_{valid_count + 1}.gif")
            valid_count += 1
            
    except Exception as e:
        print(f"Failed {gid}: {e}")
    time.sleep(0.1)

print(f"Finished! Downloaded {valid_count} valid amazed GIFs.")
