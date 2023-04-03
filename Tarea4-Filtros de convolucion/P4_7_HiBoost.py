import cv2
import numpy as np

def apply_filter(val):
    operador = cv2.getTrackbarPos('operador', winTitle)
    A = cv2.getTrackbarPos('A', winTitle) / 10
    print(A)
    if  operador == 0:
        kernel = np.array([[0,-1,0],[-1,A+4,-1],[0,-1,0]])
    elif operador == 1:
       kernel = np.array([[-1,-1,-1],[-1,A+8,-1],[-1,-1,-1]])
    out = cv2.filter2D(imagen,-1,kernel)
    cv2.imshow(winTitle,out)
    return out



winTitle = 'HiBoost'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('operador',winTitle, 0, 1, apply_filter)
        cv2.createTrackbar('A',winTitle, 5, 30, apply_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
