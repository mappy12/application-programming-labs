import argparse

from cats import download_cats
from csv_cats import create_csv

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_images', type=str, help='Path to save images')
    parser.add_argument('path_to_csv', type=str, help='Path to csv')
    args = parser.parse_args()

    download_cats("cats", 10, args.path_to_images)
    create_csv(args.path_to_images, args.path_to_csv)

if __name__ == "__main__":
    main()
