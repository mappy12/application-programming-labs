import cv2
import matplotlib.pyplot as plt
from numpy import ndarray
import os


def show_image(name_of_input_image: str) -> ndarray:

    img = cv2.imread(name_of_input_image)
    cv2.imshow('image', img)
    cv2.waitKey(0)

    height, width = img.shape[:2]
    print(f'Высота входящего изображения: {height}\nШирина входящего изображения: {width}')

    return img
