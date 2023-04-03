import cv2
import numpy as np

def mean_filter(k):
    out = np.zeros(imagen.shape)
    out = cv2.copyMakeBorder(imagen, k//2, k//2, k//2, k//2, cv2.BORDER_CONSTANT)
    kernel = np.ones((k,k), np.float32) / (k**2)
    out = cv2.filter2D(imagen, -1, kernel)
    cv2.imshow(winTitle,out)
    return out

winTitle = 'Media'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    
    #imagen = cv2.resize(imagen, (0,0), fx= 0.5, fy=0.5)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('ventana', winTitle, 3, 50, mean_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
