import cv2
import numpy as np

imagen = cv2.imread('Figuras2.bmp')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,Binaria = cv2.threshold(grises,100,255,cv2.THRESH_BINARY)

#Next, hace referencia al siguiente contorno en el mismo nivel de jerarquía.
#Previous, hace referencia al contorno anterior en el mismo nivel de jerarquía.
#First_Child, hace referencia al primer hijo del contorno.
#Parent, por último indica el padre contorno.

# Comparacion entre los Metodos de Recuperacion:

contornos,hierarchy = cv2.findContours(Binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#contornos,hierarchy = cv2.findContours(Binaria, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#contornos,hierarchy = cv2.findContours(Binaria, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#contornos,hierarchy = cv2.findContours(Binaria, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('Número de contornos encontrados: ', len(contornos))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL  
tamañoLetra = 1
grosorLetra = 2
print(hierarchy)
print ('hierarchy: [NEXT, PREVIOUS, FIST CHILD, PARENT]')
# Rojo, Azul, Verde, Amarillo, Magenta, Cian
colores = [(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,0,255),(255,255,0),(200,55,127)]
for n in range(len(hierarchy[0])):
    if hierarchy[0][n][3]==-1:
        Mensaje = ' Es un Padre porque PARENT = -1'
    else:
        if hierarchy[0][n][2]==-1:
            Mensaje = ' Es hijo de '+ str(hierarchy[0][n][3])
        else:
            Mensaje = ' Es hijo de '+ str(hierarchy[0][n][3])+' y padre de '+ str(hierarchy[0][n][2])
    print('hierarchy[', n, ']: ', hierarchy[0][n], Mensaje)                             
    cv2.drawContours(imagen, contornos, n, colores[n], 5)
    cv2.putText(imagen, str(n), (20*n,20), font, tamañoLetra, colores[n], grosorLetra)

cv2.imshow('Contornos Encontrados', imagen)    
cv2.imshow('Binaria', Binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()
