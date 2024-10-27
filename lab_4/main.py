import argparse
import matplotlib.pyplot as plt
import pandas as pd

from dataFrame import *
from csv_annotation import *


def create_hist(df: pd.DataFrame) -> None:
    """
    A function that creates a histogram of image area distribution.

    :param df: DataFrame
    """

    plt.figure(figsize=(10,5))
    plt.hist(df['Area'])
    plt.title('Area distribution')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.show()


def parser_create() -> argparse.Namespace:
    """
    Parses the arguments from terminal

    :return: Namespace of arguments
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_csv', type=str, help='Path to csv file')
    return parser.parse_args()


def main():

    args = parser_create()

    create_csv(args.path_to_csv)
    df = pd.read_csv(args.path_to_csv)
    df.columns = ['Absolute Path', 'Relative Path']

    df = add_dementions(df)

    stats = df.describe()
    print(stats)

    df = create_filtered_df(stats['Height'].max(), stats['Width'].max())

    df = get_area(df)

    sorted_df = df.sort_values(by='Area', ascending=True)

    create_hist(sorted_df)


if __name__ == "__main__":
    main()
