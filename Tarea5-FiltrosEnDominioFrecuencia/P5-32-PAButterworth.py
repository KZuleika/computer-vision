import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
import math

def pa_butterworth_filter(val):
    n = cv2.getTrackbarPos('orden',winTitle)
    fcorte = cv2.getTrackbarPos('frec',winTitle)

    if n==0:
        n=1
    if fcorte == 0:
        fcorte = 0.1
    
    print(fcorte, n)

    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    mask = np.zeros((alto, ancho, 2), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = math.sqrt( pow(c_fila-i, 2) + pow(c_col-j, 2) )
            if fcorte > 0:
                mask[i,j,:] = 1 / (1 + np.power(d/fcorte, 2*n))
    mask = 1 - mask

    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    out = cv2.idft(f_ishift)
    out = cv2.magnitude(out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],0], 
                        out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],1])
    
    print(out.shape)
    cv2.imshow(winTitle,out)
    
    plt.subplot(131),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(132),plt.imshow(mask[:,:,0]*255, cmap = 'gray')
    plt.title('Mask Ideal'), plt.xticks([]), plt.yticks([])

    plt.subplot(133),plt.imshow(out, cmap = 'gray')
    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()
    return


def addpadding(img):
    alto, ancho = img.shape
    pad = 2

    while pad < max(alto, ancho):
        pad *=2
    out = np.zeros((pad,pad), np.uint8)
    out[0:alto, 0:ancho] = img
    #cv2. imshow('con padding', out)
    return out

imgNames = ['car_newsprint.tif', 'newspaper_shot_woman.tif', 'Ruido Periodico 1.jpg', 'Ruido Periodico 2.tif']
winTitle = 'Pasa Altas Butterworth'

for i in range(0, len(imgNames)):
    imagenOriginal = cv2.imread(imgNames[i], 0)
    
    plt.subplot(121),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    imagen = np.float32(addpadding(imagenOriginal))
    dft = cv2.dft(imagen, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()         

    cv2.imshow(winTitle, imagen)
    cv2.createTrackbar('frec', winTitle,0,300, pa_butterworth_filter)
    cv2.createTrackbar('orden', winTitle,0,20, pa_butterworth_filter)
    cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()
