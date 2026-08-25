from PIL import Image, ImageDraw
import re

# 1. Image Rounding
img_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\dog_icon.png'
out_path = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\dog_icon_rounded.png'

# Open original image and ensure it's RGBA
img = Image.open(img_path).convert("RGBA")
w, h = img.size

# The user loves 1.5rem squircle corners. Let's do a radius of about 25% of the size.
radius = int(min(w, h) * 0.25)

# Create a rounded rectangle mask
mask = Image.new('L', (w, h), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle((0, 0, w, h), radius=radius, fill=255)

# Apply mask
rounded_img = Image.new('RGBA', (w, h))
rounded_img.paste(img, (0, 0), mask=mask)

# Save the new icon
rounded_img.save(out_path, "PNG")

# 2. Update HTML files
def update_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Update favicon
    html = html.replace('href="dog_icon.png"', 'href="dog_icon_rounded.png"')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

update_file(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\index.html')
update_file(r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\web\quiz.html')

print("Created rounded favicon and updated HTML!")
