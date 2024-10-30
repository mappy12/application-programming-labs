import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("LAB 5")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Мой графический интерфейс")
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(0, 25)
        self.btn.setText("Добавить")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_label)

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