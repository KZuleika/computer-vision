import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

def compare_moments(fig, reference, epsilon):
    print(fig)
    for f in range(0,8):
        fila = reference.iloc[[f]]
        print(fila)
        print(fila.h0)
        print(type(fila.h0))
        h = fila.get('h0').values
        h = str(h).replace('[','').replace(']','').replace("'",'')
        h = int(h)
        print('\n\n',h)

        print(fig[0] - int(h))
        
    return f

filenames =['Avion', 'Bailarina', 'Ballet', 'Mariposa', 'Mujer', 'Paloma', 'Patada', 'Pez']
contfig = np.zeros(8)
df_humoments = pd.read_csv('huMoments.csv', delimiter=',', header=0, index_col=0)
print(df_humoments)


captura = cv2.VideoCapture(1)

while (captura.isOpened()):
    ret, imagen = captura.read()

    if ret == True:
        src = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        src = cv2.blur(src, (3,3))
        _, src = cv2.threshold(src,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
        
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        src = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)

        #Hallar las figuras con Componentes Conexas
        n_components, output, stats, centroids = cv2.connectedComponentsWithStats(src, connectivity=8, ltype=cv2.CV_32S)
        for i in range(n_components):
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            area = stats[i, cv2.CC_STAT_AREA]
            centro = (int(centroids[i, cv2.CC_STAT_LEFT]),int(centroids[i, cv2.CC_STAT_TOP]))
            figure = src[x:x+w, y:y+h]
        
            #Calcular los momentos de Hu
            moments = cv2.moments(figure)
            huMoments = cv2.HuMoments(moments)
            huMoments_norm = -1 * np.copysign(1.0, huMoments) * np.log10(abs(huMoments))
            indexfig = compare_moments(huMoments_norm, df_humoments, 0.5)
            contfig[indexfig] = contfig[indexfig] + 1


            imagen = cv2.rectangle(imagen, (x,y), (x+w,y+h), (180,0,180),2)

        cv2.imshow('bnw', src)
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break
    time.sleep(2)
captura.release()
cv2.destroyAllWindows()
