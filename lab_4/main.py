import cv2
import numpy as np
import pandas as pd

def get_dementions(path_to_image: str):

    img = cv2.imread(path_to_image)

    height, width, channels = img.shape
    return height, width, channels

def create_new_df(max_height: int, max_width: int):
    df = pd.read_csv('catsCsv')

    df.columns = ['Absolute Path', 'Relative Path']

    new_heights = []
    new_widths = []

    for index, row in df.iterrows():
        height, width, channels =  get_dementions(row['Absolute Path'])

        new_heights.append(height)
        new_widths.append(width)

    df['Height'] = new_heights
    df['Width'] = new_widths

    print(df['Height'].max())

    filtered_df = df[(df['Height'] < max_height) & (df['Width'] < max_width)]

    return filtered_df

def get_area(df: pd.DataFrame) -> pd.DataFrame:

    df['Area'] = df['Height'] * df['Width']

    return df



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

    df = create_new_df(stats['Height'].max(), stats['Width'].max())

    df = get_area(df)

    sorted_df = df.sort_values(by='Area', ascending=True)



if __name__ == "__main__":
    main()