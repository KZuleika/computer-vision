import cv2
import numpy as np

def calculate_window(ventana):
    v_param = np.zeros(2)
    v_param[0] = ventana.mean()
    v_param[1] = ventana.std()
    return v_param
    
def create_window(img, ventana, i_actual, j_actual):
    Cuadrado = (ventana // 2)
    MatrizVentana = img[(i_actual - Cuadrado):(i_actual + Cuadrado + 1), (j_actual - Cuadrado):(j_actual + Cuadrado + 1)] 
    return MatrizVentana

def mejoraImgLuminosas(img, ventana, k0, k1, k2, E):
    out = img.copy()
    alto, ancho = out.shape
    media_global = out.mean()
    std_global = out.std()
    print(media_global,std_global)   

    for renglon in range(ventana//2 , alto - ventana//2 -1):
        for columna in range(ventana//2, ancho - ventana//2 - 1):
            proximidad = create_window(out, ventana, renglon, columna)
            med_local, std_local = calculate_window(proximidad)
            if med_local <= k0*media_global and k1*std_global <= std_local <= k2*std_global:  
                if E*out[renglon][columna] > 255:
                    out[renglon][columna] = 255
                else:
                    out[renglon][columna] = round(E * out[renglon][columna])
                
    return out

def mejoraImgOscuras(img, ventana, k0, k1, k2, E):
    out = img.copy()
    alto, ancho = out.shape
    media_global = out.mean()
    std_global = out.std()
    print(media_global,std_global)   

    for renglon in range(ventana//2 , alto - ventana//2 -1):
        for columna in range(ventana//2, ancho - ventana//2 - 1):
            proximidad = create_window(out, ventana, renglon, columna)
            med_local, std_local = calculate_window(proximidad)
            if med_local >= k0*media_global and k1*std_global <= std_local <= k2*std_global:
                #print("1")    
                if E*out[renglon][columna] > 255:
                    out[renglon][columna] = 255
                else:
                    out[renglon][columna] = round(E * out[renglon][columna])
                
    return out

nameImg = ["Fig0309(a)(washed_out_aerial_image).tif",   #Ciudad
            "Fig0327(a)(tungsten_original).tif",        #Tungsteno
            "Fig0323(a)(mars_moon_phobos) - copia.tif", #Luna/calamar
            "Fig0316(1)(top_left).tif",                 #Granos iluminada contraste bajo
            "Fig0316(3)(third_from_top).tif",           #Granos bien
            "Fig0316(4)(bottom_left).tif",              #Granos oscura 
            "Fig0320(1)(top_left).tif"                 #Granos ilumninada
            ]
            
newImage = []
imgGray = []

for i in range(len(nameImg)):
    imgGray.append(cv2.imread(nameImg[i], 0))


#imgGray = cv2.resize(imgGray,(0,0), fx=0.5, fy=0.5)
newImage.append(mejoraImgLuminosas(imgGray[0], 3, 1, 0.02, 0.8, 0.75)) #imagen blanca 
newImage.append(mejoraImgLuminosas(imgGray[1], 3, 0.4, 0.05, 0.4, 5))  #oscuro
newImage.append(mejoraImgLuminosas(imgGray[2], 3, 0.4, 0.02, 0.4, 4)) #oscura
newImage.append(mejoraImgLuminosas(imgGray[3], 3, 1, 0.01, 0.8, 0.25)) #blanca
newImage.append(mejoraImgOscuras(imgGray[4], 3, 1, 0.01, 0.8, 1.5))    #oscura
newImage.append(mejoraImgOscuras(imgGray[5], 3, 0.5, 0.1, 0.8, 4))   #oscura
newImage.append(mejoraImgLuminosas(imgGray[6], 3, 1, 0.02, 0.8, 0.7)) #blanca



for i in range(len(nameImg)):
    cv2.imshow('Imagen original'+nameImg[i],imgGray[i])
    cv2.imshow('Corregida'+nameImg[i],newImage[i])

    cv2.waitKey(0)
    cv2.destroyWindow('Corregida'+nameImg[i])
    cv2.destroyWindow('Imagen original'+nameImg[i])

cv2.destroyAllWindows()