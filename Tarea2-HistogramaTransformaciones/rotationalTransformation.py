import cv2
import numpy as np

#Load image
ImageGray = cv2.imread("Bruno.jpg", 0)

#Obtener la forma de la matriz
m,n = ImageGray.shape
theta = 5 * np.pi /180 #radianes

rotation = np.float32([[np.cos(theta),-np.sin(theta),0], [np.sin(theta),np.cos(theta),0]])
imgTransformed = cv2.warpAffine(ImageGray, rotation, (n, m))

cv2.imshow('Imagen original',ImageGray)
cv2.imshow('imagen transformada',imgTransformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
