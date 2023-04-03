import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
with mp_pose.Pose(
    static_image_mode=False) as pose:
  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      #print("Ignoring empty camera frame.")
      continue
  
    image = cv2.flip(image,1)
    Alto, Ancho, _ = image.shape
    results =  pose.process(image)
    print(results.pose_landmarks);
    if results.pose_landmarks is not None:
      mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(128, 0, 250), thickness=2, circle_radius=3),
                mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))

          
        

      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 32:
        break
cap.release()
