import cv2
import numpy as np

def gaussian_filter(k):
    if k % 2 == 0:
        k+=1
    out = cv2.GaussianBlur(imagen, (k,k), 0)
    cv2.imshow(winTitle,out)
    return out


winTitle = 'Gaussiano'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('ventana', winTitle, 5, 50, gaussian_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
