from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFrame, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class WordOptions(QWidget):
    def __init__(self, mainWindow=None):
        super().__init__()
        self.mainWindow = mainWindow
        self.setFixedSize(645, 335)
        self.setWindowTitle("WordFind - Setup Word Finding")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.layoutMain = QVBoxLayout()
        self.layoutWords = QVBoxLayout()
        self.wordsBg = QFrame(self)
        self.wordsBg.setStyleSheet(
            "QFrame {background-color:#333;min-width:645px;min-height:90px;border-bottom:2px solid yellow;}")
        self.layoutButtons = QHBoxLayout(self.wordsBg)

        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self._confirm_word)
        self.confirmBtn.setStyleSheet(
            "QPushButton {color:#e9a81d;background-color:#484848;border:3px solid #e9a81d;border-radius:16px;font-size:35px;font-weight:bold;min-width:160px;min-height:52px;}" +
            "QPushButton:hover {color:black;background-color:#e9a81d;}" +
            "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}"
        )
        self.layoutButtons.addWidget(self.confirmBtn, alignment=Qt.AlignmentFlag.AlignRight)

        # self.layoutLetters1 = QHBoxLayout()
        # self.frameLetter = QFrame(self)
        # self.frameLetter.setStyleSheet("QFrame {min-height:150px;background-color:red;border: 3px solid green;border-radius:8px;}")
        # self.layoutLetter = QVBoxLayout()#self.frameLetter)
        # self.layoutLetters1.addLayout(self.layoutLetter)
        # self.layoutWords.addLayout(self.layoutLetters1)

        # self.layoutMain.addLayout(self.layoutWords)
        # self.layoutMain.addLayout(self.layoutButtons)

        self.layoutMain.addWidget(self.wordsBg)
        self.setLayout(self.layoutMain)
        # self.setStyleSheet("{background-color:#212121;}")

    def _confirm_word(self):
        self.mainWindow.confirm_close("yes")
        self.close()
