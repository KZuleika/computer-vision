import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
#image = cv2.imread('imgColores.jpg')
#image = cv2.imread('imgBN.jpg')
image = cv2.imread('varios.jpg')

text = pytesseract.image_to_string(image,lang='spa')
print('Texto: ',text)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

