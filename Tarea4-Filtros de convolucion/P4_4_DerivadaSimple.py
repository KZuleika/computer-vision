import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

def apply_filter(derivada):
    if  derivada == 0:
        txt = 'derivada en X'
        kernel = np.array([[-1,1]])
    elif derivada == 1:
        txt = 'derivada en Y'
        kernel = np.array([[-1],[1]])
    elif derivada == 2:
        txt = 'derivada diagonal 1'
        kernel = np.array([[-1,0],[0,1]])
    elif derivada == 3:
        txt = 'derivada diagonal 2'
        kernel = np.array([[0,-1],[1,0]])
    
    out = abs(cv2.filter2D(imagen, -1, kernel))
    out = cv2.putText(out, txt, (20,20), font, 0.7, (255,255,255), 1)
    #cv2.getDerivKernels()
    #print(out.shape, imagen.shape)
    cv2.imshow(winTitle,out)
    return out



winTitle = 'Derivada simple'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('derivada', winTitle, 0,3, apply_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
