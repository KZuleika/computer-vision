import cv2
import numpy as np
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def ordenar_puntos(puntos):
    n_puntos = np.concatenate([puntos[0], puntos[1], puntos[2], puntos[3]]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos: n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order: x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order: x2_order[0])
    
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

captura = cv2.VideoCapture(1)
while (captura.isOpened()):
  ret, image = captura.read()
  if ret == True:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2. medianBlur(gray, 7)
    canny = cv2.Canny(gray, 10, 150)
    canny = cv2.dilate(canny, None, iterations=1)
    cv2.imshow('canny', canny)
    cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]

    for c in cnts:
        epsilon = 0.01*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        
        if len(approx)==4:
            cv2.drawContours(image, [approx], 0, (0,255,255),2)
            
            puntos = ordenar_puntos(approx)
            cv2.circle(image, tuple(puntos[0]), 7, (255,0,0), 2)
            cv2.circle(image, tuple(puntos[1]), 7, (0,255,0), 2)
            cv2.circle(image, tuple(puntos[2]), 7, (0,0,255), 2)
            cv2.circle(image, tuple(puntos[3]), 7, (255,255,0), 2)

            pts1 = np.float32(puntos)
            pts2 = np.float32([[0,0],[200,0],[0,100],[200,100]])
            M = cv2.getPerspectiveTransform(pts1,pts2)
            dst = cv2.warpPerspective(gray,M,(200,100))
            cv2.imshow('dst', dst)
            texto = pytesseract.image_to_string(dst, lang='spa')
            print('texto: ', texto)
            if len(texto) > 0:
                resultado = eval(texto)
                cv2.putText(image, str(resultado), (puntos[3]), 2,2,(0,0,255), 3)
    
    cv2.imshow('Image', image)        
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()
