import sys

#importing summarized data
from Summarize import getData
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QListWidgetItem, QFormLayout, QMainWindow
from PyQt5.QtWidgets import QListWidget, QLabel, QGridLayout, QVBoxLayout, QScrollArea, QGroupBox, QPlainTextEdit
from functools import partial

class Window(QMainWindow):

    def __init__(self, data, parent = None):
        super().__init__()
        self.title = "Pocket Summarizer"
        self.width = 500
        self.height = 500
        self.top = 325
        self.left = 450
        self.testUI(data)

    def testUI(self, data):

        self.setGeometry(self.left, self.top, self.width, self.height)
        textArea = QPlainTextEdit(self)
        textArea.insertPlainText(data)
        textArea.setReadOnly(True)
        textArea.resize(480, 480)
        textArea.move(10, 10)


class App(QWidget):

    def __init__(self):

        super().__init__()
        self.title = "Pocket Summarizer"
        self.width = 500
        self.height = 450
        self.top = 325
        self.left = 450
        self.wind = None
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        Data = getData()
        summarizedArticles = Data[0]
        title = Data[1]
        scrollArea = QScrollArea()
        formLayout = QFormLayout()
        grid = QGridLayout()
        groupBox = QGroupBox()
        
        for i in range(len(titles)):

            label = QLabel(title[i], self)
            label.move(9, 20 + (i * 30))
            label.setWordWrap(True)

            button = QPushButton("Read Summary", self)
            button.move(275, 20 + (i * 30))
            button.setToolTip("Read the summary")
            button.clicked.connect(partial(self.new_window, summarizedArticles[i]))#Calling functions with parameters, new window will be opened for reading summary

            formLayout.addRow(label, button)

        groupBox.setLayout(formLayout)
        scrollArea.setWidget(groupBox)
        layout = QVBoxLayout(self)
        layout.addWidget(scrollArea)

        self.show()

    def new_window(self, data):

        self.wind = Window(data)
        self.wind.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
