import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import hsv_to_rgb
from matplotlib.colors import rgb_to_hsv

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

juguetesImg = cv2.imread('Juguetes de Colores.jpg')
juguetesImg = cv2.resize(juguetesImg, (0,0), fx= 0.2, fy=0.2)
juguetesImg = cv2.cvtColor(juguetesImg, cv2.COLOR_BGR2RGB)

plt.figure(1, (10,5))
plt.subplot(1, 3, 1)
plt.imshow(juguetesImg)
plt.title("Figuras de colores")

hls_juguetes = cv2.cvtColor(juguetesImg, cv2.COLOR_RGB2HLS)
h,l,s = cv2.split(hls_juguetes)
dark_purple = (140,0,0)
ligth_purple = (179,125,125)


#dark_purple = rgb_to_hsv(np.array(dark_purple)/255)
#ligth_purple = rgb_to_hsv(np.array(ligth_purple)/255)
print(ligth_purple, dark_purple)

mask = cv2.inRange(hls_juguetes, dark_purple, ligth_purple)
result = cv2.bitwise_and(juguetesImg, juguetesImg, mask=mask)

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray")
plt.title("Mascara")

plt.subplot(1, 3, 3)
plt.imshow(result)
plt.title("Segmentacion")
plt.savefig('SegmentadaMoradaOpenCV.png', dpi=600)


lo_square = np.full((10, 10, 3), ligth_purple, dtype=np.uint8) / 255.0
do_square = np.full((10, 10, 3), dark_purple, dtype=np.uint8) / 255.0

plt.figure(2)
plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.title("Morado claro")

plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.title("Morado oscuro")
plt.show()
plt.savefig('ColoresMorado.png', dpi=600)