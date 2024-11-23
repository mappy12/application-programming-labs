import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtGui import QPixmap

from iterator import CatsIterator


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")
        self.setFixedSize(QSize(1280,700))
        self.move(100,100)

        self.setup_main_window()

        self.csv_path = None
        self.cats_iterator = None
        self.image_iterator = None


    def setup_main_window(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding
        )
        self.label.setStyleSheet("background-color: #424242; border: 2px solid #adaaaa; border-radius: 5px")

        self.opencsv_button = QPushButton("Open csv-file")
        self.opencsv_button.clicked.connect(self.setup_file_dialog)
        self.opencsv_button.setFixedSize(1000, 50)
        self.opencsv_button.setStyleSheet("border: 2px solid #ababab; border-radius: 5px; background-color: #737373;")

        self.next_button = QPushButton("Next image")
        self.next_button.clicked.connect(self.show_next_image)
        self.next_button.setEnabled(False)
        self.next_button.setFixedSize(1000, 50)
        self.next_button.setStyleSheet("border: 2px solid #ababab; border-radius: 5px; background-color: #737373;")

        layout.addWidget(self.label)
        layout.addWidget(self.next_button, alignment=Qt.AlignHCenter)
        layout.addWidget(self.opencsv_button, alignment=Qt.AlignHCenter)

    def setup_file_dialog(self):
        csv_path, _ = QFileDialog.getOpenFileName(self, "Select CSV-file", "", "CSV file (*.csv)")
        if csv_path:
            self.csv_path = csv_path
            self.image_iterator = iter(CatsIterator(self.csv_path))
            self.show_next_image()

            self.next_button.setEnabled(True)
            self.opencsv_button.setEnabled(False)


    def show_next_image(self):
        try:
           image = next(self.image_iterator)
           self.current_image = image[0]
           self.display_image(self.current_image)
        except StopIteration:
            self.label.setText("No more images")
            self.next_button.setEnabled(False)

    def display_image(self, image):
        try:
            pixmap = QPixmap(image)

            if pixmap.isNull():
                print("Invalid image file")

            self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio))
        except Exception as e:
            print(f"Error loading image: {e}")


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

def main():
    application()

if __name__ == "__main__":
    main()