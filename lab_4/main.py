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
    parser.add_argument('max_height', type=int, help='Maximum image height')
    parser.add_argument('max_width', type=int, help='Maximum image width')
    return parser.parse_args()


def main():

    try:
        args = parser_create()

        create_csv(args.path_to_csv)
        df = load_dataframe(args.path_to_csv)

        df = add_dementions(df)

        stats = df.describe()
        print(stats)

        df = create_filtered_df(args.path_to_csv,args.max_height, args.max_width)

        df = get_area(df)

        sorted_df = df.sort_values(by='Area', ascending=True)

        create_hist(sorted_df)

    except Exception as e:
        print(f"An unexpected error occurred in the main function: {e}")


if __name__ == "__main__":
    main()
