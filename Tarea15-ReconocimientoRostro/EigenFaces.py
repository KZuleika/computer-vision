import cv2
import os
import imutils
import mediapipe as mp

colorfont = (147,20,255)
fontsize = 0.75

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

dataPath = 'C:/Users/kzcoc/OneDrive - Universidad Autonoma de Yucatan/8SEMM/VisionPorComputadora/Tarea17-ReconocimientoRostro/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

# Leyendo el modelo
face_recognizer = cv2.face.EigenFaceRecognizer_create()
face_recognizer.read('modeloEigenFace.xml')


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                break
            frame = cv2.flip(frame,1)
            frame =  imutils.resize(frame, width=640)
            alto, ancho, _ = frame.shape
            
            results = face_detection.process(frame)              
            if results.detections:
                for detection in results.detections:
                    x = int(detection.location_data.relative_bounding_box.xmin * ancho)
                    y = int(detection.location_data.relative_bounding_box.ymin * alto)
                    w = int(detection.location_data.relative_bounding_box.width * ancho)
                    h = int(detection.location_data.relative_bounding_box.height * alto)
                    if x < 0 and y < 0:
                        continue

                    rostro = frame[y : y + h, x : x + w]
                    rostro = imutils.resize(rostro,width=150)
                    if rostro.shape != (150,150):
                        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)    
                    rostro = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)
                    cv2.imshow('rostro', rostro)

                    result = face_recognizer.predict(rostro)
                    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

                     
                    # EigenFaces
                    if result[1] < 7500:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,fontsize,colorfont,1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    else:
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                cv2.imshow('EigenFaces',frame)
            k = cv2.waitKey(1)
            if k == 32:
                break
cap.release()
cv2.destroyAllWindows()
