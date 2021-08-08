try:
    from PIL import Image
    from PIL import ImageFilter
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pdorai\AppData\Local\Tesseract-OCR\tesseract.exe'

#import cv2

tesseract_cmd = r'C:\Users\pdorai\AppData\Local\Tesseract-OCR'

imageObject = Image.open(r'C:\Users\pdorai\Desktop\IMX-Text Recognition\2700.PNG')

# imageObject = cv2.imread(r'C:\Users\pdorai\Desktop\IMX-Text Recognition\1404.PNG')

#tesseract imageObject res

sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened3 = sharpened2.filter(ImageFilter.SHARPEN);
sharpened4 = sharpened3.filter(ImageFilter.SHARPEN);
sharpened5 = sharpened4.filter(ImageFilter.SHARPEN);
sharpened6 = sharpened5.filter(ImageFilter.SHARPEN);
sharpened7 = sharpened6.filter(ImageFilter.SHARPEN);
sharpened8 = sharpened7.filter(ImageFilter.SHARPEN);
sharpened9 = sharpened8.filter(ImageFilter.SHARPEN);
sharpened10 = sharpened9.filter(ImageFilter.SHARPEN);
sharpened11 = sharpened10.filter(ImageFilter.SHARPEN);
sharpened12 = sharpened11.filter(ImageFilter.SHARPEN);
sharpened13 = sharpened12.filter(ImageFilter.SHARPEN);
sharpened14 = sharpened13.filter(ImageFilter.SHARPEN);
sharpened15 = sharpened14.filter(ImageFilter.SHARPEN);
sharpened16 = sharpened15.filter(ImageFilter.SHARPEN);
sharpened17 = sharpened16.filter(ImageFilter.SHARPEN);
sharpened18 = sharpened17.filter(ImageFilter.SHARPEN);
sharpened19 = sharpened18.filter(ImageFilter.SHARPEN);
sharpened20 = sharpened19.filter(ImageFilter.SHARPEN)

text = pytesseract.image_to_string(sharpened20, lang = 'eng')

print (text)
