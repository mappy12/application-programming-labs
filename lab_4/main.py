import cv2
import numpy as np
import pandas as pd

def get_dementions(path_to_image):

    img = cv2.imread(path_to_image)

    height, width, channels = img.shape
    return height, width, channels

def main():
    df = pd.read_csv("catsCsv")

    df.columns = ['Absolute Path', 'Relative Path']

    heights = []
    widths = []
    channels_list = []

    for index, row in df.iterrows():
        height, width, channels =  get_dementions(row['Absolute Path'])

        heights.append(height)
        widths.append(width)
        channels_list.append(channels)

    df['Height'] = heights
    df['Width'] = widths
    df['Channels'] = channels_list

    stats = df.describe()
    print(stats)

if __name__ == "__main__":
    main()