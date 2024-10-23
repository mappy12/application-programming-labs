import argparse
import cv2
import matplotlib.pyplot as plt
import os

from histogram import *
from image_action import *


def parser_create() -> tuple:
    """
    Parses the arguments from terminal
    :return: tuple of arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('name_of_input_image', type=str, help='Name of input image')
    parser.add_argument('name_of_output_image', type=str, help='Name of output image')
    parser.add_argument('height', type=int, help="New image height")
    parser.add_argument('width', type=int, help="New image width")

    return parser.parse_args()


def main():

    try:
        args = parser_create()
        name_of_input_image = args.name_of_input_image + '.jpg'

        img = read_image(name_of_input_image)
        show_image(img)
    except Exception:
        print('Невозможно прочитать изображение')

    try:
        list_of_histograms = create_hist(img)
        draw_histogram(list_of_histograms)
    except Exception:
        print('Невозможно построить гистограмму')

    resized_img = resize_image(img, args.width, args.height)
    show_image(resized_img)

    save_output_image(resized_img, args.name_of_output_image)


if __name__ == "__main__":
    main()
