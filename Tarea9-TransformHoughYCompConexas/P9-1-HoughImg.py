import cv2
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (255,255,196)
grosorLetra = 1

img = cv2.imread('monedas2.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('monedas', img)

src = cv2.medianBlur(img, 9)
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(src, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=50, param2=30, minRadius=0, maxRadius=0)

epsilon = 2
peso50 = 40
peso1 = 51
peso2 = 55
peso5 = 61
peso10 = 67


radiosPesos = [peso50, peso1, peso2, peso5, peso10]
numero = [0.5, 1, 2, 5, 10]
contador = np.zeros(5, np.uint8) 
print(contador)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # dibujar circulo 
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    # dibujar centro
    cv2.circle(img, (i[0], i[1]), 2, (0,0,255), 3)
    
    radio = i[2]
    for peso in range(len(radiosPesos)):
        if abs(radio - radiosPesos[peso]) < epsilon:
            cv2.putText(img, str(numero[peso]),(i[0], i[1]), font, tamañoLetra, colorLetra, grosorLetra)
            contador[peso] +=1
            print(numero[peso],": ", radio)


total = np.array(numero) * contador
total = total.sum()
cv2.putText(img, 'TOTAL: $'+str(total),(10,30), font, tamañoLetra, colorLetra, grosorLetra)

for peso in range(len(radiosPesos)):
    cadena = '$' + str(numero[peso]) + ': '+ str(contador[peso])
    cv2.putText(img, cadena , (10,60+peso*20), font, tamañoLetra, colorLetra, grosorLetra)

cv2.imshow('detected circles', img)
cv2.imwrite('detectedCirclesHough.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()