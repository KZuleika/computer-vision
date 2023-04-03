import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

def apply_filter(operador):
    #Sobel
    if operador == 0:
        txt = 'Sobel'
        dx = cv2.Sobel(imagen,cv2.CV_64F,1,0,ksize=3)
        dy = cv2.Sobel(imagen,cv2.CV_64F,0,1,ksize=3)
    #Prewitt
    elif operador == 1:
        txt = 'Prewitt' 
        kernelX =  np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
        kernelY = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
        
        dx = cv2.filter2D(imagen,-1,kernelX)
        dy = cv2.filter2D(imagen,-1, kernelY)
    
    out = np.uint8(np.sqrt(np.power(dx,2)+np.power(dy,2)))
    out = cv2.putText(out, txt, (20,20), font, 0.7, (255,255,255), 1)
    cv2.imshow(winTitle,out)
    return out


winTitle = 'Gradiente'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('operador',winTitle, 0,1, apply_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
