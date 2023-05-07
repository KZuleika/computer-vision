import cv2
import os
import imutils
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

#personName = 'JoseFelipe'
personName = 'JoseFelipeCubrebocasMal'
dataPath = 'C:/Users/kzcoc/OneDrive - Universidad Autonoma de Yucatan/8SEMM/VisionPorComputadora/Tarea17-ReconocimientoRostro'  #Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)
    
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
count = 0
count_offset = 51
Dataset_Size = 50

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
while True:  
    ret, frame = cap.read()
    if ret == False: break
    frame =  imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count+count_offset),rostro)
        count = count + 1
    cv2.imshow('frame',frame)
    #cv2.imshow('Rostro',rostro)
    k =  cv2.waitKey(1)
    if k == 32  or count >= Dataset_Size:
        break
cap.release()
cv2.destroyAllWindows()
