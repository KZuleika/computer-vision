import cv2
import numpy as np
import statistics as st


def create_window(img, k, i_actual, j_actual):
    Cuadrado = (k // 2)
    MatrizVentana = img[(i_actual - Cuadrado):(i_actual + Cuadrado + 1), (j_actual - Cuadrado):(j_actual + Cuadrado + 1)]
    return MatrizVentana

def window_to_list(window):
    v_aux = []
    for i in range(0, window.shape[0]):
        for j in range(0, window.shape[1]):
            v_aux.append(window[i,j])
    return v_aux

#Filtro promedio
def mean_filter(k):
    out = imagen.copy()
    border = k // 2
    out = cv2.copyMakeBorder(imagen,border, border, border, border, cv2.BORDER_CONSTANT)
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            out[renglon][columna] = ventana.mean()
    cv2.imshow(titles[0], out)

#Filtro Media geometrica
def geometric_mean_filter(k):
    out = imagen.copy()
    out = out.astype(float)
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            exp = 1 / (k**2)
            val  = ventana.prod() ** exp
            out[renglon][columna] = int(val)

    out =  out / out.max()
    cv2.imshow(titles[1], out)

def armonic_median_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            v_plano = ventana.flatten()
            val = 0
            for px in range(0, v_plano.size):
                 if 0!= v_plano[px]:
                    val += 1/ v_plano[px]
            
            if val != 0:
                out[renglon][columna] = k**2 / val

    cv2.imshow(titles[2], out)

def contra_armonic_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape
    r = 2
    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            v_plano = ventana.flatten()
            num = np.float_power(v_plano, r+1)
            den = np.float_power(v_plano, r)
            if den.sum() != 0:
                out[renglon][columna] = num.sum()/den.sum()
            else:
                out[renglon][columna] = 0
    cv2.imshow(titles[3], out)

def median_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            Pos_Med = (k * k)// 2
            v_plano = ventana.flatten() 
            v_plano.sort() 
            out[renglon][columna] = v_plano[Pos_Med]
    cv2.imshow(titles[4], out)

def mode_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(imagen, k, renglon, columna)
            v_plano = ventana.flatten()
            out[renglon][columna] = st.mode(v_plano)
    cv2.imshow(titles[5], out)    

def max_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(imagen, k, renglon, columna)
            out[renglon][columna] = ventana.max()

    out = out / out.max()
    cv2.imshow(titles[6], out)    


def min_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(imagen, k, renglon, columna)
            out[renglon][columna] = ventana.min()
    cv2.imshow(titles[7], out)    


def mid_point_filter(k):
    #out = np.zeros(imagen.shape)
    out = imagen.copy()
    alto, ancho = out.shape

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(imagen, k, renglon, columna)
            mid = ( ventana.max() + ventana.min() )/2
            out[renglon][columna] = mid

    #out = out / out.max()
    cv2.imshow(titles[8], out)   

def alpha_mean_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape
    T=4

    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            lstVentana = window_to_list(ventana)
            for e in range(0,T):
                lstVentana.pop(0)
                lstVentana.pop()
            out[renglon][columna] = np.array(lstVentana).mean()
    cv2.imshow(titles[9], out)   

def mmse_filter(k):
    out = imagen.copy()
    alto, ancho = out.shape
    var_ruido = 1.0* cv2.getTrackbarPos('Varianza', titles[10])
    
    for renglon in range(k//2 , alto - k//2 -1):
        for columna in range(k//2, ancho - k//2 - 1):
            ventana = create_window(out, k, renglon, columna)
            var_local = ventana.var()
            med_local = ventana.mean()
            #coef = var_ruido / var_local
            if var_local != 0:
                out[renglon][columna] = out[renglon][columna] - var_ruido*(out[renglon][columna] - med_local)/var_local
    
    cv2.imshow(titles[10], out)   
   
def varianzaRuido(value):
    value = value / 1000
    mmse_filter(cv2.getTrackbarPos('Ventana', titles[10]))


imagen = cv2.imread('nala.jpg', 0)
imagen = cv2.resize(imagen, (0,0), fx=0.4, fy=0.4)
cv2.imshow('Imagen Original', imagen)


titles = ['Filtro Promedio' , 'Filtro de Media Geometrica', 'Filtro de Media Armonica', 'Filtro Media Contra Armonica',
            'Filtro de Mediana', 'Filtro de Moda', 'Filtro de Maximo', 'Filtro de Minimo', 'Filtro de Punto Medio', 'Filtro Alfa-Media',
            'Filtro de Minimo Error Cuadratico Medio (MMSE)']


functions = [mean_filter, geometric_mean_filter, armonic_median_filter, contra_armonic_filter, median_filter, mode_filter, 
            max_filter, min_filter, mid_point_filter, alpha_mean_filter, mmse_filter]

for i in range(0, len(functions)):
    cv2.imshow(titles[i], imagen)
    cv2.createTrackbar('Ventana', titles[i], 3, 35, functions[i])
    if i + 1 == len(functions):
        cv2.createTrackbar('Varianza', titles[i], 1, 30, varianzaRuido)
    cv2.waitKey(0)
    cv2.destroyWindow(titles[i])


cv2.waitKey(0)
cv2.destroyAllWindows()