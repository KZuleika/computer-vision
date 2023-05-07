import cv2
import mediapipe as mp
import numpy as np
import math

class realTimeDraw:
    def __init__(self, color = (255,255,255), thickness = 2):
       self.color = color
       self.thickness = thickness
       self.x1 = 0
       self.x2 = 0
       self.y1 = 0
       self.y2 = 0
       self.firstPoint = True

    def shift_xy(self, newX, newY):
        self.x1 = self.x2
        self.x2 = newX

        self.y1 = self.y2
        self.y2 = newY
        return

    def draw_point(self, img):
        out = img.copy()
        x = self.x2
        y = self.y2
        thickness = self.thickness
        color = self.color
        for i in range(0,3):
            out[x-thickness:x+thickness, y-thickness : y+thickness, i] = color[i]
        return out

    def paint_line(self, img, x, y):
        out = np.copy(img)
        self.shift_xy(x, y)
        if self.firstPoint == True:
            self.firstPoint = False
            return out
        start = (self.x1, self.y1)
        end = (self.x2, self.y2)
        lcolor = self.color
        lthickness = self.thickness
        out = cv2.line(out, start, end, lcolor, lthickness)
        return out
 

def paint_point(y,x, img, color, thickness):
    out = img.copy()
    for i in range(0,3):
        out[x-thickness:x+thickness, y-thickness : y+thickness, i] = color[i]
    return out
 
