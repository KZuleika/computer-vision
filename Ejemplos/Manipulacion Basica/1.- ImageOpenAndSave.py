import cv2
import numpy as np

ImagenColor = cv2.imread("GalGadot.jfif")
ImagenGray = cv2.imread("GalGadot.jfif", 0)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(ImagenColor,'Texto En Rojo->',(100,100), font, 0.5,(0,0,255),1,cv2.LINE_AA)
cv2.putText(ImagenGray,'Texto En Gris->',(100,100), font, 0.5,128,1,cv2.LINE_AA)

cv2.imshow('GalGadot Color',ImagenColor)
cv2.imshow('GalGadot Grises',ImagenGray)


cv2.waitKey(0)
cv2.imwrite('Grises.jpg',ImagenGray)
cv2.destroyAllWindows()

