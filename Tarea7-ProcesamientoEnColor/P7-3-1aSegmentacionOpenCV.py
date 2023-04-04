import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import hsv_to_rgb

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

figurasImg = cv2.imread('Figuras de Colores.jpg')
figurasImg = cv2.resize(figurasImg, (0,0), fx= 0.2, fy=0.2)
figurasImg = cv2.cvtColor(figurasImg, cv2.COLOR_BGR2RGB)

plt.figure(1, (10,5))
plt.subplot(1, 3, 1)
plt.imshow(figurasImg)
plt.title("Figuras de colores")

hsv_figuras = cv2.cvtColor(figurasImg, cv2.COLOR_RGB2HSV)
light_orange = (12,190,200)
dark_orange = (20,255,255)

mask = cv2.inRange(hsv_figuras, light_orange, dark_orange)
result = cv2.bitwise_and(figurasImg, figurasImg, mask=mask)

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray")
plt.title("Mascara")

plt.subplot(1, 3, 3)
plt.imshow(result)
plt.title("Segmentacion")
plt.savefig('SegmentadaNaranja.png', dpi=600)

lo_square = np.full((10, 10, 3), light_orange, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_orange, dtype=np.uint8) / 255.0

plt.figure(2)
plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.title("Naranja claro")

plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.title("Naranja oscuro")
plt.show()
plt.savefig('ColoresNaranja.png', dpi=600)