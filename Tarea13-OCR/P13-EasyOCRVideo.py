import cv2
import easyocr
import time
from timeit import default_timer as timer

def eliminarLetras(texto):
    texto = texto.lower()
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O","U", "í")
    consonantes = ("b", "c", "d", "e", "f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    simbolos = ("|", "'","#","¡", "!", "@", "$","^", "&",",","?","¿",)
    for letra in vocales:
        out = texto.replace(letra, "")
    for letra in consonantes:
        out = texto.replace(letra, "")   
    for simbolo in simbolos:
        out = out.replace(simbolo, "")
    out = out.replace("_","-").replace("%/","%")
    return out

print("Creando OCR")
reader = easyocr.Reader(["en"], gpu = False)

print("Leyendo Imagen")
captura = cv2.VideoCapture(1)
firstimg = True

while (captura.isOpened()):
    ret, image = captura.read()
    if ret == True and firstimg == True:
        firstimg = False    
    elif ret == True and firstimg == False:
        startTimer = timer()
        SoloTexto = reader.readtext(image, paragraph=True, detail = 0)
        text = reader.readtext(image, paragraph = True) # Agrupa la salida en parrafos

        total_time = round(timer() - startTimer, 6)
        cv2.putText(image, str(total_time), (10,30), 2,1,(255,255,255),2)
        for Parrafo in text:
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
            texto = eliminarLetras(texto).replace(" ","*")
            resultado = eval(texto)
            print('texto: ', texto)
            cv2.putText(image, texto,pt0, 2,1,(180,0,180), 2)
            cv2.putText(image,'='+str(resultado), (pt2), 1,3,(100,0,255), 3)
            cv2.imshow("EasyOCR", image) 
        
        time.sleep(1.5)
        cv2.waitKey(0)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: 
        break
    
captura.release()
cv2.destroyAllWindows()

