import cv2
import numpy as np
import matplotlib.pyplot as plt

#Cargamos los elementos estructurantes 
kernel = []
kernel.append(cv2.getStructuringElement(cv2.MORPH_RECT,(11,11)))
kernel.append(cv2.getStructuringElement(cv2.MORPH_CROSS,(11,11)))
kernel.append(cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11)))

#Cargar la imagen original
imagenOriginal = [cv2.imread('karime.jpg', cv2.IMREAD_GRAYSCALE), 
                  cv2.imread('corazonPBlancos.jpg', cv2.IMREAD_GRAYSCALE), 
                  cv2.imread('corazonPNegros.jpg', cv2.IMREAD_GRAYSCALE),
                  cv2.imread('corazon.jpg', cv2.IMREAD_GRAYSCALE), ]
imgBinarizada = []

#Umbralizar la imagen original
for i in range(0, len(imagenOriginal)):
    _, aux= cv2.threshold(imagenOriginal[i],130,255,cv2.THRESH_BINARY)
    imgBinarizada.append(aux) 


#tophat
tophat = []
tophat.append(cv2.morphologyEx(imgBinarizada[0],cv2.MORPH_TOPHAT,kernel[0]))
tophat.append(cv2.morphologyEx(imgBinarizada[0],cv2.MORPH_TOPHAT,kernel[1]))
tophat.append(cv2.morphologyEx(imgBinarizada[0],cv2.MORPH_TOPHAT,kernel[2]))

plt.subplot(221),plt.imshow(imgBinarizada[0], cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(222),plt.imshow(tophat[0], cmap = 'gray')
plt.title('MORPH_RECT'), plt.xticks([]), plt.yticks([])

plt.subplot(223),plt.imshow(tophat[1], cmap = 'gray')
plt.title('MORPH_CROSS'), plt.xticks([]), plt.yticks([])

plt.subplot(224),plt.imshow(tophat[2], cmap = 'gray')
plt.title('MORPH_ELLIPSE'), plt.xticks([]), plt.yticks([])

plt.savefig("tophat11.png", dpi = 600)
plt.show()

print(kernel)