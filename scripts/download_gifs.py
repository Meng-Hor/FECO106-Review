import os
import urllib.request

urls = [
    "https://media.giphy.com/media/g9582DNuQppxC/giphy.gif", # Gatsby
    "https://media.giphy.com/media/11sBLVxNs7v6WA/giphy.gif", # Minions
    "https://media.giphy.com/media/nXXU1DVGVAD60/giphy.gif", # Dwight
    "https://media.giphy.com/media/xTiQyBOIQe5cgiyUPS/giphy.gif", # Jonah Hill
    "https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif", # Success Kid
    "https://media.giphy.com/media/132710H339M15m/giphy.gif", # Will Smith
    "https://media.giphy.com/media/3o7qDSOvfaCO9b3CdO/giphy.gif", # Obama
    "https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif", # Cat thumbs up
    "https://media.giphy.com/media/NnGGHE0muVqpO/giphy.gif", # The Rock
    "https://media.giphy.com/media/BI3bNv1NJMC7YzhhXc/giphy.gif" # Chuck Norris
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

for i, url in enumerate(urls):
    filename = f"success_{i+1}.gif"
    filepath = os.path.join(dest_dir, filename)
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
