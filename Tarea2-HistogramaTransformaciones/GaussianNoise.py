import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def plotHistogram(hist, title = 'Histograma'):
    plt.figure(figsize= (10,4))
    plt.plot(hist, color= 'orange')
    plt.title(title)
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.show()

def gaussProbability(p, media, std):
    varianza = std * std
    coef = abs(np.log(p * np.sqrt(2 * np.pi) * std))
    if random.random() > 0.5:
        z = media - np.sqrt(2 * varianza * coef) + media
    else:
        z = std + np.sqrt(2 * varianza * coef)
    return z

def addGaussianNoise(img, media = 30, std = 10):
    out = img.copy()

    #pixeles modificados
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            p = random.random()
            #print(p)
            out[x][y]= gaussProbability(p, media, std) +out[x][y]
        
    return out



#Load image
ImageGray = cv2.imread("sencilla.jpg", 0)
plotHistogram(cv2.calcHist(ImageGray, [0], None, [256], [0,256]))

noisyImg = addGaussianNoise(ImageGray, 30,10)
plotHistogram(cv2.calcHist(noisyImg, [0], None, [256], [0,256]))

cv2.imshow('Imagen original', ImageGray)
cv2.imshow('Imagen con ruido', noisyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
