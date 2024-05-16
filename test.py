from PIL import Image
import pytesseract

filename = 'buy3.png'
img1 = Image.open(filename)
text = pytesseract.image_to_string(img1)

print(text)