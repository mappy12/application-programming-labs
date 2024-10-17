import csv

class CatsIterator:

    def __init__(self, path_to_csv: str):
        self.path_to_csv = path_to_csv

    def __iter__(self):

        self.image_paths = open(self.path_to_csv)
        self.csvreader = csv.reader(self.image_paths)

        return self

    def __next__(self):

        try:
            self.csvreader.__next__()
        except StopIteration:
            self.image_paths.close()
            raise StopIteration
