import cv2
import matplotlib.pyplot as plt
import numpy as np


def ecualizacion_histograma_gray(img_gray):
    out = img_gray.copy()
    hist, edge = np.histogram(img_gray.flatten(), 256, [0,256]) 
    #print(edge)
    histacum = hist.cumsum()
    #print(histacum)
    prob = histacum / histacum.max()
    prob *= 255
    #print(prob)
    for i in range (0, img_gray.shape[0]):
        for j in range(0, img_gray.shape[1]):
            out[i][j] = prob[img_gray[i][j]]
    out = out.astype('uint8')
    #cv2.imshow('imgco', out)
    #cv2.waitKey(0)
    return out

def ecualizacion_histograma_hls(img_rgb):
    out = img.copy()
    #print(img[:,:,0].shape)
    out[:,:,2] = ecualizacion_histograma_gray(img_rgb[:,:,2])
    return out


#IMAGEN EN RGB
imgtxt= ['Farolas-LED.jpg', 'Rocas.tif']

for i in range(len(imgtxt)):
    img = cv2.imread(imgtxt[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    img_ecualizada = ecualizacion_histograma_hls(img_hls)
    img_ecualizada = cv2.cvtColor(img, cv2.COLOR_HLS2RGB)


    plt.subplot(221),plt.imshow(img)
    plt.title('Imagen Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(222)
    channels = cv2.split(img)
    plt.title("Histograma de Color")
    plt.xlabel('Bins')
    plt.ylabel('# de pixeles')
    plt.xlim((0, 256))
    colors = ('b', 'g', 'r')
    for (channel, color) in zip(channels, colors):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)
    

    plt.subplot(223),plt.imshow(img_ecualizada)
    plt.title('Ecualizacion Histograma'), plt.xticks([]), plt.yticks([])

    plt.subplot(224)
    channels = cv2.split(img_ecualizada)
    plt.title("Histograma de Color")
    plt.xlabel('Bins')
    plt.ylabel('# de pixeles')
    plt.xlim((0, 256))
    colors = ('b', 'g', 'r')
    for (channel, color) in zip(channels, colors):
        histogram = cv2.calcHist([channel], [0], None, [256], [0, 256])
        plt.plot(histogram, color=color)

    plt.savefig(imgtxt[i]+"HistHLS"+".png", dpi = 600)
    plt.show()
