import cv2
import numpy as np
import matplotlib.pyplot as plt

#Cargamos los elementos estructurantes 
kernel = []
kernel.append(cv2.getStructuringElement(cv2.MORPH_RECT,(7,7)))
kernel.append(cv2.getStructuringElement(cv2.MORPH_CROSS,(7,7)))
kernel.append(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))

#Cargar la imagen original
imagenOriginal = [cv2.imread('karime.jpg', cv2.IMREAD_GRAYSCALE), 
                  cv2.imread('corazonPuntitos.jpg', cv2.IMREAD_GRAYSCALE), 
                  cv2.imread('corazonPuntitosnegros.jpg', cv2.IMREAD_GRAYSCALE)]
imgBinarizada = []

#Umbralizar la imagen original
for i in range(0, 3):
    _, aux= cv2.threshold(imagenOriginal[i],130,255,cv2.THRESH_BINARY)
    imgBinarizada.append(aux) 

#Erosion
erosion = []
erosion.append(cv2.erode(imgBinarizada[0],kernel[0],iterations = 1))
erosion.append(cv2.erode(imgBinarizada[0],kernel[1],iterations = 1))
erosion.append(cv2.erode(imgBinarizada[0],kernel[2],iterations = 1))

plt.subplot(221),plt.imshow(imgBinarizada[0], cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(erosion[0], cmap = 'gray')
plt.title('MORPH_RECT'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(erosion[1], cmap = 'gray')
plt.title('MORPH_CROSS'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(erosion[2], cmap = 'gray')
plt.title('MORPH_ELIPSE'), plt.xticks([]), plt.yticks([])

plt.savefig("erosion.png", dpi = 600)
plt.show()


#Desplezar las imagenes
for i in range(0, 3):
    cv2.imshow('original', imgBinarizada[i])
    cv2.waitKey(0)

print(kernel)