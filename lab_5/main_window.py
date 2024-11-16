import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer")


    def add_label(self):
        self.new_text.setText("Привет!")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

def main():
    application()

if __name__ == "__main__":
    main()