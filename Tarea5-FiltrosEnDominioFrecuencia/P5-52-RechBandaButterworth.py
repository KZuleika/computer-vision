import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def pbanda_butterworth_filter(val):
    n = cv2.getTrackbarPos('orden',winTitle)
    fc1 = cv2.getTrackbarPos('fc1',winname=winTitle)
    fc2 = cv2.getTrackbarPos('fc2',winname=winTitle)
    
    fcMin = min(fc1,fc2)
    fcMax = max(fc1,fc2)

    if n==0:
        n=1
    if fcMin == 0:
        fcMin = 0.1
    if fcMax == 0:
        fcMax = 0.1

    alto, ancho = imagen.shape
    c_fila, c_col = alto//2, ancho//2
    pbaja1 = np.zeros((alto, ancho, 2), np.float32)
    pbaja2 = np.zeros((alto, ancho, 2), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = math.sqrt( pow(c_fila-i, 2) + pow(c_col-j, 2) )
            pbaja1[i,j,:] = 1 / (1 + np.power(d/fcMax, 2*n))
            pbaja2[i,j,:] = 1 / (1 + np.power(d/fcMin, 2*n))

    palta = 1 - pbaja2
    mask = pbaja1 * palta
    mask = 1 - mask

    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    out = cv2.idft(f_ishift)
    out = cv2.magnitude(out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],0], 
                        out[0:imagenOriginal.shape[0],0:imagenOriginal.shape[1],1])
    
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
winTitle = 'Rechaza banda Butterworth'

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
    cv2.createTrackbar('fc1', winTitle,0,300, pbanda_butterworth_filter)
    cv2.createTrackbar('fc2', winTitle,0,300, pbanda_butterworth_filter)
    cv2.createTrackbar('orden', winTitle,0,20, pbanda_butterworth_filter)
    cv2.waitKey(0)


cv2.waitKey(0)
cv2.destroyAllWindows()
