import cv2
import numpy as np
import math
import time

captura = cv2.VideoCapture(1)

font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (255,0,255)
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

epsilon = 350
areaspesos = [1730, 2630, 3250, 4000, 4750]
numero = [0.5, 1, 2, 5, 10]
contador = np.zeros(5, np.uint8)

while (captura.isOpened()):
    ret, img = captura.read()

    if ret == True:
        src = cv2.medianBlur(img, 9)
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _, aux = cv2.threshold(src,50,255,cv2.THRESH_BINARY)
        aux = 255 - aux
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
        aux = cv2.morphologyEx(aux, cv2.MORPH_CLOSE, kernel)

        n_components, output, stats, centroids = cv2.connectedComponentsWithStats(aux, 
                                                                                  connectivity=8, 
                                                                                  ltype=cv2.CV_32S)
        #print(n_components)
        for i in range(n_components):
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            area = stats[i, cv2.CC_STAT_AREA]
            centro = (int(centroids[i, cv2.CC_STAT_LEFT]),int(centroids[i, cv2.CC_STAT_TOP]))
            #print(area)
            #print('x:',x,y,w,h,area, centro)
            for peso in range(len(areaspesos)):
                if abs(area - areaspesos[peso]) <= epsilon:
                    radio = int(math.sqrt(area / math.pi))
                    cv2.circle(img, centro, radio, (0,255,0), 2)
                    cv2.putText(img, str(numero[peso]),centro, font, tamañoLetra, colorLetra, grosorLetra)
                    contador[peso] +=1
                    break
                    #print(numero[peso],": ", area)

        calculate_and_show_total(img, numero, contador)
        contador = np.zeros(5, np.uint8)

        cv2.imshow('video', img)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
        time.sleep(1)
    else: break
captura.release()
cv2.destroyAllWindows()



