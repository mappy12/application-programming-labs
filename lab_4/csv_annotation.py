import csv
import os


def create_csv(path_to_csv: str, path_to_images: str) -> None:

    """
    A function that creates csv annotation of absolute and relative paths to images.
    This is necessary in order to get the paths on each computer again.

    :param path_to_csv: Path to csv annotation
    :param path_to_images: Path to images dir
    """

    if not os.path.exists(path_to_images):
        raise FileNotFoundError

    with open(path_to_csv, 'w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        for image in os.listdir(path_to_images):

            relative_path = os.path.join(path_to_images, image)
            absolute_path = os.path.abspath(relative_path)

            writer.writerow([absolute_path, relative_path])
