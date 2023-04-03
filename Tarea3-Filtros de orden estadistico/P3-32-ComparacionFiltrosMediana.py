import cv2
import numpy as np

def create_window_as_vector(img, k, i_actual, j_actual):
    Cuadrado = (k // 2)
    lstImg = []
    for renglon in range(i_actual - Cuadrado, i_actual + Cuadrado+1):
        for columna in range(j_actual - Cuadrado, j_actual + Cuadrado + 1):
            lstImg.append(img[renglon,columna])
    vecVentana = np.array(lstImg)
    #print(vecVentana)
    return vecVentana


def create_window(img, k, i_actual, j_actual):
    Cuadrado = (k // 2)
    MatrizVentana = img[(i_actual - Cuadrado):(i_actual + Cuadrado + 1), (j_actual - Cuadrado):(j_actual + Cuadrado + 1)]
    return MatrizVentana


def median_filter(k):
    ind = 4
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            Pos_Med = (k * k)// 2
            v_plano = ventana.flatten() 
            v_plano.sort() 
            out[renglon][columna] = v_plano[Pos_Med]
    cv2.imshow('Filtro de mediana', out)

def median_adaptative_filter(k):
    out = np.zeros(imagen.shape, np.uint8)
    alto, ancho = out.shape
    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):   
            anchoVentana = k
            while(anchoVentana <= kMax):
                z = create_window_as_vector(imagen, anchoVentana, renglon, columna)
                mediana = np.median(z)
                minVent = z.min()
                maxVent = z.max()
                p1 = mediana - minVent
                p2 = mediana - maxVent
                #print(z, mediana, minVent, maxVent, p1, p2)
                if p1 > 0 and p2 < 0:
                #Zmed no es un impulso
                    q1 = imagen[renglon][columna] - minVent
                    q2 = imagen[renglon][columna] - maxVent
                    if q1 > 0 and q2 < 0:
                        out[renglon][columna] = imagen[renglon][columna]
                    else:
                        out[renglon][columna] = mediana
                    break
                else:
                #zmed es un impulso, hago mas grande la ventana
                    anchoVentana  = anchoVentana + 1
                    if anchoVentana <= kMax:
                        out[renglon][columna] = imagen[renglon][columna]
                    else:
                        break
            
    cv2.imshow(titleWin, out)   


imagen = cv2.imread('salpimienta.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#imagen = cv2.resize(imagen, (0,0), fx=0.4, fy=0.4)
cv2.imshow('Imagen Original', imagen)

titleWin = 'filtro adaptativo de mediana'
kMax = 35
cv2.imshow(titleWin, imagen)
cv2.createTrackbar('Ventana', titleWin, 3, 35, median_adaptative_filter)
cv2.waitKey(0)

cv2.imshow('Filtro de mediana', imagen)
cv2.createTrackbar('Ventana', 'Filtro de mediana', 3, 35, median_filter)

cv2.waitKey(0)
#cv2.destroyAllWindows()
