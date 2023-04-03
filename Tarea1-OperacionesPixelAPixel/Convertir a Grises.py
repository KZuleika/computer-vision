import cv2 as cv
import numpy as np

ImagenColor = cv.imread("Legos.jpg")
ImagenGray = cv.cvtColor(ImagenColor,cv.COLOR_BGR2GRAY)

cv.imshow('GalGadot Color',ImagenColor)
cv.imshow('GalGadot Grises',ImagenGray)

cv.waitKey(0)
cv.imwrite('LegosGrises.jpg',ImagenGray)
cv.destroyAllWindows()
