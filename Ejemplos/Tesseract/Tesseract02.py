import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#image = cv2.imread('imgColores.jpg')
#image = cv2.imread('imgBN.jpg')
image = cv2.imread('varios.jpg')
d = pytesseract.image_to_data(image, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('img', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
