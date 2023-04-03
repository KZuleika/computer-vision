import cv2
import matplotlib.pyplot as plt
import numpy as np

def segmentation(value):
    rMin = cv2.getTrackbarPos('Rmin', 'segmentada')
    gMin = cv2.getTrackbarPos('Gmin', 'segmentada')
    bMin = cv2.getTrackbarPos('Bmin', 'segmentada')
    rMax = cv2.getTrackbarPos('Rmax', 'segmentada')
    gMax = cv2.getTrackbarPos('Gmax', 'segmentada')
    bMax = cv2.getTrackbarPos('Bmax', 'segmentada')

    minColor = np.array([rMin, gMin, bMin])
    maxColor = np.array([rMax, gMax, bMax])

    mask = cv2.inRange(img, minColor, maxColor)

    outimg = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('segmentada', outimg)
    cv2.imwrite('segmentadaRGBMorado.jpg',outimg)
    return 

#IMAGEN EN RGB
NomArchivo = 'Juguetes de Colores.jpg'
#NomArchivo = 'Figuras de Colores.jpg'

img = cv2.imread(NomArchivo)
img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
#img = cv2.resize(img, (0,0), fx=0.3, fy=0.3)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('original', img)

cv2.imshow('segmentada', img)
cv2.createTrackbar('Rmin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Rmax', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Gmin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Gmax', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Bmin', 'segmentada', 0, 255, segmentation)
cv2.createTrackbar('Bmax', 'segmentada', 0, 255, segmentation)

cv2.setTrackbarPos('Rmax', 'segmentada',255)
cv2.setTrackbarPos('Gmax', 'segmentada',255)
cv2.setTrackbarPos('Bmax', 'segmentada',255)



cv2.waitKey(0)
cv2.destroyAllWindows()