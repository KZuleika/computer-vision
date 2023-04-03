import cv2
import numpy as np

def findC(img):
    c = -1.5
    alto, ancho = img.shape
    for renglon in range (0,alto):
        for columna in range (0,ancho):
            if c < img[renglon][columna]:
                c = img[renglon][columna]
    return c
    

def changeContrast_gammaTransform(img, gamma):
    out = img.copy()
    alto, ancho = out.shape
    
    for renglon in range(0 , alto):
        for columna in range(0, ancho ):
            out[renglon][columna] =  np.power(out[renglon][columna]/255, gamma)*255
    out = out / findC(out) 
    cv2.imshow(windowName, out)

def on_change(value):
    value /= 100.0 * 1.0
    changeContrast_gammaTransform(ImagenGray, value)

windowName = 'image'
nomImage = "BajoContrasteGrises.jpg"
ImagenGray = cv2.imread(nomImage, 0)

cv2.imshow(windowName, ImagenGray)
cv2.createTrackbar('slider', windowName, 1, 400, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()

nomImage = "SobreeExpuestaGrises.jpg"
ImagenGray = cv2.imread(nomImage, 0)

cv2.imshow(windowName, ImagenGray)
cv2.createTrackbar('slider', windowName, 1, 400, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()

nomImage = "SubExpuestaGrises.jpg"
ImagenGray = cv2.imread(nomImage, 0)

cv2.imshow(windowName, ImagenGray)
cv2.createTrackbar('slider', windowName, 1, 400, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
