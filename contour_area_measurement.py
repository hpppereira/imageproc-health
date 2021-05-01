# Calculo da area de uma feicao

import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
plt.close('all')

def plot_rgb(img):
    cv2.imshow('2', img)
    plt.imshow(img[:,:,0])
    return

def find_edges(img):
    edges = cv2.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    return

if __name__ == "__main__":

    pathname = os.environ['HOME'] + '/gdrive/henrique/mae/Exames_medicos/ACCamargo/11749-Mamografia_Digital_Bilateral_20191002/Mamografia_Digital_Biltateral_exm_20191002/'
    filename = 'jpeg\image_s0001_i0001.jpg'

    img = cv2.imread(pathname + filename, 0)

    # plot_rgb(im)

    ret, threshold = cv2.threshold(img, 20, 80, 0)

    contours, hirerchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


plt.show()

