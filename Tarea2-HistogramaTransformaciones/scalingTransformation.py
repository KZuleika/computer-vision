import cv2
import numpy as np

#Load image
ImageGray = cv2.imread("Bruno.jpg", 0)

#Obtener la forma de la matriz
m,n = ImageGray.shape
c = 1.5      #Escalamiento

scale = np.float32([[c,0,0], [0,c,0]])
imgTransformed = cv2.warpAffine(ImageGray, scale, (n, m))

cv2.imshow('Imagen original',ImageGray)
cv2.imshow('imagen transformada',imgTransformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
