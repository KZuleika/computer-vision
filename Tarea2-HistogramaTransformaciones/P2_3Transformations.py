import cv2
import numpy as np

def identity_transformation(img):
    m,n = img.shape
    identity = np.float32([[1,0,0], [0,1,0]])
    imgTransformed = cv2.warpAffine(img, identity, (n, m))
    return imgTransformed

def scale_transformation(img, c):
    m, n = img.shape
    scale = np.float32([[c,0,0], [0,c,0]])
    imgTransformed = cv2.warpAffine(img, scale, (n, m))
    return imgTransformed

def rotational_transformation(img, theta):
    m,n = img.shape
    rotation = np.float32([[np.cos(theta),-np.sin(theta),0], [np.sin(theta),np.cos(theta),0]])
    imgTransformed = cv2.warpAffine(img, rotation, (n, m))
    return imgTransformed

def traslational_transformation(img, tx, ty):
    m,n = img.shape
    traslation = np.float32([[1,0,tx], [0,1,ty]])
    imgTransformed = cv2.warpAffine(img, traslation, (n, m))
    return imgTransformed

def shear_vertical(img, sv):
    m,n = img.shape
    shearVert = np.float32([[1,sv,0], [0,1,0]])
    imgTransformed = cv2.warpAffine(img, shearVert, (n, m))
    return imgTransformed

def shear_horizontal(img, sh):
    m,n = img.shape
    shearHor = np.float32([[1,0,0], [sh,1,0]])
    imgTransformed = cv2.warpAffine(img, shearHor, (n, m))
    return imgTransformed

def trapezoidal_transform(img):
    cv2.circle(img, (90, 50), 7, (255,0,0), 2)
    cv2.circle(img, (390, 50), 7, (0,255,0), 2)
    cv2.circle(img, (70, 440), 7, (0,0,255), 2)
    cv2.circle(img, (470, 420), 7, (255,255,0), 2)

    imgExtracct = np.float32([[90,50],[390,50],[70,440], [470,420]])
    imgSize = np.float32([[0,0],[508,0],[0,500], [508,500]])

    #Obtener la forma de la matriz
    m,n = img.shape
    trapezoidal = cv2.getPerspectiveTransform(imgExtracct, imgSize)
    imgTransformed = cv2.warpPerspective(img, trapezoidal, (n,m))
    return imgTransformed

#Titulos para imprimir imagenes
titles = ['identidad', 'escalamiento', 'rotacion', 'traslacion', 'shear vertical', 'shear horizontal','trapezoidal']
imgTransformed = []

#Cargar las imagenes
imgBruno = cv2.imread("Bruno.jpg", 0)
imgLibro = cv2.imread("Libro.jpg", 0)

cv2.imshow('Imagen original',imgBruno)



theta = 5 * np.pi /180 #radianes

imgTransformed.append(identity_transformation(imgBruno))
imgTransformed.append(scale_transformation(imgBruno, 2))
imgTransformed.append(rotational_transformation(imgBruno, theta))
imgTransformed.append(traslational_transformation(imgBruno, 33,22))
imgTransformed.append(shear_vertical(imgBruno, 0.2))
imgTransformed.append(shear_horizontal(imgBruno, 0.2))
imgTransformed.append(trapezoidal_transform(imgLibro))

for i in range(0, len(imgTransformed)):
    cv2.imshow('Imagen '+titles[i],imgTransformed[i])
    cv2.waitKey(0)
    if i + 2 >= len(imgTransformed):
        cv2.imshow('Imagen original', imgLibro)
    cv2.destroyWindow('Imagen '+titles[i])
    

cv2.destroyAllWindows()
