import cv2
import numpy as np

imagen = cv2.imread('Figuras3.bmp')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,Binaria = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

contornos,hierarchy = cv2.findContours(Binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print('Número de contornos encontrados: ', len(contornos))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL  
tamañoLetra = 1
grosorLetra = 2
colores = [(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,255,0),(200,55,127), (127,55,200)]

for n in range(len(contornos)):                         
    Epsilon = 0.005*cv2.arcLength(contornos[n],True)
    Aproximacion = cv2.approxPolyDP(contornos[n], Epsilon, True)
    X, Y, W, H = cv2.boundingRect(Aproximacion)
    if len(Aproximacion)==3:
        cv2.putText(imagen,'Triangulo', (X, Y-5),1,1.5,colores[n],2)
    if len(Aproximacion)==4 and W == H:
        cv2.putText(imagen,'Cuadrado', (X, Y-5),1,1.5,colores[n],2)
    if len(Aproximacion)==4 and W != H:
        cv2.putText(imagen,'Rectangulo', (X, Y-5),1,1.5,colores[n],2)
    if len(Aproximacion)==5:
        cv2.putText(imagen,'Pentagono', (X, Y-5),1,1.5,colores[n],2)
    if len(Aproximacion)==6:
        cv2.putText(imagen,'Hexagono', (X, Y-5),1,1.5,colores[n],2)
    if len(Aproximacion)>10:
        cv2.putText(imagen,'Circulo', (X, Y-5),1,1.5,colores[n],2)
    cv2.putText(imagen, str(len(Aproximacion)), (40*n,20), font, tamañoLetra, colores[n], grosorLetra)    
    cv2.drawContours(imagen, [Aproximacion], 0, colores[n], 2)

cv2.imshow('Contornos Encontrados', imagen)    
#cv2.imshow('Binaria', Binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()
