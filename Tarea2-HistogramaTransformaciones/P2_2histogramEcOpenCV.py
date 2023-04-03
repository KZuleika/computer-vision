import cv2
import numpy as np
import matplotlib.pyplot as plt

def loadGrayImage(nom, window = 'Imagen original'):
    img = cv2.imread(nom, 0)
    cv2.imshow(window,img)
    return img

def plotHistogram(hist):
    dist = hist.cumsum()
    dist = dist * float(hist.max()) / dist.max()
    plt.figure(figsize= (10,4))
    plt.plot(dist, color='red')
    plt.xlim([0,256])
    plt.plot(hist, color= 'blue')
    plt.title('Histograma')
    plt.xlabel('Nivel de gris')
    plt.ylabel('Frecuencia')
    plt.grid(color = '#95a5a6', linestyle = '--', linewidth =2, axis='y', alpha = 0.7)
    plt.show()

def ecHistOpenCV(nomImage):
    ImageGray = loadGrayImage(nomImage)
    plotHistogram(cv2.calcHist(ImageGray, [0], None, [256], [0,256]))
    imgEc = cv2.equalizeHist(ImageGray)
    cv2.imshow('Ecualizacion del histograma', imgEc)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()



#Imagen Fig0316(1)(top_left).tif
ecHistOpenCV("Fig0316(1)(top_left).tif")

#Imagen Fig0316(3)(third_from_top).tif
ecHistOpenCV("Fig0316(3)(third_from_top).tif")

#Imagen Fig0316(4)(bottom_left).tif
ecHistOpenCV("Fig0316(4)(bottom_left).tif")

#Imagen Fig0320(1)(top_left).tif
ecHistOpenCV("Fig0320(1)(top_left).tif")

#Imagen Fig0323(a)(mars_moon_phobos) - copia.tif
ecHistOpenCV("Fig0323(a)(mars_moon_phobos) - copia.tif")

#Imagen  Fig0327(a)(tungsten_original).tif
ecHistOpenCV("Fig0327(a)(tungsten_original).tif")

#Imagen Fig0309(a)(washed_out_aerial_image).tif
ecHistOpenCV("Fig0309(a)(washed_out_aerial_image).tif")

