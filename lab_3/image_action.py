import cv2
import matplotlib.pyplot as plt
from numpy import ndarray
import os

from numpy.ma.core import resize


def read_image(name_of_input_image: str) -> ndarray:
    """
    Reades an image using OpenCV
    :param name_of_input_image: Name of input image
    :return: The image as a NumPy array
    """

    img = cv2.imread(name_of_input_image)
    return img


def show_image(img: ndarray) -> ndarray:
    """
    Showes an image using OpenCV and show its dimensions
    :param img: The image as a NumPy array
    :return: The input image as a NumPy array.
    """

    cv2.imshow('image', img)
    cv2.waitKey(0)

    height, width = img.shape[:2]
    print(f'Высота входящего изображения: {height}\nШирина входящего изображения: {width}\n')

    return img


def resize_image(img: ndarray, width: int, height: int):
    """
    Resizes the image according to the specified height and width
    :param img: The image as a NumPy array
    :param width: Specified width
    :param height: Specified height
    :return: Resized image
    """

    new_size = (width, height)

    resized_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    return resized_img


def save_output_image(resized_img: ndarray, name_of_output_image: str) -> None:
    """
    Saves the resized image
    :param resized_img: The resized image
    :param name_of_output_image: The name of output image
    """
    cv2.imwrite(name_of_output_image, resized_img)
