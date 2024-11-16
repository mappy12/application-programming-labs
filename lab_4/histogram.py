import matplotlib.pyplot as plt
import pandas as pd


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