import cv2
import pandas as pd


def load_dataframe(path_to_csv: str) -> pd.DataFrame:
    """
    Loads data from a csv file into a DataFrame.

    :param path_to_csv: Path to csv-file
    :return: Loaded DataFrame
    """

    df = pd.read_csv(path_to_csv)
    df.columns = ['Absolute_Path', 'Relative_Path']

    return df

def get_dementions(path_to_image: str) -> tuple:
    """
    Function to get the dimensions of each image.

    :param path_to_image: Path to image
    :return: A tuple for each image consisting of its height, width and number of channels.
    """


    img = cv2.imread(path_to_image)

    if img is None:
        raise FileNotFoundError(f"Image not found or cannot be opened: {path_to_image}")

    height, width, channels = img.shape
    return height, width, channels


def add_dementions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function to add dimensions of each image to DataFrame.

    :param df: Source DataFrame
    :return: Updated DataFrame
    """

    heights = []
    widths = []
    channels_list = []

    for index, row in df.iterrows():
        height, width, channels =  get_dementions(row['Absolute_Path'])

        heights.append(height)
        widths.append(width)
        channels_list.append(channels)

    df['Height'] = heights
    df['Width'] = widths
    df['Channels'] = channels_list

    return df


def create_filtered_df(df: pd.DataFrame, max_height: int, max_width: int) -> pd.DataFrame:
    """
    A function that filters a date frame by a given condition.
    (height <= max_height и width <= max_width)

    :param df: Source DataFrame
    :param max_height: Maximum height in source DataFrame
    :param max_width: Maximum width in source DataFrame
    :return: Filtered DataFrame
    """

    new_heights = []
    new_widths = []

    for index, row in df.iterrows():
        height, width, channels =  get_dementions(row['Absolute_Path'])

        new_heights.append(height)
        new_widths.append(width)

    df['Height'] = new_heights
    df['Width'] = new_widths

    filtered_df = df[(df['Height'] < max_height) & (df['Width'] < max_width)]

    return filtered_df


def get_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Function for getting the area of the dimensions of each image.

    :param df: Source DataFrame
    :return: Updated DataFrame
    """

    df['Area'] = df['Height'] * df['Width']
    return df