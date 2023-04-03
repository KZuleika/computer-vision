import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

def apply_filter(val):
    derivada = cv2.getTrackbarPos('derivada',winTitle)
    operador = cv2.getTrackbarPos('operador', winTitle)
    #SOBEL
    if  operador == 0:
        txt = 'Sobel '
        #Derivada X
        if derivada == 0 :
            txt += 'derivada X'
            kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
        #Derivada Y
        else:
            txt += 'derivada Y'
            kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    #PREWIT
    elif operador == 1:
        txt = 'Prewitt '
        #Derivada X
        if derivada == 0 :
            txt += 'derivada X'
            kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        #Derivada Y
        else:
            txt += 'derivada Y'
            kernel = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    #SCHARR
    elif operador == 2:
        txt = 'Scharr '
         #Derivada X
        if derivada == 0 :
            txt += 'derivada X'
            kernel = np.array([[-3,0,3],[-10,0,10],[-3,0,3]])
        #Derivada Y
        else:
            txt += 'derivada Y'
            kernel = np.array([[-3,-10,-3],[0,0,0],[3,10,3]])
    
    out = cv2.filter2D(imagen,-1,kernel)
    out = abs(out)
    out = cv2.putText(out, txt, (20,20), font, 0.7, (255,255,255), 1)
    cv2.imshow(winTitle,out)
    return out



winTitle = 'Derivada con operadores'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('derivada', winTitle, 0,1, apply_filter)
        cv2.createTrackbar('operador',winTitle, 0,2, apply_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
