import cv2
import matplotlib.pyplot as plt
import numpy as np


def ecualizacion_histograma_gray(img_gray):
    out = img_gray.copy()
    hist, _ = np.histogram(img_gray.flatten(), 256, [0,256]) 
    histacum = hist.cumsum()
    prob = histacum / histacum.max()
    prob *= 255
    for i in range (0, img_gray.shape[0]):
        for j in range(0, img_gray.shape[1]):
            out[i][j] = prob[img_gray[i][j]]
    out = out.astype('uint8')
    return out

def ecualizacion_histograma_hls(img_hls):
    out = img_hls.copy()
    for channel in range(out.shape[2]):
        out[:,:,channel] = ecualizacion_histograma_gray(out[:,:,channel])
    return out


#IMAGEN EN RGB
imgtxt= ['Farolas-LED.jpg', 'Rocas.tif']

for i in range(len(imgtxt)):
    img = cv2.imread(imgtxt[i])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    img_ecualizada = ecualizacion_histograma_hls(img_hls)
    img_ecualizada = cv2.cvtColor(img_ecualizada, cv2.COLOR_HLS2RGB)


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
    plt.show()
