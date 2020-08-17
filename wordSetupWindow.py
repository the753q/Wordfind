from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel

class WordOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.setGeometry(150, 150, 595, 285)
        self.setWindowTitle("Wordfind - Setup Word Finding")
        self.setWindowModality(QtCore.Qt.ApplicationModal)