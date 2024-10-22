import cv2
import matplotlib.pyplot as plt
from numpy import ndarray

def create_hist(img: ndarray):

    list_of_histograms = []

    for i in range(0,3):
        hist = cv2.calcHist(img, [i], None, [256], [0,256])
        list_of_histograms.append(hist)

    return list_of_histograms




