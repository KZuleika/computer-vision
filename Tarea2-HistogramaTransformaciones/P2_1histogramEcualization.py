import cv2
import numpy as np
import matplotlib.pyplot as plt

#Devuelve un vector con la fercuenciad de cada nivel de gris
def findGrayFrequency(img):
    freqArray = np.zeros(256)
    n, m = img.shape
    for i in range (0, n):
        for j in range (0, m):
            freqArray[img[i][j]] += 1
    return freqArray

#Carga la iamgen con CV2
def loadGrayImage(nom):
    return cv2.imread(nom, 0)

#Crea el vector con el nombre de las intensidades de gris
def grayVector():
    a = np.zeros(256)
    for i in range (0, 256):
        a[i] = i
    return a
        
#Imprime el histograma en una ventana
def plotHistogram(x, y):
    plt.figure(figsize= (12,4))
    plt.bar(x= namevector, height= gray_frequency)
    plt.title('Histograma')
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.show()

#Crea el vector regla de asignacion
def assignationRule(freqArray):
    probability = np.zeros(256)
    probability[0] = freqArray[0]
    for k in range(1, 256):
        probability[k] = freqArray[k] + probability[k-1]
    probability /= probability.max()
    print(probability)
    return probability

#Aplica la ecualizacion del histograma
def HistogramEcualization(img, prob):
    out = img.copy()
    n, m = out.shape
    prob *= 255
    for i in range (0, n):
        for j in range(0, m):
            out[i][j] = prob[img[i][j]]
    return out


namevector = grayVector()


#Imagen Fig0316(1)(top_left).tif
ImageGray = loadGrayImage("Fig0316(1)(top_left).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)

#Imagen Fig0316(3)(third_from_top).tif
ImageGray = loadGrayImage("Fig0316(3)(third_from_top).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)


#Imagen Fig0316(4)(bottom_left).tif
ImageGray = loadGrayImage("Fig0316(4)(bottom_left).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)


#Imagen Fig0320(1)(top_left).tif
ImageGray = loadGrayImage("Fig0320(1)(top_left).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)

#Imagen Fig0323(a)(mars_moon_phobos) - copia.tif
ImageGray = loadGrayImage("Fig0323(a)(mars_moon_phobos) - copia.tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)


#Imagen Fig0327(a)(tungsten_original).tif
ImageGray = loadGrayImage("Fig0327(a)(tungsten_original).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)


#Imagen Fig0309(a)(washed_out_aerial_image).tif
ImageGray = loadGrayImage("Fig0309(a)(washed_out_aerial_image).tif")
cv2.imshow('imagen original',ImageGray)
gray_frequency = findGrayFrequency(ImageGray)
probRule= assignationRule(gray_frequency)
correctImage = HistogramEcualization(ImageGray, probRule)
cv2.imshow('imagen corregida',correctImage)
plotHistogram(namevector, gray_frequency)
