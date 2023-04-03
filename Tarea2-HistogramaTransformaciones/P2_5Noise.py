import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
     
#Crea el vector con el nombre de las intensidades de gris
def grayVector():
    a = np.zeros(256)
    for i in range (0, 256):
        a[i] = i
    return a
        
#Imprime el histograma en una ventana
def plotHistogram(img, title = 'Histograma'):
    freqArray = np.zeros(256)
    n, m = img.shape
    for i in range (0, n):
        for j in range (0, m):
            freqArray[img[i][j]] += 1

    plt.figure(figsize= (8,4))
    plt.bar(x= levelGray, height= freqArray)
    plt.title(title)
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.show()


def gaussian_noise(img, mean, std):
    out = img.copy()
    out = out.astype(float) / 255.0
    noise = np.random.normal(loc= mean, scale=std, size=out.shape)
    out = out + noise

    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out

def rayleigh_noise(img, a, b):
    out = img.copy()
    out = out.astype(float) / 255.0

    noise = np.zeros(out.shape, float)

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            p = random.random()
            noise[i][j] = a + np.sqrt(- b* np.log(1-p))

    out = out + noise
    out = np.uint8(out*255)
    return out

def exponential_noise(img, a):
    out = img.copy()
    out = out.astype(float) / 255.0
    noise = np.zeros(out.shape, float)
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            p = random.random()
            noise[i][j] = - 1 * np.log(1 - p)/a

    out = out + noise
    out = np.uint8(out*255)
    return out

def SaltPepper_Noise(img, pSalt, pPepper):
    out = img.copy()
    pSalt = 1 - pSalt
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            p = random.random()
            if p < pPepper:
                out[i][j] = 0
            elif p > pSalt:
                out[i][j] = 255                

    return out

levelGray = grayVector()
img = cv2.imread("sencilla.jpg", 0)

cv2.imshow('Imagen original', img)
plotHistogram(img, 'Histograma imagen original')

cv2.waitKey(0)
cv2.destroyAllWindows()

noisyImg = []
titleNoise = ['Gauss', 'Ryleigh', 'Exponencial', 'sal y pimienta']

noisyImg.append(gaussian_noise(img, -0.02, 0.01))
noisyImg.append(rayleigh_noise(img, 0, 0.001))
noisyImg.append(exponential_noise(img, 50))
noisyImg.append(SaltPepper_Noise(img, 0.05, 0.05))

for i in range(len(noisyImg)):
    cv2.imshow('Imagen con ruido '+titleNoise[i], noisyImg[i])
    #plotHistogramCV(cv2.calcHist(noisyImg[0], [0], None, [256], [0,256]), 'Histograma ruido '+titleNoise[i])
    plotHistogram(noisyImg[i], 'Histograma de imagen con ruido '+ titleNoise[i])
    cv2.waitKey(0)
    cv2.destroyWindow('Imagen con ruido '+titleNoise[i])

cv2.waitKey(0)
cv2.destroyAllWindows()