import cv2
import numpy as np
import math
import matplotlib.pyplot as plt


def getDFT(img):
    imagen = np.float32(img)
    dft = np.fft.fft2(imagen)
    dft_shift = np.fft.fftshift(dft)
    return dft_shift

def getInversDFT(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    out = np.fft.ifft2(f_ishift)
    return out

def getLinealH_dft(imgFrec, a, b, T):
    alto, ancho = imgFrec.shape
    c_alto , c_ancho = alto//2, ancho//2

    u = np.linspace(0, alto, alto)
    v = np.linspace(0, ancho, ancho)
    U,V = np.meshgrid(u,v)
    den = a * (U-c_ancho)+ b * (V - c_alto)
    Hmask = np.sin(np.pi * den) * np.exp(-np.pi*1j*den) * T / den

    return Hmask

def normalize(mask):
    mask = np.abs(mask)
    mask -= mask.min()
    out = mask / mask.max() * 255
    print(out.shape)
    return out

def getpolarimg(img):
    alto, ancho = img.shape
    c_filas, c_columnas = alto/2.0 , ancho/2.0
    central = math.sqrt(c_filas**2 + c_columnas**2)
    polar = cv2.linearPolar(img,(c_filas, c_columnas), central, cv2.WARP_FILL_OUTLIERS)
    polar = polar.astype(np.uint8)
    return polar

def polar_a_cuadradas(polar):
    alto, ancho = polar.shape
    c_filas, c_columnas = alto/2.0 , ancho/2.0
    central = math.sqrt(c_filas**2 + c_columnas**2)
    img = cv2.linearPolar(polar,(c_filas, c_columnas), central, cv2.WARP_INVERSE_MAP)
    img = img.astype(np.uint8)
    return img


a, b, t = 0.15, 0.2, 1
mean , var = 0, 10
imgName = 'PortadaLibro.tif'
imagenOriginal = cv2.imread(imgName, 0)
imagenOriginal = cv2.resize(imagenOriginal, (0,0), fx=0.5, fy=0.5)

#Obtener la imagen en coordenadas polares
polar_img = getpolarimg(imagenOriginal)
polar_dft = getDFT(polar_img)

#Obtenemos la deformacion rotacional en frecuencia
H_dft = getLinealH_dft(polar_dft, a, b, t)
G_dft = H_dft * polar_dft

#La imagen con deformacion rotacional
G_img = getInversDFT(G_dft)
G_img = normalize(G_img)

#Convertir de polar a cuadradas
G_img = polar_a_cuadradas(G_img)

plt.subplot(131),plt.imshow(imagenOriginal, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(132),plt.imshow(polar_img, cmap = 'gray')
plt.title('Imagen Polar'), plt.xticks([]), plt.yticks([])

plt.subplot(133),plt.imshow(G_img, cmap = 'gray')
plt.title('Degradación rotacional'), plt.xticks([]), plt.yticks([])

plt.savefig("DegradacionRotacional.png", dpi = 400)
plt.show()