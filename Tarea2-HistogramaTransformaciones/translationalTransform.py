import cv2
import numpy as np

#Load image
ImageGray = cv2.imread("Bruno.jpg", 0)

#Obtener la forma de la matriz
m,n = ImageGray.shape
tx = 12    #Translacion en X
ty = 5     #Translacion en Y

traslation = np.float32([[1,0,tx], [0,1,ty]])
imgTransformed = cv2.warpAffine(ImageGray, traslation, (n, m))

cv2.imshow('Imagen original',ImageGray)
cv2.imshow('imagen transformada',imgTransformed)

cv2.waitKey(0)
cv2.destroyAllWindows()