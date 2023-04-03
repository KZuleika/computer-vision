import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


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

for i in range(0, len(imgNames)):
    imagenOriginal = cv2.imread(imgNames[i], 0)

    d_parche = 15
    
    plt.subplot(221),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])

    imagen = np.float32(addpadding(imagenOriginal))
    dft = cv2.dft(imagen, flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    #cv2.imwrite('espectro1.jpg', magnitude_spectrum)

    alto, ancho = imagen.shape
    mask = np.ones((alto,ancho, 2), np.uint8)
    
    parche = np.array([[80,45], 
                       [80,85], 
                       [85,170], 
                       [85,210], 
                       [170,40], 
                       [170,80], 
                       [170,170], 
                       [174,210]])

    #Recorre la matriz del parche
    for col in range(ancho):
        for fila in range(alto):
            mask[col, fila, :] = 1
            #recorre cada uno de los puntos
            for p in range(0, parche.shape[0]):
                if (math.sqrt(pow(fila-parche[p,0],2) + pow(col-parche[p,1],2))) < d_parche:
                    #print(parche[p,0], parche[p,1])
                    mask[col, fila,:] = 0

    cv2.imshow('mask', mask[:,:,0]*255)


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
    plt.title('Mask Ideal'), plt.xticks([]), plt.yticks([])

    plt.subplot(224),plt.imshow(out, cmap = 'gray')
    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()         

    cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()
