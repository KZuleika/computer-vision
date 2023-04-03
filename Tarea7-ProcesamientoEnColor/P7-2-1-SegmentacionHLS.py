import cv2
import matplotlib.pyplot as plt
import numpy as np

def segmentation(value):
    hMin = cv2.getTrackbarPos('Hmin', 'segmentada')
    hMax = cv2.getTrackbarPos('Hmax', 'segmentada')
    sMin = cv2.getTrackbarPos('Smin', 'segmentada')
    sMax = cv2.getTrackbarPos('Smax', 'segmentada')
    lMin = cv2.getTrackbarPos('Lmin', 'segmentada')
    lMax = cv2.getTrackbarPos('Lmax', 'segmentada')

        # ajustar valores máximos y minimos para ingresar a la máscara
    lower = np.array([hMin,  sMin, lMin])
    upper = np.array([hMax, sMax, lMax])
    mask = cv2.inRange(img, lower, upper)

    outimg = cv2.bitwise_and(img, img, mask=mask)
    outimg = cv2.cvtColor(outimg, cv2.COLOR_HLS2BGR)
    cv2.imshow('segmentada', outimg)
    cv2.imwrite('segmentadaHLSNaranja.jpg',outimg)
    return 

#IMAGEN EN RGB

#NomArchivo = 'Juguetes de Colores.jpg'
NomArchivo = 'Figuras de Colores.jpg'

img = cv2.imread(NomArchivo)

#img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

cv2.imshow('original', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)


cv2.imshow('segmentada', img)
cv2.createTrackbar('Hmin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Hmax', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Smin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Smax', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Lmin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Lmax', 'segmentada', 0, 255, segmentation)


cv2.setTrackbarPos('Hmax', 'segmentada',255)
cv2.setTrackbarPos('Smax', 'segmentada',255)
cv2.setTrackbarPos('Lmax', 'segmentada',255)



cv2.waitKey(0)
cv2.destroyAllWindows()