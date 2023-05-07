import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

thumb_points = [1,2,4] 
palm_points = [0, 1, 2, 5, 9, 13, 17]
fingertips_points = [8, 12, 16, 20]
finger_base_points =[6, 10, 14, 18]


def palm_centroid(coordinates_list):
    coordinates = np.array(coordinates_list)
    centroid = np.mean(coordinates, axis=0)
    centroid = int(centroid[0]), int(centroid[1])
    return centroid

def clic_position(hand_results, fingertips_points, alto, ancho):
    coordenadas_puntadedo = []
    clic_points = [fingertips_points[0]]

    for hand_landmarks in hand_results.multi_hand_landmarks:
        for index in clic_points:
            x = int(hand_landmarks.landmark[index].x * ancho)
            y = int(hand_landmarks.landmark[index].y * alto)
            coordenadas_puntadedo.append([x,y]) 
            
    coordenadas_puntadedo = np.array(coordenadas_puntadedo)
    centroid = np.mean(coordenadas_puntadedo, axis=0)
    centroid = int(centroid[0]), int(centroid[1])
    print(centroid)
    return centroid

def fingers_up_down(hand_results, thumb_points, palm_points, fingertips_points, finger_base_points, alto, ancho):
    fingers = None
    coordenadas_pulgar = []
    coordenadas_palma = []
    coordenadas_puntadedo = []
    coordenadas_basededo = []

    for hand_landmarks in hand_results.multi_hand_landmarks:
        for index in thumb_points:
            x = int(hand_landmarks.landmark[index].x * ancho)
            y = int(hand_landmarks.landmark[index].y * alto)
            coordenadas_pulgar.append([x,y])
        for index in palm_points:
            x = int(hand_landmarks.landmark[index].x * ancho)
            y = int(hand_landmarks.landmark[index].y * alto)
            coordenadas_palma.append([x,y])
        for index in fingertips_points:
            x = int(hand_landmarks.landmark[index].x * ancho)
            y = int(hand_landmarks.landmark[index].y * alto)
            coordenadas_puntadedo.append([x,y]) 
        for index in finger_base_points:
            x = int(hand_landmarks.landmark[index].x * ancho)
            y = int(hand_landmarks.landmark[index].y * alto)
            coordenadas_basededo.append([x,y])
        
        # Puntos del pulgar
        p1 = np.array(coordenadas_pulgar[0])
        p2 = np.array(coordenadas_pulgar[1])
        p3 = np.array(coordenadas_pulgar[2])

        #Lineas del pulgar
        l1 = np.linalg.norm(p2-p3)
        l2 = np.linalg.norm(p1 - p3)
        l3 = np.linalg.norm(p1 - p2)

        #Calcular el angulo del pulgar
        pulgar_angulo = (l1**2 + l3**2 - l2**2) / (2 * l1 * l3)
        if int(pulgar_angulo) == -1:
            angulo = 180
        else:
            angulo = math.degrees(math.acos(pulgar_angulo))
        if angulo > 150:
            dedo_pulgar = np.array(True)
        else:
            dedo_pulgar = np.array(False)

        # DEDOS INDICE, MEDIO, ANULAR Y ME'IQUE
        palmaX, palmaY = palm_centroid(coordenadas_palma)
        coordenadas_centroide = np.array([palmaX, palmaY])
        coordenadas_basededo = np.array(coordenadas_basededo)
        coordenadas_puntadedo = np.array(coordenadas_puntadedo)

        # Distancias dedo a palma
        dist_puntadedo = np.linalg.norm(coordenadas_centroide - coordenadas_puntadedo, axis = 1)
        dist_basededo = np.linalg.norm(coordenadas_centroide - coordenadas_basededo, axis = 1)
        diferencia = dist_puntadedo - dist_basededo
        fingers = diferencia > 0    
        fingers = np.append(dedo_pulgar, fingers)
    return fingers



