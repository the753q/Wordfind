import sys
import WordSetupWindow
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout = QHBoxLayout()
        self.textArea = QTextEdit(str(8999999999**850))
        self.barCSS = (
            "QScrollBar::handle {border-radius:4px;background-color:#616161;width:8px;}" + 
            "QScrollBar::handle:hover {background-color:#bdbdbd;}" + 
            "QScrollBar::handle:pressed {background-color:white;}" + 
            "QScrollBar::add-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-page {background-color:rgba(0,0,0,0);}" + 
            "QScrollBar::sub-line {height:0;}" + 
            "QScrollBar::add-line {height:0;}" + 
            "QScrollBar {margin:8px 0 8px 0;width:8px;background-color:blue;}" + 
            "QWidget {background-color:rgba(0,0,0,0);}"
        )

        self.layout.addWidget(self.textArea)
        self.textArea.setStyleSheet(
            self.barCSS + 
            "QTextEdit {color:#e0e0e0;background-color:#212121;border-radius:16px;padding:2px;font-size:18px;max-width:700px;}"
        )
        
        self.sans = QFont("Segoe UI",69)
        self.textArea.setFont(self.sans)
        
        self.btnLayout = QVBoxLayout()
        self.openBtn = QPushButton("Open")
        self.setupBtn = QPushButton("Setup")
        self.findBtn = QPushButton("Find")
        self.btnLayout.addWidget(self.openBtn)
        self.btnLayout.addWidget(self.setupBtn)
        self.btnLayout.addWidget(self.findBtn)

        self.setupBtn.clicked.connect(self.WordOptionsShow)

        self.setStyleSheet(
            "QPushButton {margin-bottom:8px;min-height:52px;max-width:160px;color:#4fc3f7;background-color:#424242;border:3px solid #4fc3f7;border-radius:16px;font-size:35px;font-weight:bold;}" + 
            "QPushButton:hover {color:#212121;background-color:#4fc3f7;}" + 
            "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}"
        )
        
        self.status = QTextEdit()
        self.status.insertPlainText("Successfully loaded" + "\nOpen a file...")
        self.status.setReadOnly(1)
        self.status.setStyleSheet(
            self.barCSS + 
            "QTextEdit {color:#bdbdbd;background-color:#212121;padding:2px;border-radius:16px;font-size:14px;font-weight:bold;max-width:160px;max-height:100px;border-bottom:none;border-bottom-left-radius:0;border-bottom-right-radius:0;}"
        )

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

        self.setLayout(self.mainLayout)
        self.setGeometry(100, 100, 695, 385)
        self.widgetMargin = 6
        self.btnLayout.setContentsMargins(self.widgetMargin,0,0,0)
        self.setContentsMargins(self.widgetMargin,self.widgetMargin,self.widgetMargin,self.widgetMargin)
        self.setWindowTitle("Wordfind")

    def WordOptionsShow(self):
        self.WordOptions = WordSetupWindow.WordOptions()
        self.WordOptions.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("icon.png"))
    app.setStyleSheet("QWidget {background-color:#424242;}" + "QTextEdit {border: 3px solid #181818;}")
    app.setFont(QFont("Trebuchet MS"))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())