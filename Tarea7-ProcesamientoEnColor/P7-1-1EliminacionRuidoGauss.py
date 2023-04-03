import cv2
import matplotlib.pyplot as plt
import numpy as np

#IMAGEN EN RGB
img = cv2.imread('Valle de la luna-adicion de ruido gaussiano.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
k = 7
kMax = 9

img_filtered = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

plt.savefig("ValleGauss.png", dpi = 600)
plt.show()

#IMAGEN EN RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
k = 7
kMax = 9

img_filtered = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

plt.savefig("ValleGaussHLS.png", dpi = 600)
plt.show()
