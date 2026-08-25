import os
import urllib.request

urls = [
    "https://media.giphy.com/media/l41JRsph73VokN6ik/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",
    "https://media.giphy.com/media/3o72FcJmLzIdYJqwDe/giphy.gif",
    "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
    "https://media.giphy.com/media/3oz8xAFtjouK9ScjEN/giphy.gif",
    "https://media.giphy.com/media/d31w24psGYecj95K/giphy.gif",
    "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "https://media.giphy.com/media/3oFzmf97Qkvw7vwuic/giphy.gif",
    "https://media.giphy.com/media/26n6R5HOYPbekK0YE/giphy.gif",
    "https://media.giphy.com/media/xT8qBhrlNooHBYR9f2/giphy.gif",
    "https://media.giphy.com/media/Lndtxw3ztLhNC/giphy.gif"
]

dest_dir = r"C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\assets\gifs"

# Start at 11 since we already downloaded 1-10
for i, url in enumerate(urls, start=11):
    filename = f"success_{i}.gif"
    filepath = os.path.join(dest_dir, filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")
