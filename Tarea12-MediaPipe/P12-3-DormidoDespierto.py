import cv2
import mediapipe as mp
import time
import numpy as np
from playsound import playsound

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

ojo_izquierdo_sup_puntos = [161, 159, 157]
ojo_izquierdo_inf_puntos = [163, 145, 154]
ojo_derecho_sup_puntos = [384, 386, 388] 
ojo_derecho_inf_puntos = [381, 374, 390]
lagrimal_puntos = [243, 463]

def eye_close_open(face_result):
  ojos = False
  coordenadas_izq_sup = []
  coordenadas_izq_inf = []
  coordenadas_der_sup = []
  coordenadas_der_inf = []
  coordenadas_lagrimal = []

  for face_landmarks in face_result.multi_face_landmarks:
    for index in ojo_izquierdo_sup_puntos:
      x = int(face_landmarks.landmark[index].x * ancho)
      y = int(face_landmarks.landmark[index].y * alto)
      coordenadas_izq_sup.append([x,y])
    for index in ojo_izquierdo_inf_puntos:
      x = int(face_landmarks.landmark[index].x * ancho)
      y = int(face_landmarks.landmark[index].y * alto)
      coordenadas_izq_inf.append([x,y])
    for index in ojo_derecho_sup_puntos:
      x = int(face_landmarks.landmark[index].x * ancho)
      y = int(face_landmarks.landmark[index].y * alto)
      coordenadas_der_sup.append([x,y])
    for index in ojo_derecho_inf_puntos:
      x = int(face_landmarks.landmark[index].x * ancho)
      y = int(face_landmarks.landmark[index].y * alto)
      coordenadas_der_inf.append([x,y])
    for index in lagrimal_puntos:
      x = int(face_landmarks.landmark[index].x * ancho)
      y = int(face_landmarks.landmark[index].y * alto)
      coordenadas_lagrimal.append([x,y])
    
  #Puntos del ojo
  izq_sup = np.array(coordenadas_izq_sup)
  izq_inf = np.array(coordenadas_izq_inf)
  der_sup = np.array(coordenadas_der_sup)
  der_inf = np.array(coordenadas_der_inf)
  lagrimal = np.array(coordenadas_lagrimal)

  #lineas ojo izquierdo 
  dist_izq = np.linalg.norm(izq_sup - izq_inf)
  #print('distizq',dist_izq)
  ojo_izq = dist_izq <= 7

  #Lineas del Ojo derecho
  dist_der = np.linalg.norm(der_sup - der_inf)
  #print('distder', dist_der)
  ojo_der = dist_der <= 7
  #print('ojoiz,der', ojo_izq, ojo_der)
  ojos = np.append(ojo_izq, ojo_der)
  return ojos

rawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
dormido = False

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    alto, ancho, _ = image.shape
    results = face_mesh.process(image)
    
    if results.multi_face_landmarks:
      ojos = eye_close_open(results)
      if not True in ojos:
        cv2.putText(image, 'DESPIERTO', (10,30), 1, 1.5, (0,0,180),2)
        dormido = False
      elif not False in ojos:
        cv2.putText(image, 'DORMIDO', (10,30), 1, 1.5, (0,0,180),2)
        if dormido == False:
          start_dormido = time.time()
          dormido = True
        elif dormido == True:
          end_dormido = time.time()
          cv2.putText(image, str(round(end_dormido - start_dormido, 2))+ 'seg', (10,50), 1, 1.5, (0,0,180),2)
          if end_dormido - start_dormido >= 3.0:
            print('REPRODUCIR ALARMA')
            playsound('alarma-kikiriki.mp3')
            #playsound('tik-tok-lyrics.mp3')

            
        
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', image)
    #cv2.waitKey(0)
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
cv2.destroyAllWindows()