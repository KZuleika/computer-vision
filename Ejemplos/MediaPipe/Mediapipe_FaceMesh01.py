import cv2
import mediapipe as mp
import math
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    static_image_mode = False,
    max_num_faces=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    Alto, Ancho, _ = image.shape
    results = face_mesh.process(image)
    #print("Face Landmarks: ", results.multi_face_landmarks)
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
          
        ##mp_drawing.draw_landmarks(image, face_landmarks)
        

##          mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_LIPS)
##        
##        mp_drawing.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_CONTOURS,
##        mp_drawing.DrawingSpec(color=(0,0,255), thickness = 1, circle_radius = 1),
##        mp_drawing.DrawingSpec(color=(255,0,0), thickness = 1))
##        
        PosX1 = int(face_landmarks.landmark[159].x*Ancho)
        PosY1 = int(face_landmarks.landmark[159].y * Alto)
        cv2.circle(image, (PosX1, PosY1), 10, (0,0,255))
        PosX2 = int(face_landmarks.landmark[145].x*Ancho)
        PosY2 = int(face_landmarks.landmark[145].y * Alto)
        cv2.circle(image, (PosX2, PosY2), 10, (0,0,255))
        print(PosX1, PosY1, PosX2, PosY2)
        
     # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
