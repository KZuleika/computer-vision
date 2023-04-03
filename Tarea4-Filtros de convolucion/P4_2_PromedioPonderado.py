import cv2
import numpy as np

def promedio_ponderado(k):
    out = np.zeros(imagen.shape)
    out = cv2.copyMakeBorder(imagen, k//2, k//2, k//2, k//2, cv2.BORDER_CONSTANT)
    kernel = np.ones((k,k), np.float32)

    posCentral = kernel.shape[0]//2
    for i in range(0, posCentral):
        print(i)
        kernel[posCentral-i:posCentral+i+1, posCentral-i:posCentral+1+i] *= 2
        print(kernel[posCentral-i:posCentral+i+1, posCentral-i:posCentral+1+i],posCentral-i, posCentral+i )
    print(posCentral, kernel)
    kernel /= kernel.sum()

    out = cv2.filter2D(imagen, -1, kernel)
    print(out.shape, imagen.shape)
    cv2.imshow(winTitle,out)
    return out


winTitle = 'Promedio ponderado'

imgNames = ['lena_gray_512.tif', 'livingroom.tif','mandril_gray.tif', 'walkbridge.tif']

for i in range(0, len(imgNames)):
    imagen= cv2.imread(imgNames[i], 0)
    #imagen = cv2.resize(imagen, (0,0), fx= 0.4, fy=0.4)
    cv2.imshow('Imagen original',imagen)
    cv2.imshow(winTitle,imagen)
    if i == 0:
        cv2.createTrackbar('ventana', winTitle, 5, 50, promedio_ponderado)
    cv2.waitKey(0)

cv2.waitKey(0)
cv2.destroyAllWindows()
