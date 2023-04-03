import cv2
import numpy as np
import math

font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (255,0,255)
grosorLetra = 1

img = cv2.imread('monedas.jpg')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow('monedas', img)

src = cv2.medianBlur(img, 9)
src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('gris', src)

_, aux = cv2.threshold(src,50,255,cv2.THRESH_BINARY)
aux = 255 - aux
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
aux = cv2.morphologyEx(aux, cv2.MORPH_CLOSE, kernel)

cv2.imshow('umbral', aux)

epsilon = 800
areaspesos = [4500, 6500, 55, 61, 67]
numero = [0.5, 1, 2, 5, 10]
contador = np.zeros(5, np.uint8)

n_components, output, stats, centroids = cv2.connectedComponentsWithStats(aux, connectivity=8, ltype=cv2.CV_32S)

print(type(n_components),'> ', n_components)
print(type(output), output.shape, '> ',output)
print(type(stats), stats.shape,'> ',stats)
print(type(centroids), centroids.shape,'> ',centroids)


for i in range(n_components):
    x = stats[i, cv2.CC_STAT_LEFT]
    y = stats[i, cv2.CC_STAT_TOP]
    w = stats[i, cv2.CC_STAT_WIDTH]
    h = stats[i, cv2.CC_STAT_HEIGHT]
    area = stats[i, cv2.CC_STAT_AREA]
    centro = (int(centroids[i, cv2.CC_STAT_LEFT]),int(centroids[i, cv2.CC_STAT_TOP]))
    
    print('x:',x,y,w,h,area, centro)
    
    for peso in range(len(areaspesos)):
        if abs(area - areaspesos[peso]) <= epsilon:
            radio = int(math.sqrt(area / math.pi))
            cv2.circle(img, centro, radio, (0,255,0), 2)
            cv2.putText(img, str(numero[peso]),centro, font, tamañoLetra, colorLetra, grosorLetra)
            contador[peso] +=1
            print(numero[peso],": ", area)


total = np.array(numero) * contador
total = total.sum()
cv2.putText(img, 'TOTAL: $'+str(total),(10,30), font, tamañoLetra, colorLetra, grosorLetra)

for peso in range(len(areaspesos)):
    cadena = '$' + str(numero[peso]) + ': '+ str(contador[peso])
    cv2.putText(img, cadena , (10,60+peso*20), font, tamañoLetra, colorLetra, grosorLetra)

cv2.imshow('detected circles', img)
cv2.imwrite('detectedCirclesConexas.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()