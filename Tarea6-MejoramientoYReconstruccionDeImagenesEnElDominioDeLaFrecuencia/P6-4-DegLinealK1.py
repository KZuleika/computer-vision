import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def gaussian_noise(img, mean, std):
    out = np.copy(img)
    noise = np.random.normal(loc= mean, scale=std, size=out.shape)
    return noise

def getDFT(img):
    imagen = np.float32(img)
    dft = cv2.dft(imagen, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    return dft_shift

def getInversDFT(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    out = cv2.idft(f_ishift)
    out = cv2.magnitude(out[:,:,0],out[:,:,1])
    return out

def getLinealH_dft(imgFrec, a, b):
    alto, ancho, prof = imgFrec.shape
    c_alto , c_ancho = alto//2, ancho//2
    
    Hmask = np.ones((alto, ancho, prof), np.complex64)

    for u in range(0, Hmask.shape[0]):
        for v in range(0, Hmask.shape[1]):
            den = math.pi * ((u-c_alto)*a +b*(v-c_ancho))
            if den == 0:
                Hmask[u,v,:] = 1
            else:
                Hmask[u,v,:] = math.sin(den)*math.e**(-1j*den)/den
    #print(Hmask)
    return Hmask

def normalize(mask):
    mask = np.abs(mask)
    mask -= mask.min()
    out = mask / mask.max() * 255
    return out

def correct_zeros(mask):
    out = np.copy(mask)
    for u in range(0, out.shape[0]):
        for v in range(0, out.shape[1]):
            if out[u,v,0] < 0.000001:
                out[u,v,0] = 0.000001
            if out[u,v,1] < 0.000001:
                out[u,v,1] = 0.000001
    return out

def pb_buterrworth_filter(fcorte, n, imagen):
    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    mask = np.zeros((alto, ancho, 2), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = math.sqrt( pow(c_fila-i, 2) + pow(c_col-j, 2) )
            if fcorte > 0:
                mask[i,j,:] = 1 / (1 + np.power(d/fcorte, 2*n))

    return mask

a, b = 0.15, 0.2
mean , var = 0, 20
imgName = 'PortadaLibro.tif'
imagenOriginal = cv2.imread(imgName, 0)
imagenOriginal = cv2.resize(imagenOriginal, (0,0), fx=0.5, fy=0.5)

F_dft = getDFT(imagenOriginal)

#Obtenemos la deformacion
H_dft = getLinealH_dft(F_dft, a, b)
print(type(H_dft), H_dft.shape)
#H_dft = normalize(H_dft)
deformedimg_dft = F_dft * H_dft
print(type(deformedimg_dft), deformedimg_dft.shape)

#La imagen con deformacion lineal SIN ruido
deformedImg = getInversDFT(deformedimg_dft)
deformedImg = normalize(deformedImg)

#Obtener el ruido gaussiano
noise = gaussian_noise(imagenOriginal, mean, var)
N_dft = getDFT(noise)

#Imagen degradada CON ruido
G_img =  deformedImg + noise
G_dft = getDFT(G_img)

#Filtrado Inverso
H_dft = correct_zeros(H_dft)
Finversa_dft = F_dft / H_dft
Finversa_img = getInversDFT(Finversa_dft)
Finversa_img = np.array(normalize(Finversa_img), np.uint8)

#Filtro Limitacion radial
maskpb = pb_buterrworth_filter(100, 5, Finversa_dft[:,:,0])
Frad_dft = Finversa_dft * maskpb
Frad_img = getInversDFT(Frad_dft)
Frad_img = normalize(Frad_img)

#Filtro Wiener


plt.subplot(231),plt.imshow(imagenOriginal, cmap = 'gray')
plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

plt.subplot(232),plt.imshow(deformedImg, cmap = 'gray')
plt.title('Deformacion lineal'), plt.xticks([]), plt.yticks([])

plt.subplot(233),plt.imshow(G_img, cmap = 'gray')
plt.title('Deformacion+ruido'), plt.xticks([]), plt.yticks([])

plt.subplot(234),plt.imshow(Finversa_img, cmap = 'gray')
plt.title('Filtrado inverso'), plt.xticks([]), plt.yticks([])

plt.subplot(235),plt.imshow(Frad_img, cmap = 'gray')
plt.title('Filtrado de limitacion radial'), plt.xticks([]), plt.yticks([])

plt.subplot(236),plt.imshow(Finversa_img, cmap = 'gray')
plt.title('Filtrado Wiener'), plt.xticks([]), plt.yticks([])

plt.show()