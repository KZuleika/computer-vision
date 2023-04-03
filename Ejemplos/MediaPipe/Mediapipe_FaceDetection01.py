import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.75) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue
    image= cv2.flip(image, 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)
    Alto, Ancho, _ = image.shape
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.detections:
      for detection in results.detections:
        print(detection)
        mp_drawing.draw_detection(image, detection)
        
        PosX1 = int(detection.location_data.relative_keypoints[0].x * Ancho)
        PosY1 = int(detection.location_data.relative_keypoints[0].y * Alto)
                
        PosX2 = int(detection.location_data.relative_keypoints[1].x * Ancho)
        PosY2 = int(detection.location_data.relative_keypoints[1].y * Alto)

        cv2.putText(image, "Ojo1", (PosX1 - 50, PosY1), 1, 1.5, (0,255,0),2)
        cv2.putText(image, "Ojo2", (PosX2 + 5, PosY2), 1, 1.5, (0,255,255),2)

        cv2.line(image, (PosX1, PosY1), (PosX2, PosY2), (255, 0, 0), 2)
        cv2.line(image, (PosX1, PosY1), (PosX2, PosY1), (255, 0, 0), 2)

        
        
    cv2.imshow('MediaPipe Face Detection', image)
    if cv2.waitKey(5) & 0xFF == 32:
      break
cap.release()
