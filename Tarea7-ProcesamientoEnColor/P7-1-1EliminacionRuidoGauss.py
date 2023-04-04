import cv2
import matplotlib.pyplot as plt

#IMAGEN EN RGB
img = cv2.imread('Valle de la luna-adicion de ruido gaussiano.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_filtered = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

plt.savefig("ValleGauss.png", dpi = 600)
plt.show()

#IMAGEN EN HLS
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
img_filtered = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121),plt.imshow(img)
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

plt.savefig("ValleGaussHLS.png", dpi = 600)
plt.show()

img_hls2rgb = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
img_filtered_hls2rgb = cv2.cvtColor(img_filtered, cv2.COLOR_HLS2RGB)

plt.subplot(121),plt.imshow(img_hls2rgb)
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered_hls2rgb)
plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

plt.savefig("ValleGaussHLS2RGB.png", dpi = 600)
plt.show()