from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class WordOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        self.layout.addWidget(self.label)
    
        self.setGeometry(150, 150, 595, 285)
        self.setWindowTitle("Wordfind - Setup Word Finding")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.confirmWord)
        self.layout.addWidget(self.confirmBtn)

        self.setLayout(self.layout)


    def confirmWord(self):
        print("Word to find confirmed")
        return(str("yes"))