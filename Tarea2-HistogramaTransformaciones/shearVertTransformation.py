import cv2
import numpy as np

#Load image
ImageGray = cv2.imread("Bruno.jpg", 0)

#Obtener la forma de la matriz
m,n = ImageGray.shape
sv = 0.2      #Shear
shearVert = np.float32([[1,sv,0], [0,1,0]])
imgTransformed = cv2.warpAffine(ImageGray, shearVert, (n, m))

cv2.imshow('Imagen original',ImageGray)
cv2.imshow('imagen transformada',imgTransformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
