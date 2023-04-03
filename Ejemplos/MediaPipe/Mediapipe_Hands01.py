import cv2
import mediapipe as mp
import math
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    static_image_mode = False,
    max_num_hands = 2,
    min_detection_confidence = 0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    image = cv2.flip(image,1)
    Alto, Ancho, _ = image.shape
    results = hands.process(image)
    
    print('Manos:', results.multi_handedness)
    print('Hand landmarks:', results.multi_hand_landmarks)
    
    #image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          
##          mp_drawing.draw_landmarks(image, hand_landmarks)
##          mp_drawing.draw_landmarks(
##          image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
##          mp_drawing.DrawingSpec(color=(255,255,0), thickness=4, circle_radius=5),
##          mp_drawing.DrawingSpec(color=(255,0,255), thickness=4))
##
          X1 =  int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x*Ancho)        
          Y1 =  int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y*Alto)
          X2 =  int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x*Ancho)        
          Y2 =  int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y*Alto)
          D = math.sqrt(pow((X1-X2),2)+pow((Y1-Y2), 2))
          Xm = int((X1 + X2)/2)
          Ym = int((Y1 + Y2)/2)
          cv2.line(image, (X1,Y1), (X2,Y2), (0,255,255), 2)
          cv2.putText(image, "D={:.2f}".format(D), (Xm+10, Ym), 1, 1.5, (0,255,0),2)
          cv2.circle(image, (Xm, Ym), 2, (0,0,255))

        
     # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
