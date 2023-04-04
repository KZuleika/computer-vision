import cv2
import matplotlib.pyplot as plt
import numpy as np

#Crea una ventana/submatriz de k x k
def create_window(img, k, i_actual, j_actual):
    Cuadrado = (k // 2)
    MatrizVentana = img[(i_actual - Cuadrado):(i_actual + Cuadrado + 1), (j_actual - Cuadrado):(j_actual + Cuadrado + 1)]
    
    return MatrizVentana

#Filtro de mediana para imagenes en escala de grises
def median_filter_gray(img, k):
    out = img.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            VentanaProximidad = create_window(img, k, renglon, columna)
            out[renglon][columna] = np.median(VentanaProximidad)
    
    return out

# Igual que antes pero para imagenes a color.
def median_filter_rgb(img, k):
    out = img.copy()
    out[:, :, 0] = median_filter_gray(img[:, :, 0], k)
    out[:, :, 1] = median_filter_gray(img[:, :, 1], k)
    out[:, :, 2] = median_filter_gray(img[:, :, 2], k)
    return out


#IMAGEN EN RGB
img = cv2.imread('Lena RGB Sal.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
k = 3

img_filtered = median_filter_rgb(img, k)

plt.subplot(121),plt.imshow(img)
plt.title('Lena RGB Sal.tif'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Filtro de mediana'), plt.xticks([]), plt.yticks([])

plt.savefig("LenaSal.png", dpi = 600)
plt.show()

#IMAGEN EN HLS
img = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
k = 3

img_filtered = median_filter_rgb(img, k)

plt.subplot(121),plt.imshow(img)
plt.title('Lena RGB Sal.tif'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered)
plt.title('Filtro de mediana'), plt.xticks([]), plt.yticks([])

plt.savefig("LenaSalHLS.png", dpi = 600)
plt.show()

img_hls2rgb = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)
img_filtered_hls2rgb = cv2.cvtColor(img_filtered, cv2.COLOR_HLS2RGB)

plt.subplot(121),plt.imshow(img_hls2rgb)
plt.title('Lena RGB Sal.tif'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_filtered_hls2rgb)
plt.title('Filtro de mediana'), plt.xticks([]), plt.yticks([])

plt.savefig("LenaSalHLS2RGB.png", dpi = 600)
plt.show()