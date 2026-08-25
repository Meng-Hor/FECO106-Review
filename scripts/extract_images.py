import fitz
import os

pdf_files = [
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\material\Revision Exercise 1.pdf',
    r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\material\Revision Exercise 2.pdf'
]

out_dir = r'C:\Users\Ly Meng Hor ING\Documents\PERSONAL\CAMTECH\YEAR-01\TERM-03\FECO106\Mid-Term\material'

for pdf_path in pdf_files:
    pdf_name = os.path.basename(pdf_path).replace('.pdf', '')
    doc = fitz.open(pdf_path)
    img_index = 0
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        for img in image_list:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            img_filename = f"{pdf_name}_img_{img_index}.{image_ext}"
            with open(os.path.join(out_dir, img_filename), "wb") as f:
                f.write(image_bytes)
            print(f"Extracted {img_filename}")
            img_index += 1
