import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

filenames =['Avion', 'Bailarina', 'Ballet', 'Mariposa', 'Mujer', 'Paloma', 'Patada', 'Pez']
h = [[],[],[],[],[],[],[],[]]

for f in range(len(filenames)):
    src = cv2.imread('Capturas/'+filenames[f]+'.jpg', 0)
    _, aux = cv2.threshold(src,120,1,cv2.THRESH_BINARY_INV)
    cv2.imshow('binary img',aux)

    moments = cv2.moments(aux)
    huMoments = cv2.HuMoments(moments)

    huMoments_norm_list = np.ndarray.tolist(huMoments)

    for i in range(0,7):
        h[i].append(huMoments_norm_list[i])

    cv2.waitKey(0)

data = {'img_names' : filenames, 
        'h1': h[0], 
        'h2': h[1],
        'h3': h[2], 
        'h4': h[3],
        'h5': h[4], 
        'h6': h[5],
        'h7': h[6]}
df_HuMoments = pd.DataFrame(data)
df_HuMoments.to_csv('huMoments.csv')
