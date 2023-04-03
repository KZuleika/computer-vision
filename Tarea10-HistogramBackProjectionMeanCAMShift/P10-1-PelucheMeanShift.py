#https://docs.opencv.org/3.4/d7/d00/tutorial_meanshift.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

captura = cv2.VideoCapture(0)

# take first frame of the video
rret, first_frame = captura.read()
print (first_frame.shape)

obj_rgb = cv2.imread('waltercara.png')
x = 0
y = 0
h = 200
w = 200
track_window = (x,y,w,h)

obj_hsv = cv2.cvtColor(obj_rgb, cv2.COLOR_BGR2HSV)
obj_hist = cv2.calcHist([obj_hsv], [0], None, [180], [0, 180])
obj_hist = cv2.normalize(obj_hist, obj_hist, 0, 255, cv2.NORM_MINMAX)


# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while (captura.isOpened()):
  ret, imagen = captura.read()

  if ret == True:
    hsv_captura = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    mask = cv2.calcBackProject([hsv_captura],[0],obj_hist,[0,180],1)

    # apply meanshift to get the new location
    ret, track_window = cv2.meanShift(mask, track_window, term_crit) 
    # Draw it on image
    x,y,w,h = track_window
    imagen = cv2.rectangle(imagen, (x,y), (x+w,y+h), 255,2)

    cv2.imshow('video', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
cv2.destroyAllWindows()
