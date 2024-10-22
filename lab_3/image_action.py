import cv2
import matplotlib.pyplot as plt
from numpy import ndarray
import os

from numpy.ma.core import resize


def read_image(name_of_input_image: str):

    img = cv2.imread(name_of_input_image)
    return img


def show_image(img: ndarray) -> ndarray:

    cv2.imshow('image', img)
    cv2.waitKey(0)

    height, width = img.shape[:2]
    print(f'Высота входящего изображения: {height}\nШирина входящего изображения: {width}')

    return img

def resize_image(img: ndarray, width: int, height: int):

    new_size = (width, height)

    resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    return resized_img