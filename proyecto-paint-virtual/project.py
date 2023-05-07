from fingerfunctions import *
from paintfunctions import  *
import cv2
import mediapipe as mp
import numpy as np
import math

mydraw = realTimeDraw(color=(0,255,255), thickness=5)
cap = cv2.VideoCapture(0)

cv2.namedWindow('Dibujo')
imgPizarra = cv2.imread('pizarra.jpg')

# Dedos en MediaPipe
thumb_points = [1,2,4] 
palm_points = [0, 1, 2, 5, 9, 13, 17]
fingertips_points = [8, 12, 16, 20]
finger_base_points =[6, 10, 14, 18]

#Posiciones de los dedos
PIEDRA = np.array([False, False, False, False, False])
PAPEL = np.array([True, True, True, True, True])
CLIC = np.array([False, True, True, False, False])


with mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 1,
    min_detection_confidence = 0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
#_______________________ Fondo para dibujar ____________________
        scale_percent = 100 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        imgPizarra = cv2.resize(imgPizarra,dim, interpolation = cv2.INTER_AREA)
       
#_________________ Imagen de la camara ________________________
        
        image = cv2.flip(image,1)
        alto, ancho, _ = image.shape
        results = hands.process(image)
      
        if results.multi_hand_landmarks:
            fingers = fingers_up_down(results, thumb_points, 
                                      palm_points, fingertips_points, finger_base_points,
                                      alto, ancho)


            if not False in (fingers == PIEDRA):
                cv2.putText(image, 'PIEDRA', (10,30), 1, 1.5, (0,0,180),2)
                mydraw.firstPoint = True  
            elif not False in (fingers == PAPEL):
                cv2.putText(image, 'PAPEL', (10,30), 1, 1.5, (0,0,180),2)
                mydraw.firstPoint = True
            elif not False in (fingers == CLIC):
                cv2.putText(image, 'TIJERA', (10,30), 1, 1.5, (0,0,180),2)
                tip_position = clic_position(results,fingertips_points, alto, ancho)
                (x,y) = tip_position
                imgPizarra = mydraw.paint_line(imgPizarra, x, y)
                #imgPizarra = paint_point(tip_position[0], tip_position[1], imgPizarra, (0,0,255), 5)
            else:
                mydraw.firstPoint = True    

        cv2.imshow('MediaPipe Hands', image)
        cv2.imshow('Dibujo', imgPizarra)
        if cv2.waitKey(5) & 0xFF == 32:
            break
cap.release()