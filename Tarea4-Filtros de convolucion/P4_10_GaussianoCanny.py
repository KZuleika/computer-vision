import cv2
import numpy as np

def apply_filter(val):
    u1 = cv2.getTrackbarPos('umbral1', winTitle)
    u2 = cv2.getTrackbarPos('umbral2', winTitle)
    imgGauss = gaussian_filter(cv2.getTrackbarPos('ventana', 'gauss'))
    out = cv2.Canny(imgGauss, u1, u2)
    cv2.imshow(winTitle,out)
    return

def gaussian_filter(k):
    if k % 2 == 0:
        k+=1
    out = cv2.GaussianBlur(imagen, (k,k), 0)
    cv2.imshow('gauss',out)
    return out



winTitle = 'Canny'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    cv2.imshow('gauss',imagen)
    if i == 0:
        cv2.createTrackbar('ventana', 'gauss', 3,30, gaussian_filter)
        cv2.createTrackbar('umbral1',winTitle, 0,500, apply_filter)
        cv2.createTrackbar('umbral2',winTitle, 0,500, apply_filter)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
