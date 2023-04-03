import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

captura = cv2.VideoCapture(1)
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    imagen = cv2.blur(imagen, (3, 3))
    #imagen = cv2.Canny(imagen, 20, 150)
    #ret,imagen = cv2.threshold(imagen,127,255,cv2.THRESH_OTSU)
        
    d = pytesseract.image_to_data(imagen, output_type=Output.DICT)
    text = pytesseract.image_to_string(imagen,lang='spa')
    
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('video', imagen)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
      print('Texto: ',text)
      break
  else: break
captura.release()
cv2.destroyAllWindows()
