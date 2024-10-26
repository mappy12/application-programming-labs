import cv2
import pandas as pd

def get_dementions(path_to_image: str) -> tuple:

    img = cv2.imread(path_to_image)

    height, width, channels = img.shape
    return height, width, channels


def add_dementions(df: pd.DataFrame) -> pd.DataFrame:

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

    return df


def create_filtered_df(max_height: int, max_width: int) -> pd.DataFrame:
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

    filtered_df = df[(df['Height'] < max_height) & (df['Width'] < max_width)]

    return filtered_df


def get_area(df: pd.DataFrame) -> pd.DataFrame:

    df['Area'] = df['Height'] * df['Width']
    return df