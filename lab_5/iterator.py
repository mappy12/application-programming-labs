import csv

class CatsIterator:

    """
    Custom image iterator class
    This iterator iterates over absolute and relative paths to cat images.
    """

    def __init__(self, path_to_csv: str):
        self.path_to_csv = path_to_csv

    def __iter__(self):

        self.image_paths = open(self.path_to_csv)
        self.csvreader = csv.reader(self.image_paths)

        return self

    def __next__(self):

        try:
            return self.csvreader.__next__()
        except StopIteration:
            self.image_paths.close()
            raise StopIteration
