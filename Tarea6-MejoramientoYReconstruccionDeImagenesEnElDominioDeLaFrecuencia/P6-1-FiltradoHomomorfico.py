import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def normalize(mask):
    mask = np.abs(mask)
    mask -= mask.min()
    out = mask / mask.max() * 255
    return out

def filtrado_homomofico(value):
    gammaH = cv2.getTrackbarPos('gammaH', windowName) / 100
    d0 = cv2.getTrackbarPos('D0', windowName) *10
    if d0 == 0:
        d0 = 100
    c = 1
    gammaL = 1 - gammaH

    #gammaL, gammaH, d0 = 0.8,0.2,1

    imagen = np.float32(imagenOriginal)
    dft = np.fft.fft2(imagen)
    dft_shift = np.fft.fftshift(dft)
    
    alto, ancho = dft_shift.shape
    c_fila, c_col = alto//2, ancho//2
    mask = np.ones((alto,ancho), np.float32)

    for i in range(alto):
        for j in range (ancho):
            d = pow(c_fila-i, 2) + pow(c_col-j, 2)
            aux = math.exp(-c * d / pow(d0,2))
            mask[i,j] = (gammaH - gammaL) * (1 - aux) + gammaL
    
    
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    out =  np.fft.ifft2(f_ishift)
    out = normalize(out)

    cv2.imshow(windowName, mask)

    plt.subplot(121),plt.imshow(imagenOriginal, cmap = 'gray')
    plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(122),plt.imshow(out, cmap = 'gray')
    plt.title('Imagen Filtrada'), plt.xticks([]), plt.yticks([])

    plt.show()
    return


imgName = ['Mars_moon_phobos.tif', 'Paisaje.jpg']


for i in range(0, len(imgName)):
    imagenOriginal = cv2.imread(imgName[i], 0)
    imagenOriginal = cv2.resize(imagenOriginal, (0,0), fx= 0.5, fy=0.5)
    windowName = imgName[i]

    cv2.imshow(imgName[i],imagenOriginal)
    cv2.createTrackbar('gammaH', imgName[i], 1, 100, filtrado_homomofico)
    cv2.createTrackbar('D0', imgName[i], 1, 50, filtrado_homomofico)

    cv2.waitKey(0)
    cv2.destroyWindow(imgName[i])

cv2.destroyAllWindows()
