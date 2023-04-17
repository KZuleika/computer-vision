import cv2
import easyocr
import time
from timeit import default_timer as timer

print("Creando OCR")
reader = easyocr.Reader(["es"], gpu = True)

print("Leyendo Imagen")
#image = cv2.imread('imgColores.jpg')
#image = cv2.imread('imgBN.jpg')
image = cv2.imread('operaciones/op3.jpg')
image = cv2.resize(image, (0,0), fx= 0.3, fy=0.3)

print("Analizando Texto")
#Texto = reader.readtext('chinese_tra.jpg')

startTimer = timer()
SoloTexto = reader.readtext(image, paragraph=True, detail = 0)
text = reader.readtext(image, paragraph = True) # Agrupa la salida en parrafos

total_time = round(timer() - startTimer, 6)
cv2.putText(image, str(total_time), (10,30), 2,1,(255,255,255),2)

print("Imprimiendo Resultados")
#La salida tiene el formato:
#[[X1, Y1], [X2, Y2], [X3, Y3], [X4, Y4]],'Texto Encontrado', Confianza si Paragraph = False
##[[X1, Y1], [X2, Y2], [X3, Y3], [X4, Y4]],'Texto Encontrado' si Paragraph = True
for Parrafo in text:
     print("Parrafo:", Parrafo)
     pt0 = Parrafo[0][0]
     pt1 = Parrafo[0][1]
     pt2 = Parrafo[0][2]
     pt3 = Parrafo[0][3]
     cv2.rectangle(image, pt0, pt2, (166, 56, 242), 1)
     cv2.circle(image, pt0, 2, (255, 0, 0), 2)
     cv2.circle(image, pt1, 2, (0, 255, 0), 2)
     cv2.circle(image, pt2, 2, (0, 0, 255), 2)
     cv2.circle(image, pt3, 2, (0, 255, 255), 2)
     texto = SoloTexto[text.index(Parrafo)]
     resultado = eval(texto)
     print('texto: ', texto)
     cv2.putText(image,'='+str(resultado), (pt2), 1,3,(100,0,255), 3)
     cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



