import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


def addpadding(img):
    alto, ancho = img.shape
    pad = 2

    while pad < max(alto, ancho):
        pad *=2
    out = np.ones((pad,pad), np.uint8)
    out[0:alto, 0:ancho] = img
    #cv2. imshow('con padding', out)
    return out

imgNames = ['Ruido Periodico 1.jpg', 'newspaper_shot_woman.tif',  'car_newsprint.tif', 'Ruido Periodico 2.tif']

for i in range(0, len(imgNames)):
    imagenOriginal = cv2.imread(imgNames[i], 0)
    
    plt.subplot(221),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    imagen = np.float32(addpadding(imagenOriginal))
    dft = cv2.dft(imagen, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    cv2.imwrite('espectro'+str(i+1)+'.jpg', magnitude_spectrum)

    alto, ancho = magnitude_spectrum.shape
    mask = np.zeros((alto,ancho, 2), np.uint8)
    
    imgMask = cv2.imread('mask'+str(i+1)+'.jpg',0)
    mask[:,:,0] = imgMask
    mask[:,:,1] = imgMask

    #cv2.imshow('mask', mask[:,:,0]*255)

    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    out = cv2.idft(f_ishift)
    out = cv2.magnitude(out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],0], 
                        out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],1])
    
    #Para la imagen original
    dft_filtered = cv2.dft(out, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift_filtered = np.fft.fftshift(dft_filtered)
    magnitud_spectrum_filtered = np.log(cv2.magnitude(dft_shift_filtered[:,:,0],dft_shift_filtered[:,:,1]))


    plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

    plt.subplot(223),plt.imshow(magnitud_spectrum_filtered, cmap = 'gray')
    plt.title('Espectro (filtrado)'), plt.xticks([]), plt.yticks([])

    plt.subplot(224),plt.imshow(out, cmap = 'gray')
    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()         
    cv2.waitKey(0)
    
