import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadGrayImage(nom):
    return cv2.imread(nom, 0)

def grayVector():
    a = np.zeros(256)
    for i in range (0, 256):
        a[i] = i
    return a

def findGrayFrequency(img, ):
    freqArray = np.zeros(256)
    n, m, = img.shape
    for i in range (0, n):
        for j in range (0, m):
            freqArray[img[i][j]] += 1
    return freqArray
        
def plotHistogram(x, y):
    plt.figure(figsize= (10,4))
    plt.bar(x= namevector, height= gray_frequency)
    plt.title('Histograma')
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.axvline(x = 60, color = 'yellow', linestyle = 'dashed', linewidth = 2)
    plt.axvline(x = 25, color = 'green', linestyle = 'dashed', linewidth = 2)
    plt.show()

def applyUmbral(img, umbral):
    out = img.copy()
    n, m = out.shape
    for i in range (0, n):
        for j in range(0, m):
            if umbral <= out[i][j]:
                out[i][j] = 1
            elif umbral > out[i][j]:
                out[i][j]=0
    return 255*out

def showMostBrilliantObj(img1,img2):
    out = img1.copy()
    n, m = out.shape
    for i in range (0, n):
        for j in range(0, m):
            if img1[i][j] > 0 and img1[i][j] > 0:
                out[i][j] = 1
            else:
                out[i][j]=0
    return out*255


namevector = grayVector()

ImageGray = loadGrayImage("LegosGrises 1.jpg")
gray_frequency = findGrayFrequency(ImageGray)
plotHistogram(namevector, gray_frequency)

umbral = np.array([60, 25])
out60 = applyUmbral(ImageGray, umbral[0])
cv2.imshow('umbral 60', out60)

out25 = applyUmbral(ImageGray, umbral[1])
cv2.imshow('umbral 25', out25)

cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('Original', ImageGray)

mostBrilliantImg = showMostBrilliantObj(out60, out25)
cv2.imshow('Objeto mas brillante', mostBrilliantImg)

cv2.waitKey(0)
cv2.destroyAllWindows()