import cv2
import mediapipe as mp
import numpy as np
import math

contador1, contador2 = 0,0
Xm_before, Ym_before = [0,0], [0,0]

def startpoint()
    return

def paint_point(y,x, img, color, thickness):
    out = img.copy()
    for i in range(0,3):
        out[x-thickness:x+thickness, y-thickness : y+thickness, i] = color[i]
    return out

class realTimeDraw:
    def __init__(self):
       self.color = (255,255,255)
       self.thickness = 2
       self.x1 = 0
       self.x2 = 0
       self.y1 = 0
       self.y2 = 0
            
    def paint_line(img):
        return out

 

 
 
