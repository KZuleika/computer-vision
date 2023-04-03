import cv2
import mediapipe as mp
import numpy as np

mp_selfie_segmentation = mp.solutions.selfie_segmentation

Fondo1 = cv2.VideoCapture('CarreteraBosque.mp4')
cv2.namedWindow('Cambio de fondo')

cap = cv2.VideoCapture(0)
with mp_selfie_segmentation.SelfieSegmentation(
     model_selection=0) as selfie_segmentation:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    
    image = cv2.flip(image,1)
    Alto, Ancho, _ = image.shape
    results = selfie_segmentation.process(image)
    
    cv2.imshow('Original', image)

    _, Mascara = cv2.threshold(results.segmentation_mask, 0.50, 255, cv2.THRESH_BINARY)
    Mascara = Mascara.astype(np.uint8)
    Mascara =  cv2.medianBlur(Mascara, 13)

    Mascara_inv = cv2.bitwise_not(Mascara)

    #cv2.imshow('mascara', Mascara) 
    #cv2.imshow('mascara invertida', Mascara_inv)


    _, Fondo = Fondo1.read()
    Fondo = cv2.resize (Fondo, (Ancho, Alto), interpolation = cv2.INTER_CUBIC)

    Fondo = cv2.bitwise_and(Fondo, Fondo, mask = Mascara_inv)
    Personas = cv2.bitwise_and(image, image, mask=Mascara)

    #cv2.imshow('fondo', Fondo)
    #cv2.imshow('personas', Personas)


    NuevoFondo = cv2.add(Fondo, Personas)
    cv2.imshow("Cambio de Fondo", NuevoFondo)
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
