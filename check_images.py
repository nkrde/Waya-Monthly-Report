import pytesseract
from PIL import Image
import glob

for img_path in sorted(glob.glob('templates/*.png')):
    text = pytesseract.image_to_string(Image.open(img_path))
    # print the first 3 lines of text
    lines = [l for l in text.split('\n') if l.strip()]
    print(f"--- {img_path} ---")
    print('\n'.join(lines[:5]))
    print()
