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


def exponential_noise(img, a = 0.1):
    out = img.copy()
    media = 1 / a
    varianza = 1/(a*a)
    for x in range(out.shape[0]):
        for y in range(out.shape[1]):
            p = random.random()
            if p>0:
                out[x][y] = np.log(p/a) / (-1 * a) -230
            else:
                out[x][y]=0
    print(out)   
    return out + img



#Load image
ImageGray = cv2.imread("sencilla.jpg", 0)
plotHistogram(cv2.calcHist(ImageGray, [0], None, [256], [0,256]))

noisyImg = exponential_noise(ImageGray)
plotHistogram(cv2.calcHist(noisyImg, [0], None, [256], [0,256]))

cv2.imshow('Imagen original', ImageGray)
cv2.imshow('Imagen con ruido', noisyImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
