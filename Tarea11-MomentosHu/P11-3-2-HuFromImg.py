import cv2
import numpy as np

def calculate_and_show_total(img, objetnames, contador):
    cv2.putText(img, 'TOTAL FIGURAS: '+str(contador.sum()),(10,30), font, tamañoLetra, colorLetra, grosorLetra)
    desplazo = 0
    for obj in range(len(objetnames)):
        if contador[obj] != 0:
            cv2.putText(img, objetnames[obj]+': '+str(contador[obj]),(10,50+desplazo*20), font, tamañoLetra, colorLetra, grosorLetra)
            desplazo += 1

def compare_moments(actual_fig_humom, reference_humoments, epsilon):
    #print('\n ACTUAL:', actual_fig_humom, '\n REFERENCIA:', reference_humoments[1],'\n', actual_fig_humom - reference_humoments[1],'\n\n')
    #print(actual_fig_humom.shape, reference_humoments[2].shape )
    diferencias = []
    #print(humoment_obj.shape, humoment_ref.shape)
    for obj in range(0,len(reference_humoments)):
        aux = reference_humoments[obj] - actual_fig_humom
        aux = np.power(aux,2)
        diferencia_total = aux.sum()
        diferencias.append(np.sqrt(diferencia_total))
    dif_array = np.array(diferencias)
    minimoDist = dif_array.min()
    indice = diferencias.index(minimoDist)
    #print('obj: ', actual_fig_humom, 'min,indx: ', minimoDist, indice)
    return indice

def load_humoments_object(filenames):
    h = []
    for f in range(len(filenames)):
        src = cv2.imread('Capturas/'+filenames[f]+'.jpg', 0)
        _, aux = cv2.threshold(src,120,1,cv2.THRESH_BINARY_INV)

        cv2.imwrite('Referencias/'+filenames[f]+'.jpg',aux*255)
        #cv2.imshow('load', aux*255)
        #cv2.waitKey(0)
        moments = cv2.moments(aux)
        huMoments = cv2.HuMoments(moments)
        print(filenames[f],"\n",huMoments, "\n\n")
        #huMoments_norm = -1 * np.copysign(1.0, huMoments) * np.log10(abs(huMoments))
        
        #h.append(huMoments_norm.flatten())
        h.append(huMoments)
    return h


font = cv2.FONT_HERSHEY_COMPLEX
tamañoLetra = 0.5
colorLetra = (180,0,255)
grosorLetra = 1

tolerancia = 0.44
filenames =['Avion', 'Bailarina', 'Ballet', 'Mariposa', 'Mujer', 'Paloma', 'Patada', 'Pez']
obj_hu_mom = load_humoments_object(filenames)   

#############LEER IMAGENES
for imgTest in range(len(filenames)):
    for imgVersion in range(3):
        archivoNombre = 'Prueba/'+str(filenames[imgTest])+str(imgVersion+1) + '.jpg'
        imagen = cv2.imread(archivoNombre)
        src = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        src = cv2.blur(src, (3,3))
        _, src = cv2.threshold(src,120,1,cv2.THRESH_BINARY_INV)

        cv2.imshow('src', src*255)

        #Hallar las figuras con Componentes Conexas
        n_components, label, stats, centroids = cv2.connectedComponentsWithStats(src, connectivity=8, ltype=cv2.CV_32S)
        contfig = np.zeros(8)
        for i in range(1, n_components):
            x = int(stats[i, cv2.CC_STAT_LEFT])
            y = int(stats[i, cv2.CC_STAT_TOP])
            w = int(stats[i, cv2.CC_STAT_WIDTH])
            h = int(stats[i, cv2.CC_STAT_HEIGHT])
            area = int(stats[i, cv2.CC_STAT_AREA])
            centro = (int(centroids[i, cv2.CC_STAT_LEFT]),int(centroids[i, cv2.CC_STAT_TOP]))
            
            (cX, cY) = centroids[i]
            cX = int(cX)
            cY = int (cY)
            width = stats[label[cY,cX], cv2.CC_STAT_WIDTH]
            height = stats[label[cY,cX], cv2.CC_STAT_HEIGHT]
            x_ = stats[label[cY,cX], cv2.CC_STAT_LEFT]
            y_ = stats[label[cY,cX], cv2.CC_STAT_TOP]
            
            figure = src[y:y+height, x:x+width]

            #cv2.putText(figure, str(x)+'+'+str(w)+' '+str(y)+'+'+str(h)+' '+str(area), (x+20,y+20), font, tamañoLetra, (180,0,180), grosorLetra)
            cv2.imshow('figure', figure*255)
            print(figure.shape)
            if area > 1000:
                #Calcular los momentos de Hu
                moments = cv2.moments(figure)
                huMoments = cv2.HuMoments(moments)
                #huMoments_flatten = huMoments.flatten()
                #huMoments_norm = -1 * np.copysign(1.0, huMoments) * np.log10(abs(huMoments))
                #huMoments_norm_flatten = huMoments_norm.flatten()
                print(huMoments)
                indexfig = compare_moments(huMoments, obj_hu_mom, tolerancia)
                if indexfig != None:
                    contfig[indexfig] += 1
                    cv2.putText(imagen, filenames[indexfig], centro, font, tamañoLetra, (180,0,180), grosorLetra)
                    #print('fig #',contfig.sum())
                else:
                    cv2.putText(imagen, 'S/C', centro, font, tamañoLetra, (180,0,180), grosorLetra)
                imagen = cv2.rectangle(imagen, (x,y), (x+w,y+h), (180,0,180),2)
                cv2.putText(imagen, '#'+str(contfig.sum()), (x,y-10), font, tamañoLetra, (180,0,180), grosorLetra)
        calculate_and_show_total(imagen, filenames, contfig)
        #cv2.imshow('bnw', src)
        cv2.imshow('video', imagen)
        cv2.waitKey(0)
        cv2.destroyWindow('figure')
        
cv2.destroyAllWindows()