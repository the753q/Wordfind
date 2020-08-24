import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont, QTextCharFormat, QTextCursor, QTextDocument, QCursor
from PyQt5.QtCore import Qt, QPoint, QObject
from PyQt5.QtWidgets import (
    QApplication, QFrame, QDesktopWidget, QWidget,
    QPushButton, QHBoxLayout, QVBoxLayout,
    QTextEdit, QLabel
)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        global wordSet
        wordSet = False

        self.layout = QHBoxLayout()
        self.textArea = QTextEdit(str(99**9**3) + " yes " + str(99**5**4))
        self.textFieldCSS = (
            "QScrollBar::handle {border-radius:4px;background-color:#555555;width:8px;}" + 
            "QScrollBar::handle:hover {background-color:#bdbdbd;}" + 
            "QScrollBar::handle:pressed {background-color:white;}" + 
            "QScrollBar::add-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-line {height:0;}" +
            "QScrollBar::add-line {height:0;}" +
            "QScrollBar {margin:8px 0 8px 0;width:8px;background-color:red;}" + 
            "QWidget {background-color:rgba(0,0,0,0);}" +
            "QTextEdit {color:#999;background-color:#212121;border-radius:16px;padding:2px;font-size:18px;max-width:700px;}"
        )
        self.btnStyle = (
            "QPushButton {margin-bottom:8px;min-height:52px;max-width:160px;color:#4fc3f7;background-color:#424242;border:3px solid #4fc3f7;border-radius:16px;font-size:35px;font-weight:bold;}" + 
            "QPushButton:hover {color:#212121;background-color:#4fc3f7;}" + 
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
        self.findBtn.setEnabled(0)

        self.btnLayout.addWidget(self.openBtn)
        self.btnLayout.addWidget(self.setupBtn)
        self.btnLayout.addWidget(self.findBtn)

        self.setupBtn.clicked.connect(self.WordOptionsShow)
        self.findBtn.clicked.connect(self.handleFind)
        
        self.status = QTextEdit()
        self.status.insertPlainText("Successfully loaded." + "\nOpen a file...")
        self.status.setReadOnly(1)
        self.status.setTextInteractionFlags(Qt.NoTextInteraction)
        self.status.setStyleSheet(
            self.textFieldCSS +
            "QTextEdit {color:#bdbdbd;font-size:14px;font-weight:bold;max-width:160px;max-height:100px;border-bottom:none;border-bottom-left-radius:0;border-bottom-right-radius:0;}"
        )
        self.status.viewport().setCursor(Qt.ArrowCursor)

        self.controlLayout = QVBoxLayout()
        self.controlLayout.addWidget(self.status)

        self.statusBtnLayout = QHBoxLayout()
        self.prevBtn = QPushButton("Previous")
        self.nextBtn = QPushButton("Next")
        self.cntrlBtnDesign = ("QPushButton {margin-bottom:0;min-height:26px;color:#757575;font-size:14px;background-color:#212121;border:3px solid #181818;border-top:3px solid gray;border-radius: 4px 10px 4px 4px;border-radius:0;border-bottom-left-radius:16px;border-bottom-right-radius:16px;}")
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

    def WordOptionsShow(self):
        self.WSetup = WordOptions()
        self.WSetup.show()
        print("wordSet value: " + str(wordSet))
        if wordSet:
            self.updateStatusText(str("Word to find set:" + word))
            print("word set")

    def handleFind(self):
        self.updateStatusText("\nGrabbed word: " + word + ".")
        #text = Wordfinding.WordOptions()
        if not word:
            return
        fmt = QTextCharFormat()
        fmt.setForeground(Qt.yellow)
        print("\nfmt.setForeground(Qt.red)", Qt.yellow)    

        self.textArea.moveCursor(QTextCursor.Start)

        while self.textArea.find(word, QTextDocument.FindWholeWords):
            self.mergeFormatOnWordOrSelection(fmt)

    def mergeFormatOnWordOrSelection(self, format):
        cursor = self.textArea.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.textArea.mergeCurrentCharFormat(format)

    def updateStatusText(self, message):
        self.status.insertPlainText(message)
        self.status.verticalScrollBar().setValue(self.status.verticalScrollBar().maximum())

    def returnWord():
        self.updateStatusText(word)


class WordOptions(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        self.layout.addWidget(self.label)
    
        #self.setGeometry(150, 150, 595, 285)
        self.setFixedSize(595,285)
        self.setWindowTitle("Wordfind - Setup Word Finding")
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.confirmWord)
        #self.confirmBtn.setStyleSheet(self.btnStyle)
        self.layout.addWidget(self.confirmBtn)

        self.setLayout(self.layout)

    def confirmWord(self):
        global word
        word = "yes"
        print("wordSet to True")
        global wordSet
        wordSet = True
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    app.setStyleSheet(
        "QWidget {background-color:#424242;}" +
        "QTextEdit {border: 3px solid #181818;}"
    )
    app.setFont(QFont("Trebuchet MS"))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())