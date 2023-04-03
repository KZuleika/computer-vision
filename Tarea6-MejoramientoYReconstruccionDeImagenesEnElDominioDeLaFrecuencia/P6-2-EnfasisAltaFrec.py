import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def addpadding(img):
    alto, ancho = img.shape
    pad = 2

    while pad < max(alto, ancho):
        pad *=2
    out = np.zeros((pad,pad), np.uint8)
    out[0:alto, 0:ancho] = img
    #cv2. imshow('con padding', out)
    return out


def enfasis_alta_frecuencia(val):
    k1 = cv2.getTrackbarPos('k1', imgName)
    k2 = cv2.getTrackbarPos('k2', imgName)
    fcorte = cv2.getTrackbarPos('fcorte', imgName)

    if fcorte == 0:
        fcorte = 0.1

    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    mask = np.zeros((alto, ancho, 2), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = math.sqrt( pow(c_fila-i, 2) + pow(c_col-j, 2) )
            if fcorte > 0:
                aux = d**2 / (2 * fcorte**2)
                mask[i,j,:] = math.exp(-aux)

    mask = 1 - mask

    fshift = dft_shift * (k1 + k2 * mask)
    f_ishift = np.fft.ifftshift(fshift)
    out = cv2.idft(f_ishift)
    out = cv2.magnitude(out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],0], 
                        out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],1])
    
    cv2.imshow(imgName,out)
    
    plt.subplot(121),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])


    plt.subplot(122),plt.imshow(out, cmap = 'gray')
    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()

    return 

imgName = 'Lena.tif'
imagenOriginal = cv2.imread(imgName, 0)
    
plt.subplot(121),plt.imshow(imagenOriginal, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

imagen = np.float32(addpadding(imagenOriginal))
dft = cv2.dft(imagen, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()         


cv2.imshow(imgName, imagenOriginal)
cv2.createTrackbar('fcorte', imgName, 1, 100, enfasis_alta_frecuencia)
cv2.createTrackbar('k1', imgName, 1, 100, enfasis_alta_frecuencia)
cv2.createTrackbar('k2', imgName, 1, 100, enfasis_alta_frecuencia)

cv2.waitKey(0)
cv2.destroyAllWindows(0)