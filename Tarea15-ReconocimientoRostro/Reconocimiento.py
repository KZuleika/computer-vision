import cv2
import os
import imutils
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

dataPath = 'C:/Users/kzcoc/OneDrive - Universidad Autonoma de Yucatan/8SEMM/VisionPorComputadora/Tarea17-ReconocimientoRostro/Data' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

# Leyendo el modelo
##face_recognizer = cv2.face.EigenFaceRecognizer_create()
##face_recognizer.read('modeloEigenFace.xml')

#face_recognizer = cv2.face.FisherFaceRecognizer_create()
#face_recognizer.read('modeloFisherFace.xml')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('modeloLBPHFace.xml')

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
            Alto, Ancho, _ = frame.shape
            
            results = face_detection.process(frame)              
            if results.detections:
                for detection in results.detections:
                    x = int(detection.location_data.relative_bounding_box.xmin * Ancho)
                    y = int(detection.location_data.relative_bounding_box.ymin * Alto)
                    w = int(detection.location_data.relative_bounding_box.width * Ancho)
                    h = int(detection.location_data.relative_bounding_box.height * Alto)
                    if x < 0 and y < 0:
                        continue
                    rostro = frame[y : y + h, x : x + w]
                    rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                    rostro = cv2.cvtColor(rostro, cv2.COLOR_BGR2GRAY)
                    result = face_recognizer.predict(rostro)
                    cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
                    # EigenFaces
##                    if result[1] < 5000:
##                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
##                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
##                    else:
##                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
##                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
                    # FisherFace
##                    if result[1] < 5000:
##                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
##                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
##                    else:
##                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
##                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
        
                    # LBPHFace
                    if result[1] < 90:
                        cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
                    else:
                        cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
                        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
                        print(result[1])
                cv2.imshow('frame',frame)
            k = cv2.waitKey(1)
            if k == 32:
                break
cap.release()
cv2.destroyAllWindows()
