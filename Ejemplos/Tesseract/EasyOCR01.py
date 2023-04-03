import cv2
import easyocr
print("Creando OCR")
reader = easyocr.Reader(["es"], gpu = True)

print("Leyendo Imagen")
#image = cv2.imread('imgColores.jpg')
#image = cv2.imread('imgBN.jpg')
image = cv2.imread('varios.jpg')

print("Analizando Texto")
#Texto = reader.readtext('chinese_tra.jpg')

SoloTexto = reader.readtext(image, paragraph=True, detail = 0)
text = reader.readtext(image, paragraph = True) # Agrupa la salida en parrafos
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
     cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()



