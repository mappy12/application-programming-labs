import argparse

from csv_cats import create_csv
from cats import download_cats
from iterator import CatsIterator

def parse_arguments():

    """
        Parses the keyword, path to images, path to csv from the terminal arguments.

        :return: The list of arguments
        """

    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help="Search word")
    parser.add_argument('path_to_images', type=str, help='Path to save images')
    parser.add_argument('path_to_csv', type=str, help='Path to csv')

    return parser.parse_args()

def main():

    args = parse_arguments()

    download_cats(args.keyword, 10, args.path_to_images)
    create_csv(args.path_to_images, args.path_to_csv)

    iterator = CatsIterator(args.path_to_csv)

    for cat in iterator:
        print(cat)

if __name__ == "__main__":
    main()
