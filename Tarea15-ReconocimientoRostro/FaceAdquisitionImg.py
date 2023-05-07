import cv2
import os
import imutils
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

personName = 'RamsesCubrebocasMal'
dataPath = 'C:/Users/kzcoc/OneDrive - Universidad Autonoma de Yucatan/8SEMM/VisionPorComputadora/Tarea17-ReconocimientoRostro'  #Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)
    
count = 0
count_offset = 3
Dataset_Size = 23


with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
    for i in range(25,60):
        fileName = 'Personas/RamsesCubrebocasMaal/WIN_20230428_07_46_'+ str(i) + '_Pro.jpg'
        print(fileName)
        image = cv2.imread(fileName)

        image = cv2.flip(image,1)
        image =  imutils.resize(image, width=640)
        Alto, Ancho, _ = image.shape
        results = face_detection.process(image)              
        if results.detections:
            for detection in results.detections:
                x = int(detection.location_data.relative_bounding_box.xmin * Ancho)
                y = int(detection.location_data.relative_bounding_box.ymin * Alto)
                w = int(detection.location_data.relative_bounding_box.width * Ancho)
                h = int(detection.location_data.relative_bounding_box.height * Alto)
                if x < 0 and y < 0:
                    continue
                rostro = image[y : y + h, x : x + w]
                #rostro = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)
                rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count+count_offset),rostro)
                count = count + 1
                mp_drawing.draw_detection(image, detection)            
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    cv2.imshow('Rostro', rostro)
cv2.destroyAllWindows()
