import cv2
import mediapipe as mp
import math
mp_selfie_segmentation = mp.solutions.selfie_segmentation

##mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_selfie_segmentation.SelfieSegmentation(
     model_selection=1) as selfie_segmentation:
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
    cv2.imshow("Mascara", results.segmentation_mask)
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
