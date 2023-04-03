import cv2

def changeRes_NearestNeighbour_Inter(imgName, aspecRatio):
    return cv2.resize(imgName, (0,0), fx=aspecRatio, fy=aspecRatio, interpolation= cv2.INTER_NEAREST)

def changeRes_Bilinear_Inter(imgName, aspecRatio):
    return cv2.resize(imgName, (0,0), fx=aspecRatio, fy=aspecRatio, interpolation= cv2.INTER_LINEAR)

def changeRes_Bicubic_Inter(imgName, aspecRatio):
    return cv2.resize(imgName, (0,0), fx=aspecRatio, fy=aspecRatio, interpolation= cv2.INTER_CUBIC)

nomImage = "Casa.jpg"
ImagenGray = cv2.imread(nomImage, 0)

#nearest neighbour interpolation
ResizedImg15= changeRes_NearestNeighbour_Inter(ImagenGray, 1.5)
ResizedImg05 = changeRes_NearestNeighbour_Inter(ImagenGray, 0.5)
ResizedImg025= changeRes_NearestNeighbour_Inter(ImagenGray, 0.25)
ResizedImg0125 = changeRes_NearestNeighbour_Inter(ImagenGray, 0.125)

cv2.imshow('casa original',ImagenGray)
cv2.imshow('casa 150%',ResizedImg15)
cv2.imshow('casa 50%',ResizedImg05)
cv2.imshow('casa 25%',ResizedImg025)
cv2.imshow('casa 12.5%',ResizedImg0125)

cv2.waitKey(0)
cv2.destroyAllWindows()

#linear interpolation
ResizedImg15= changeRes_Bilinear_Inter(ImagenGray, 1.5)
ResizedImg05 = changeRes_Bilinear_Inter(ImagenGray, 0.5)
ResizedImg025= changeRes_Bilinear_Inter(ImagenGray, 0.25)
ResizedImg0125 = changeRes_Bilinear_Inter(ImagenGray, 0.125)

cv2.imshow('casa original',ImagenGray)
cv2.imshow('casa 150%',ResizedImg15)
cv2.imshow('casa 50%',ResizedImg05)
cv2.imshow('casa 25%',ResizedImg025)
cv2.imshow('casa 12.5%',ResizedImg0125)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Bicubic interpolation
ResizedImg15= changeRes_Bicubic_Inter(ImagenGray, 1.5)
ResizedImg05 = changeRes_Bicubic_Inter(ImagenGray, 0.5)
ResizedImg025= changeRes_Bicubic_Inter(ImagenGray, 0.25)
ResizedImg0125 = changeRes_Bicubic_Inter(ImagenGray, 0.125)

cv2.imshow('casa original',ImagenGray)
cv2.imshow('casa 150%',ResizedImg15)
cv2.imshow('casa 50%',ResizedImg05)
cv2.imshow('casa 25%',ResizedImg025)
cv2.imshow('casa 12.5%',ResizedImg0125)

cv2.waitKey(0)
cv2.destroyAllWindows()


