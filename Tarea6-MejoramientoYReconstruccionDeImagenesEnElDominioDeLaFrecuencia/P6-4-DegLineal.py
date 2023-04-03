import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def gaussian_noise(img, mean, var):
    std = math.sqrt(var)
    noise = np.random.normal(loc= mean, scale=std, size=img.shape)
    return noise

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


def pb_buterrworth_filter(fcorte, n, imagen):
    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    mask = np.zeros((alto, ancho), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = math.sqrt( pow(c_fila-i, 2) + pow(c_col-j, 2) )
            if fcorte > 0:
                mask[i,j] = 1 / (1 + np.power(d/fcorte, 2*n))

    return mask

def buterrworth_filter(fcorte, n, imagen):
    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    u = np.linspace(0, alto, alto)
    v = np.linspace(0, ancho, ancho)
    U,V = np.meshgrid(u,v)
    d = np.sqrt( (c_fila - U)**2 + (c_col - V)**2) 
    mask = 1 / (1 + np.power(d/fcorte, 2*n))            
    return mask


a, b, t = 0.15, 0.2, 1
mean , var = 0, 20
imgName = 'PortadaLibro.tif'
imagenOriginal = cv2.imread(imgName, 0)
imagenOriginal = cv2.resize(imagenOriginal, (0,0), fx=0.5, fy=0.5)

F_dft = getDFT(imagenOriginal)

#Obtener el ruido gaussiano
noise = gaussian_noise(imagenOriginal, mean, var)
N_dft = getDFT(noise)

#Obtenemos la deformacion
H_dft = getLinealH_dft(F_dft, a, b, t)
G_dft = H_dft * F_dft

#La imagen con deformacion lineal SIN ruido
G_img = getInversDFT(G_dft)
G_img = normalize(G_img)

#Imagen deformada CON ruido
GN_img = G_img + noise
GN_dft = getDFT(GN_img)

#Filtrado Inverso
Finversa_dft = F_dft + N_dft / H_dft
Finversa_img = getInversDFT(Finversa_dft)
Finversa_img = np.array(normalize(Finversa_img), np.uint8)

#Filtro Limitacion radial
maskpb = buterrworth_filter(25, 20, GN_dft)
Frad_dft = F_dft + N_dft / H_dft 
Frad_dft *= maskpb

Frad_img = getInversDFT(Frad_dft)
Frad_img = normalize(Frad_img)

#Filtro Wiener
numWiener = np.abs(H_dft)**2
Sn = np.abs(N_dft)**2
Sf = np.abs(F_dft)**2
coefWiener = numWiener / (numWiener + Sn /Sf)
Fwiener_dtf = (1/H_dft) * coefWiener * G_dft
Fwiener_img = getInversDFT(Fwiener_dtf)
Fwiener_img = normalize(Fwiener_img)



plt.subplot(231),plt.imshow(imagenOriginal, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(232),plt.imshow(G_img, cmap = 'gray')
plt.title('Deformacion lineal'), plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(GN_img, cmap = 'gray')
plt.title('Deformacion+ruido'), plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(Finversa_img, cmap = 'gray')
plt.title('Filtrado inverso'), plt.xticks([]), plt.yticks([])

plt.subplot(235),plt.imshow(Frad_img, cmap = 'gray')
plt.title('Filtrado de limitacion radial'), plt.xticks([]), plt.yticks([])

plt.subplot(236),plt.imshow(Fwiener_img, cmap = 'gray')
plt.title('Filtrado Wiener'), plt.xticks([]), plt.yticks([])

plt.savefig("Degradaciones.png", dpi = 400)

plt.show()