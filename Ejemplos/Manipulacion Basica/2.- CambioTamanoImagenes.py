import cv2
import numpy as np
import imutils 

font = cv2.FONT_HERSHEY_SIMPLEX
# Cambiar Tamaño usando OpenCV
# cv.INTER_NEAREST
# cv.INTER_LINEAR
# cv.INTER_CUBIC
# cv.INTER_AREA
# cv.INTER_LANCZOS4
# cv.INTER_LINEAR_EXACT

ImagenColor = cv2.imread("GalGadot.jfif")
ResizedImg1 = cv2.resize(ImagenColor,(600,150), interpolation = cv2.INTER_LINEAR_EXACT)
ResizedImg2 = cv2.resize(ImagenColor, (0,0), fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR_EXACT)

Filas, Columnas, Canales = ImagenColor.shape
cv2.putText(ImagenColor,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)
Filas, Columnas, Canales = ResizedImg1.shape
cv2.putText(ResizedImg1,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)
Filas, Columnas, Canales = ResizedImg2.shape
cv2.putText(ResizedImg2,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('GalGadot Original',ImagenColor )
cv2.imshow('GalGadot 600x150',ResizedImg1)
cv2.imshow('GalGadot 50%',ResizedImg2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Cambiar Tamaño Usando imutils
# NOTA: Para instalar imutils  puedes usar pip install imutils.
ImagenColor = cv2.imread("GalGadot.jfif")
ResizedImg1 = imutils.resize(ImagenColor,height=300)
ResizedImg2 = imutils.resize(ImagenColor,width=300)

Filas, Columnas, Canales = ImagenColor.shape
cv2.putText(ImagenColor,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)
Filas, Columnas, Canales = ResizedImg1.shape
cv2.putText(ResizedImg1,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)
Filas, Columnas, Canales = ResizedImg2.shape
cv2.putText(ResizedImg2,('ImageSize: %dx%d'%(Filas, Columnas)),(10,15), font, 0.5,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('GalGadot Original',ImagenColor)
cv2.imshow('GalGadot Alto=300',ResizedImg1)
cv2.imshow('GalGadot Ancho=300',ResizedImg2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

# Recortar
ImagenColor = cv2.imread("GalGadot.jfif")
Recortada = ImagenColor[50:850,250:750]
cv2.imshow('GalGadot Original',ImagenColor)
cv2.imshow('GalGadot Recortada',Recortada)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Transformar
ImagenColor = cv2.imread("GalGadot512x256.jpg")
cv2.imshow('GalGadot512x256',ImagenColor)

cv2.waitKey(0)
cv2.destroyAllWindows()

