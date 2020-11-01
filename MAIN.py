import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont, QTextCharFormat, QColor, QTextCursor, QTextDocument, QCursor
from PyQt5.QtCore import Qt, QPoint, QObject
from PyQt5.QtWidgets import (
    QApplication, QFrame, QDesktopWidget, QWidget,
    QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QHBoxLayout()
        self.textArea = QTextEdit(str(99**9**3) + " yes " + str(99**5**4))
        self.textFieldCSS = (
            "QScrollBar::handle {border-radius:4px;background-color:#444;width:8px;}" + 
            "QScrollBar::handle:hover {background-color:#bbb;}" + 
            "QScrollBar::handle:pressed {background-color:white;}" + 
            "QScrollBar::add-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-line {height:0;}" +
            "QScrollBar::add-line {height:0;}" +
            "QScrollBar {margin:8px 0 8px 0;width:8px;background-color:red;}" + 
            "QWidget {background-color:rgba(0,0,0,0);}" +
            "QTextEdit {color:#aaa;background-color:#212121;border-radius:16px;padding:2px;font-size:18px;max-width:700px;}"
        )
        self.btnStyle = (
            "QPushButton {color:#1de9b6;background-color:#484848;margin-top:4px;margin-bottom:4px;min-height:52px;max-width:160px;border:3px solid #1de9b6;border-radius:16px;font-size:35px;font-weight:bold;}" + 
            "QPushButton:hover {color:#212121;background-color:#1de9b6;}" + 
            "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}"
        )
        self.layout.addWidget(self.textArea)
        self.textArea.setStyleSheet(self.textFieldCSS)
        
        self.sans = QFont("Segoe UI",69)
        self.textArea.setFont(self.sans)
        
        self.btnLayout = QVBoxLayout()
        self.openBtn = QPushButton("Open")
        self.setupBtn = QPushButton("Setup")
        self.findBtn = QPushButton("Find")

        self.openBtn.setStyleSheet("QPushButton {margin-top:0;}")

        self.btnToggle(False, self.findBtn)

        self.btnLayout.addWidget(self.openBtn)
        self.btnLayout.addWidget(self.setupBtn)
        self.btnLayout.addWidget(self.findBtn)

        self.openBtn.setCursor(Qt.PointingHandCursor)
        self.setupBtn.setCursor(Qt.PointingHandCursor)
        self.findBtn.setCursor(Qt.PointingHandCursor)

        self.setupBtn.clicked.connect(self.wordOptionsShow)
        self.findBtn.clicked.connect(self.findWord)
        
        self.status = QTextEdit()
        self.status.insertPlainText("Open a file or paste text...")
        self.status.setReadOnly(1)
        self.status.setTextInteractionFlags(Qt.NoTextInteraction)
        self.status.setStyleSheet(
            self.textFieldCSS +
            "QTextEdit {margin-top:4px;color:#bdbdbd;font-size:14px;font-weight:bold;max-width:160px;max-height:100px;border-bottom:none;border-bottom-left-radius:0;border-bottom-right-radius:0;}"
        )
        self.status.viewport().setCursor(Qt.ArrowCursor)

        self.controlLayout = QVBoxLayout()
        self.controlLayout.addWidget(self.status)

        self.statusBtnLayout = QHBoxLayout()
        self.prevBtn = QPushButton("Previous")
        self.nextBtn = QPushButton("Next")
        self.cntrlBtnDesign = ("QPushButton {margin:0;min-height:26px;color:#757575;font-size:14px;background-color:#212121;border:3px solid #181818;border-top:3px solid gray;border-radius: 4px 10px 4px 4px;border-radius:0;border-bottom-left-radius:16px;border-bottom-right-radius:16px;}")
        self.prevBtn.setStyleSheet(self.cntrlBtnDesign + "QPushButton:hover {color:white;background-color:black;}" + "QPushButton:pressed {color:black;background-color:white;}" + "QPushButton {border-bottom-right-radius:0;border-right:1px solid gray;}")
        self.nextBtn.setStyleSheet(self.cntrlBtnDesign + "QPushButton:hover {color:white;background-color:black;}" + "QPushButton:pressed {color:black;background-color:white;}" + "QPushButton {color:#f5f5f5;border-bottom-left-radius:0;border-left:2px solid gray;}")
        self.statusBtnLayout.addWidget(self.prevBtn)
        self.statusBtnLayout.addWidget(self.nextBtn)
        self.controlLayout.setSpacing(0)
        self.controlLayout.addLayout(self.statusBtnLayout)
        self.btnLayout.addLayout(self.controlLayout)

        self.btnLayout.setAlignment(Qt.AlignTop)
        self.layout.addLayout(self.btnLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.layout)

        self.setStyleSheet(self.btnStyle)
        self.setLayout(self.mainLayout)
        self.resize(695, 385)
        self.setMinimumSize(695, 385)
        self.center()
        self.widgetMargin = 6
        self.btnLayout.setContentsMargins(self.widgetMargin,0,0,0)
        self.setContentsMargins(self.widgetMargin,self.widgetMargin,self.widgetMargin,self.widgetMargin)
        self.setWindowTitle("Wordfind")

    def center(self): #thx https://github.com/saleph
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def wordOptionsShow(self):
        self.WSetup = WordOptions(self)
        self.WSetup.show()

    def findWord(self):
        self.updateStatusText("Found " + "6" + " words.")
        fmt = QTextCharFormat()
        fmt.setForeground(QColor("#e9a81d")) 

        self.textArea.moveCursor(QTextCursor.Start)

        while self.textArea.find("yes", QTextDocument.FindWholeWords):
            self.mergeFormatOnWordOrSelection(fmt)

    def mergeFormatOnWordOrSelection(self, format):
        cursor = self.textArea.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.textArea.mergeCurrentCharFormat(format)

    def confirmClose(self, wordSet):
        self.updateStatusText("Word set: " + wordSet)
        self.btnToggle(True, self.findBtn)

    def updateStatusText(self, message):
        self.status.insertPlainText("\n" + message)
        self.status.verticalScrollBar().setValue(self.status.verticalScrollBar().maximum())

    def btnToggle(self, status, button):
        button.setEnabled(status)
        if status:
            button.setStyleSheet(self.btnStyle)
        else:
            button.setStyleSheet("QPushButton {color:#555555;border-color:#555555;background-color:#383838}")


class WordOptions(QWidget):
    def __init__(self, mainWindow = None):
        super(WordOptions, self).__init__()
        self.mainWindow = mainWindow
        #self.setGeometry(150, 150, 595, 285)
        self.setFixedSize(645,335)
        self.setWindowTitle("Wordfind - Setup Word Finding")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.layoutMain = QVBoxLayout()
        self.layoutWords = QVBoxLayout()
        self.wordsBg = QFrame(self)
        self.wordsBg.setStyleSheet("QFrame {background-color:#333;min-width:645px;min-height:90px;border-bottom:2px solid yellow;}")
        self.layoutButtons = QHBoxLayout(self.wordsBg)

        self.optionsBtnStyle = (
            "QPushButton {color:#e9a81d;background-color:#484848;border:3px solid #e9a81d;border-radius:16px;font-size:35px;font-weight:bold;min-width:160px;min-height:52px;}" + 
            "QPushButton:hover {color:black;background-color:#e9a81d;}" +
            "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}"
        )

        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.confirmWord)
        self.confirmBtn.setStyleSheet(self.optionsBtnStyle)
        self.layoutButtons.addWidget(self.confirmBtn, alignment=QtCore.Qt.AlignRight)
        #self.layoutLetters1 = QHBoxLayout()
        #self.frameLetter = QFrame(self)
        #self.frameLetter.setStyleSheet("QFrame {min-height:150px;background-color:red;border: 3px solid green;border-radius:8px;}")
        #self.layoutLetter = QVBoxLayout()#self.frameLetter)
        #self.layoutLetters1.addLayout(self.layoutLetter)
        #self.layoutWords.addLayout(self.layoutLetters1)

        #self.layoutMain.addLayout(self.layoutWords)
        #self.layoutMain.addLayout(self.layoutButtons)
        #self.setLayout(self.layoutMain)
        #self.setStyleSheet("{background-color:#212121;}")

    def confirmWord(self):
        self.mainWindow.confirmClose("yes")
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    app.setStyleSheet(
        "QWidget {background-color:#333;}" +
        "QTextEdit {border: 3px solid #181818;}"
    )
    app.setFont(QFont("Trebuchet MS"))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())