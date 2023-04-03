import cv2
import numpy as np

#Load image
ImageGray = cv2.imread("Libro.jpg", 0)

cv2.circle(ImageGray, (90, 50), 7, (255,0,0), 2)
cv2.circle(ImageGray, (390, 50), 7, (0,255,0), 2)
cv2.circle(ImageGray, (70, 440), 7, (0,0,255), 2)
cv2.circle(ImageGray, (470, 420), 7, (255,255,0), 2)

imgExtracct = np.float32([[90,50],[390,50],[70,440], [470,420]])
imgSize = np.float32([[0,0],[508,0],[0,500], [508,500]])

#Obtener la forma de la matriz
m,n = ImageGray.shape
print(n,m)
sh = 0.2      #Shear
trapezoidal = cv2.getPerspectiveTransform(imgExtracct, imgSize)
imgTransformed = cv2.warpPerspective(ImageGray, trapezoidal, (n,m))

cv2.imshow('ImageGray original',ImageGray)
cv2.imshow('ImageGray transformada',imgTransformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
