import cv2
import numpy as np


def changeRes_NearestNeighbour_Inter(imgName, aspecRatio):
    ResizedImg15= cv2.resize(imgName, (0,0), fx=aspecRatio, fy=aspecRatio, interpolation= cv2.INTER_NEAREST)


nomImage = "Casa.jpg"

ImagenColor = cv2.imread(nomImage)
ImagenGray = cv2.imread(nomImage, 0)

font = cv2.FONT_HERSHEY_SIMPLEX

plt.imshow('Casa Color (tamaño original)',ImagenColor)
plt.imshow('Casa Grises (tamaño original)',ImagenGray)

cv2.waitKey(0)
cv2.destroyAllWindows()

#nearest neighbour interpolation
ResizedImg15= cv2.resize(ImagenGray, (0,0), fx=1.5, fy=1.5, interpolation= cv2.INTER_NEAREST)
ResizedImg05 = cv2.resize(ImagenGray, (0,0), fx=0.5, fy=0.5, interpolation = cv2.INTER_NEAREST)
ResizedImg025= cv2.resize(ImagenGray, (0,0), fx=0.25, fy=0.25, interpolation= cv2.INTER_NEAREST)
ResizedImg0125 = cv2.resize(ImagenGray, (0,0), fx=0.125, fy=0.125, interpolation = cv2.INTER_NEAREST)

cv2.imshow('casa 150%',ResizedImg15)
cv2.imshow('casa 50%',ResizedImg05)
cv2.imshow('casa 25%',ResizedImg025)
cv2.imshow('casa 12.5%',ResizedImg0125)

cv2.waitKey(0)
cv2.destroyAllWindows()

#linear interpolation
ResizedImg15 = cv2.resize(ImagenGray, (0,0), fx=1.5, fy=1.5, interpolation= cv2.INTER_LINEAR_EXACT)
ResizedImg05 = cv2.resize(ImagenGray, (0,0), fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR_EXACT)

cv2.imshow('casa 150%',ResizedImg15)
cv2.imshow('casa 50%',ResizedImg05)


cv2.waitKey(0)
cv2.destroyAllWindows()

