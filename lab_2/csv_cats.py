import csv
import os

from numpy.ma.core import absolute

def create_csv(path_to_images: str, path_to_csv: str) -> None:

    """
    A function that creates csv annotation of absolute and relative paths to images

    :param path_to_images: Path to images
    :param path_to_csv: Path to csv annotation
    """

    with open(path_to_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ['Absolute Path', 'Relative Path']
        writer.writerow(headers)

        for image in os.listdir(path_to_images):

            relative_path = os.path.join(path_to_images, image)
            absolute_path = os.path.abspath(relative_path)

            writer.writerow([absolute_path, relative_path])
