import argparse

from cats import download_cats

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_images', type=str, help='Path to save images')
    args = parser.parse_args()

    download_cats("cats", 10, args.path_to_images)

if __name__ == "__main__":
    main()
