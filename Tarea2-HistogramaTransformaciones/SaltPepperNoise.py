#https://pythoneyes.wordpress.com/2017/06/23/anadir-ruido-a-imagenes-con-python/

import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def addSaltPepperNoise(img, percentage):
    out = img.copy()

    totalPx = out.shape[0] * out.shape[1]
    nPixels=(totalPx*percentage)//800
 
    black = 0
    white = 255
 
    #pixeles blancos
    for x in range(nPixels):
 
        x=random.randrange(2, out.shape[0]-2)
        y=random.randrange(2, out.shape[1]-2)

        out[x][y]= white
        out[x+1][y]= white
        out[x][y+1]= white
        out[x+1][y+1]= white
 
    #pixeles negros
    for x in range(nPixels):
 
        x=random.randrange(2, out.shape[0]-2)
        y=random.randrange(2, out.shape[1]-2)
 
        out[x][y]= black
        out[x+1][y]= black
        out[x][y+1]= black
        out[x+1][y+1]= black
 
 
    return out


def plotHistogram(hist, title = 'Histograma'):
    plt.figure(figsize= (10,4))
    plt.plot(hist, color= 'orange')
    plt.title(title)
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.show()

#Load image
ImageGray = cv2.imread("sencilla.jpg", 0)

#Obtener la forma de la matriz
noisyImg = addSaltPepperNoise(ImageGray, 10)

#Imprimir los histogramas
plotHistogram(cv2.calcHist(ImageGray, [0], None, [256], [0,256]), 'Imagen Original')
plotHistogram(cv2.calcHist(noisyImg, [0], None, [256], [0,256]), 'Imagen con ruido')


#Imprimir las imges
cv2.imshow('out original', ImageGray)
cv2.imshow('out con ruido', noisyImg)

cv2.waitKey(0)
cv2.destroyAllnPixels()
