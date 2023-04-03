import cv2
import mediapipe as mp
import numpy as np
import math
mp_selfie_segmentation = mp.solutions.selfie_segmentation

##mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_selfie_segmentation.SelfieSegmentation(
     model_selection=0) as selfie_segmentation:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    image = cv2.flip(image,1)
    Alto, Ancho, _ = image.shape
    results = selfie_segmentation.process(image)
    
    cv2.imshow('Original', image)
    #cv2.imshow("Mascara", results.segmentation_mask)

    _, Mascara = cv2.threshold(results.segmentation_mask, 0.50, 255, cv2.THRESH_BINARY)
    Mascara = Mascara.astype(np.uint8)
    Mascara =  cv2.medianBlur(Mascara, 13)
          
    #cv2.imshow("Mascara (con Umbral)", Mascara)
    Mascara_inv = cv2.bitwise_not(Mascara) 
    #cv2.imshow("Mascara (Inversa)", Mascara_inv)
    Fondo = cv2.imread("Fondo3.jpg")
    Fondo = cv2.resize(Fondo, (Ancho, Alto), interpolation=cv2.INTER_CUBIC)
    Fondo = cv2.bitwise_and(Fondo, Fondo, mask=Mascara_inv)
    Personas = cv2.bitwise_and(image, image, mask=Mascara)
    #cv2.imshow("Fondo)", Fondo)
    #cv2.imshow("Personas", Personas)
    NuevoFondo = cv2.add(Fondo, Personas)
    cv2.imshow("Cambio de Fondo", NuevoFondo)
    
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
