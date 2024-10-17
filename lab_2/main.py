import argparse

from cats import download_cats
from csv_cats import create_csv

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_images', type=str, help='Path to save images')
    parser.add_argument('path_to_csv', type=str, help='Path to csv')
    parser.add_argument('keyword', type=str, help="Search word")
    parser.add_argument('number_of_images', type=int, help="Number of downloaded images")
    args = parser.parse_args()

    download_cats(args.keyword, args.number_of_images, args.path_to_images)
    create_csv(args.path_to_images, args.path_to_csv)

if __name__ == "__main__":
    main()
