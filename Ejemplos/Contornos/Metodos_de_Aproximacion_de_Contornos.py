import cv2
import numpy as np

imagen = cv2.imread('Figuras.bmp')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,Binaria = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

# Comparacion entre los Metodos de aproximacion:

contornos1,hierarchy1 = cv2.findContours(Binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contornos2,hierarchy2 = cv2.findContours(Binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('Número de contornos encontrados: ', len(contornos1))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL  
tamañoLetra = 1
grosorLetra = 2
# Rojo, Azul, Verde, Amarillo, Magenta, Cian
colores = [(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,255,0)]
for n in range(len(contornos1)):
    print('Contorno1[', n, ']: ', len(contornos1[n]), ' puntos')
    print('Contorno2[', n, ']: ', len(contornos2[n]), ' puntos')                                
    cv2.drawContours(imagen, contornos1, n, colores[n], 5)
    cv2.putText(imagen, str(n), (20*n,20), font, tamañoLetra, colores[n], grosorLetra)

cv2.imshow('Contornos Encontrados', imagen)    
cv2.imshow('Binaria', Binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()
