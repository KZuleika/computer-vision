import cv2
import mediapipe as mp
import numpy as np
import imutils
from math import acos, degrees
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
up = False
down = False
count = 0

colorLines = (255, 255, 255)
colorHombros = (128, 0 ,255)
colorTorso = (255,191,0)

thicknessLines = 5
radiusCircles = 6
thicknessCircles = -1

with mp_pose.Pose(
     static_image_mode=False) as pose:
     while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, height = 600)
        if ret == False:
            print("ERROR al abrir el video")
            break
        
        height, width, _ = frame.shape
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        
        if results.pose_landmarks is not None:

            # POSICIONES DE LOS PUNTOS DEL CUERPO
            x1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width) #12
            y1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * height) #12
            x2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width) #14
            y2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * height) #14
            x3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width) #16
            y3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * height) #16
            
            x4 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * width) #11
            y4 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height) #11
            x5 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * width) #13
            y5 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * height) #13
            x6 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * width) #15
            y6 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height) #15
            
            x7 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x * width)#23
            y7 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y * height)#23
            x8 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x * width)#24
            y8 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * height)#24
            x9 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].x * width) #26
            y9 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * height)#26

            #PUNTOS COORDINADOS DEL CUERPO
            p1 = np.array([x1, y1])
            p2 = np.array([x2, y2])
            p3 = np.array([x3, y3])
            p4 = np.array([x4, y4])
            p5 = np.array([x5, y5])
            p6 = np.array([x6, y6])
            p7 = np.array([x7, y7])
            p8 = np.array([x8, y8])
            p9 = np.array([x9, y9])

            l1 = np.linalg.norm(p8 - p9)
            l2 = np.linalg.norm(p1 - p9)
            l3 = np.linalg.norm(p1 - p8)
            
            # Calcular el ángulo
            angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
            
            if angle >= 140:
                down = True
            if up == False and down == True and angle < 60:
                up = True
            if up == True and down == True and angle >= 60:
                count += 1
                up = False
                down = False
            
            # Visualización
            aux_image = np.zeros(frame.shape, np.uint8)
            
            #PUNTOS DEL CUERPO
            cv2.circle(aux_image, (x1,y1), radiusCircles, colorHombros, thicknessCircles)
            cv2.circle(aux_image, (x2,y2), radiusCircles, colorHombros, thicknessCircles)
            cv2.circle(aux_image, (x3,y3), radiusCircles, colorHombros, thicknessCircles)
            cv2.circle(aux_image, (x4,y4), radiusCircles, colorTorso, thicknessCircles)
            cv2.circle(aux_image, (x5,y5), radiusCircles, colorTorso, thicknessCircles)
            cv2.circle(aux_image, (x6,y6), radiusCircles, colorTorso, thicknessCircles)
            cv2.circle(aux_image, (x7,y7), radiusCircles, colorTorso, thicknessCircles)
            cv2.circle(aux_image, (x8,y8), radiusCircles, colorTorso, thicknessCircles)
            cv2.circle(aux_image, (x9,y9), radiusCircles, colorTorso, thicknessCircles)

            #HOMBROS Y CINTURA
            cv2.line(aux_image, (x1, y1), (x2, y2), colorLines, thicknessLines)
            cv2.line(aux_image, (x2, y2), (x3, y3), colorLines, thicknessLines)
            cv2.line(aux_image, (x4, y4), (x5, y5), colorLines, thicknessLines)
            cv2.line(aux_image, (x5, y5), (x6, y6), colorLines, thicknessLines)
            
            #TORSO Y PIERNAS
            cv2.line(aux_image, (x8, y8), (x9, y9), colorLines, thicknessLines)
            cv2.line(aux_image, (x1, y1), (x8, y8), colorLines, thicknessLines)
            cv2.line(aux_image, (x1, y1), (x9, y9), colorLines, thicknessLines)
            
            output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0)
            cv2.rectangle(output, (0, 0), (60, 60), (229, 204, 255), -1)
            cv2.putText(output, str(int(angle)), (x7 + 30, y7), 1, 1.5, (128, 0, 250), 2)
            cv2.putText(output, str(int(count)), (10, 50), 4, 2, (128, 0, 250), 2)
            cv2.imshow("output", output)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == 32:
            break
cap.release()
cv2.destroyAllWindows()
