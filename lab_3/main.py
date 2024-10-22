import argparse
import os
from argparse import ArgumentParser

import cv2
import matplotlib.pyplot as plt

def parser_create():

    parser = argparse.ArgumentParser()

    parser.add_argument('name_of_input_image', type=str, help='Name of input image')
    return parser.parse_args()

def main():

    args = parser_create()
    name_of_input_image = args.name_of_input_image + '.jpg'

    img = cv2.imread(name_of_input_image)
    cv2.imshow('cat', img)
    cv2.waitKey(0)

    height, width = img.shape[:2]

    print(f"Высота изображения: {height}\nШирина изображения: {width}")

if __name__ == "__main__":
    main()


    #
    # cat = cv2.imread()
    #
    # img_size = cat.shape
    # print(img_size)
