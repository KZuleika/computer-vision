import cv2
import numpy as np
import time

captura = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (255,255,196)
grosorLetra = 1

def calculate_and_show_total(img, numero, contador):
    total = np.array(numero) * contador
    total = total.sum()
    cv2.putText(img, 'TOTAL: $'+str(total),(10,30), font, tamañoLetra, colorLetra, grosorLetra)
    cv2.putText(img, 'MONEDAS: '+str(contador.sum()),(10,50), font, tamañoLetra, colorLetra, grosorLetra)

    for peso in range(len(numero)):
        cadena = '$' + str(numero[peso]) + ': '+ str(contador[peso])
        cv2.putText(img, cadena , (10,70+peso*20), font, tamañoLetra, colorLetra, grosorLetra)

    return

radiosPesosmin = np.array([19, 25, 31, 34, 37])
radiosPesosmax = np.array([24, 30, 33, 36, 44])
numero = [0.5, 1, 2, 5, 10]
contador = np.zeros(5, np.uint8) 

while (captura.isOpened()):
    ret, img = captura.read()
    if ret == True:
        cv2.imwrite('houghOriginal.jpg', img)
        src = cv2.medianBlur(img, 5)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=20, maxRadius=65)

        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # dibujar circulo 
            cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
            # dibujar centro
            cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
            radio = i[2]
            for peso in range(len(numero)):
                if radiosPesosmin[peso] <= radio <= radiosPesosmax[peso]:
                    cv2.putText(img, str(numero[peso]),(i[0], i[1]), font, tamañoLetra, colorLetra, grosorLetra)
                    #cv2.putText(img,'r'+str(radio),(i[0], i[1]+20), font, tamañoLetra, colorLetra, grosorLetra)
                    contador[peso] +=1
                    #print(numero[peso],": ", radio)
                    break
        calculate_and_show_total(img, numero, contador)
        contador = np.zeros(5, np.uint8)
        
        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        time.sleep(0.1)
    else: break

captura.release()
cv2.destroyAllWindows()



