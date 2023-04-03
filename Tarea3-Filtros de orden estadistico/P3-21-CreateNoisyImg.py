import cv2
import numpy as np
import random
import matplotlib.pyplot as plt


def gaussian_noise(img, mean, std):
    out = img.copy()
    out = out.astype(float) / 255.0
    noise = np.random.normal(loc= mean, scale=std, size=out.shape)
    out = out + noise

    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out


def SaltPepper_Noise(img, pSalt, pPepper):
    out = img.copy()
    pSalt = 1 - pSalt
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            p = random.random()
            if p < pPepper:
                out[i][j] = 0
            elif p > pSalt:
                out[i][j] = 255                

    return out

def uniform_Noise(img):
    out = img.copy()
    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            out[i][j] += random.random()          
    return out

def gaussSaltPepper_noise(img, mean, std, pSalt, pPepper):
    pSalt = 1 - pSalt
    out = img.copy()
    out = out.astype(float) / 255.0
    noise = np.random.normal(loc= mean, scale=std, size=out.shape)
    out = out + noise

    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)

    for i in range(out.shape[0]):
        for j in range(out.shape[1]):
            p = random.random()
            if p < pPepper:
                out[i][j] = 0
            elif p > pSalt:
                out[i][j] = 255         
    return out



img = cv2.imread("nala.jpg", 0)
img = cv2.resize(img, (0,0), fx=0.4, fy=0.4)

cv2.imshow('Imagen original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

noisyImg = []
titleNoise = ['Gauss', 'uniforme', 'sal', 'pimienta', 'salpimienta', 'gausssalpimienta']

noisyImg.append(gaussian_noise(img, 0.02, 0.01))
noisyImg.append(uniform_Noise(img))
noisyImg.append(SaltPepper_Noise(img, 0.05, 0))
noisyImg.append(SaltPepper_Noise(img, 0, 0.05))
noisyImg.append(SaltPepper_Noise(img, 0.05, 0.05))
noisyImg.append(gaussSaltPepper_noise(img, 0, 0.01, 0.025, 0.025))



for i in range(len(noisyImg)):
    cv2.imshow('Imagen con ruido '+titleNoise[i], noisyImg[i])
    cv2.imwrite(titleNoise[i]+'.jpg', noisyImg[i])
    cv2.waitKey(0)
    cv2.destroyWindow('Imagen con ruido '+titleNoise[i])
    

cv2.waitKey(0)
cv2.destroyAllWindows()