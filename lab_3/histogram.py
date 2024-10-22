import cv2
import matplotlib.pyplot as plt
from numpy import ndarray

def create_hist(img: ndarray):

    list_of_histograms = []

    for i in range(0,3):
        hist = cv2.calcHist(img, [i], None, [256], [0,256])
        list_of_histograms.append(hist)

    return list_of_histograms

def draw_histogram(list_of_histograms: list):

    colors = ['b','g','r']
    labels = ['Blue channel', 'Green channel', 'Red channel']


    plt.figure(figsize=(10,5))

    for i, hist in enumerate(list_of_histograms):
        plt.plot(hist, color = colors[i], label = labels[i])

    plt.title('Histogram of image')
    plt.xlabel('Pixel intensity value')
    plt.ylabel('Number of pixels')

    plt.legend()
    plt.show()

