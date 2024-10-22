import argparse
import cv2
import matplotlib.pyplot as plt
import os

from histogram import *
from image_action import *



def parser_create():

    parser = argparse.ArgumentParser()

    parser.add_argument('name_of_input_image', type=str, help='Name of input image')
    return parser.parse_args()

def main():

    args = parser_create()
    name_of_input_image = args.name_of_input_image + '.jpg'

    img = show_image(name_of_input_image)

    list_of_histograms = create_hist(img)
    draw_histogram(list_of_histograms)


if __name__ == "__main__":
    main()
