import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setFixedSize(QSize(1280,700))
        self.move(100,100)

        self.setup_main_window()

        self.csv_path = None

    def setup_main_window(self):
        opencsv_button = QPushButton("Open csv-file")
        opencsv_button.clicked.connect(self.setup_file_dialog)

        self.setCentralWidget(opencsv_button)
        opencsv_button.setFixedSize(200,50)

    def setup_file_dialog(self):
        csv_path, _ = QFileDialog.getOpenFileName(self, "Select CSV-file", "", "CSV file (*.csv)")
        if csv_path:
            self.csv_path = csv_path


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

def main():
    application()

if __name__ == "__main__":
    main()