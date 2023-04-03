import cv2
import numpy as np
import time

def calculate_and_show_total(img, objetnames, contador):
    cv2.putText(img, 'TOTAL FIGURAS: '+str(contador.sum()),(10,30), font, tamañoLetra, colorLetra, grosorLetra)
    for obj in range(len(objetnames)):
        if contador[obj] != 0:
            cv2.putText(img, objetnames[obj]+': '+str(contador[obj]),(10,50+obj*20), font, tamañoLetra, colorLetra, grosorLetra)

def compare_moments(actual_fig, reference_fig):
    dmin = 9876543210.6
    numRef = None
    for f in range(len(reference_fig)):
        aux = cv2.matchShapes(reference_fig[f], actual_fig,cv2.CONTOURS_MATCH_I3,0)
        print(filenames[f],': ', aux)
        if aux < dmin: 
            dmin = aux
            numRef = f
    #print(filenames[numRef])
    return numRef

def load_humoments_object(filenames):
    h = []
    for f in range(len(filenames)):
        src = cv2.imread('Capturas/'+filenames[f]+'.jpg', 0)
        _, aux = cv2.threshold(src,120,1,cv2.THRESH_BINARY_INV)
        cv2.imwrite('Referencias/'+filenames[f]+'.jpg',aux*255)
        #cv2.imshow('load', aux)
        #cv2.waitKey(0)

        h.append(aux)
    return h


font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (180,0,255)
grosorLetra = 1

tolerancia = 0.44
filenames =['Avion', 'Bailarina', 'Ballet', 'Mariposa', 'Mujer', 'Paloma', 'Patada', 'Pez']
#filenames =['Avion', 'Mujer', 'Paloma', 'Patada']
obj_ref = load_humoments_object(filenames)
#print(obj_ref)
   

captura = cv2.VideoCapture(1)

while (captura.isOpened()):
    ret, imagen = captura.read()

    if ret == True:
        src = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, src = cv2.threshold(src,120,255,cv2.THRESH_BINARY_INV)
        cv2.imshow('src', src)
        #cv2.waitKey(0)

        #Hallar las figuras con Componentes Conexas
        n_components, output, stats, centroids = cv2.connectedComponentsWithStats(src, connectivity=8, ltype=cv2.CV_32S)
        contfig = np.zeros(8)
        for i in range(1, n_components):
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            area = stats[i, cv2.CC_STAT_AREA]
            centro = (int(centroids[i, cv2.CC_STAT_LEFT]),int(centroids[i, cv2.CC_STAT_TOP]))
            figure = src[x:x+w, y:y+h]

            if w > 100 and h > 100:
                #Calcular los momentos de Hu
                indexfig = compare_moments(figure, obj_ref)
                if indexfig != None:
                    contfig[indexfig] += 1
                    cv2.putText(imagen, filenames[indexfig], centro, font, tamañoLetra, (180,0,180), grosorLetra)
                else:
                    cv2.putText(imagen, 'S/C', centro, font, tamañoLetra, (180,0,180), grosorLetra)
                imagen = cv2.rectangle(imagen, (x,y), (x+w,y+h), (180,0,180),2)
        calculate_and_show_total(imagen, filenames, contfig)
        #cv2.imshow('bnw', src)
        cv2.imshow('video', imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break
    time.sleep(1)
captura.release()
cv2.destroyAllWindows()

