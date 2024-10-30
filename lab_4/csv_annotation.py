import csv
import os


def create_csv(path_to_csv: str) -> None:

    """
    A function that creates csv annotation of absolute and relative paths to images.
    This is necessary in order to get the paths on each computer again.

    :param path_to_csv: Path to csv annotation
    """

    if not os.path.exists('catsImg'):
        print("Error: Directory 'catsImg' does not exist. Please create it and add images.")
        exit(1)

    with open(path_to_csv, 'w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        for image in os.listdir('catsImg'):

            relative_path = os.path.join('catsImg', image)
            absolute_path = os.path.abspath(relative_path)

            writer.writerow([absolute_path, relative_path])
