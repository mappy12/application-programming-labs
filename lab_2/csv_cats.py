import csv
import os

def create_csv(path_to_images: str, path_to_csv: str) -> None:

    with open('path_to_csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        headers = ['Absolute Path', 'Relative Path']
        writer.writerow(headers)

    for image in os.listdir(path_to_images):
        relative_path = os.path.relpath(path_to_images, start=im
