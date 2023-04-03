import cv2

firstImg = True
def calculateAbsDif(lastImg, newImg):
    return cv2.absdiff(lastImg,newImg)

captura = cv2.VideoCapture(0)
while (captura.isOpened()):
  ret, imagen = captura.read()

  if(firstImg): 
        lastImage = imagen
        firstImg=False
  if ret == True:
    cv2.imshow('video', imagen)
    cv2.imshow('diferencia', calculateAbsDif(lastImage, imagen))
    lastImage = imagen
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
  
captura.release()
cv2.destroyAllWindows()


