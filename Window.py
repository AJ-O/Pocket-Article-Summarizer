import sys

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QListWidgetItem, QFormLayout
from PyQt5.QtWidgets import QListWidget, QLabel, QGridLayout, QVBoxLayout, QScrollArea, QGroupBox

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.title = "Article"
        self.top = 300
        self.left = 300
        self.height = 500
        self.width = 500

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel("test")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
