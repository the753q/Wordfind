from PySide6.QtCore import QSize

APP = (
        "QWidget {background-color:#333;}" +
        "QTextEdit {border: 3px solid #181818;}" +
        "QLineEdit {border: 3px solid #181818;}"
)
TEXT_FIELD = (
        "QScrollBar::handle {border-radius:4px;background-color:#444;width:8px;}" +
        "QScrollBar::handle:hover {background-color:#bbb;}" +
        "QScrollBar::handle:pressed {background-color:white;}" +
        "QScrollBar::add-page {background-color:rgba(0,0,0,0);}" +
        "QScrollBar::sub-page {background-color:rgba(0,0,0,0);}" +
        "QScrollBar::sub-line {height:0;}" +
        "QScrollBar::add-line {height:0;}" +
        "QScrollBar {margin:8px 0 8px 0;width:8px;background-color:red;}" +
        "QWidget {background-color:rgba(0,0,0,0);}" +
        "QTextEdit {" +
        "color:#aaa;background-color:#212121;border-radius:16px;padding:2px;font-size:18px;max-width:700px;}"
)
_BUTTON_PRESSED = "QPushButton:pressed {color:white;background-color:#212121;border-color:white;}"
BUTTON = (
        "QPushButton {" +
        "color:#1de9b6;background-color:#484848;margin-bottom:4px;min-height:52px;" +
        "max-width:160px;border:3px solid #1de9b6;border-radius:16px;font-size:35px;font-weight:bold;}" +
        "QPushButton:hover {color:#212121;background-color:#1de9b6;}" +
        _BUTTON_PRESSED
)
BUTTON_DISABLED = "QPushButton {color:#555555;border-color:#555555;background-color:#383838}"
FIND_BUTTON = (
        BUTTON +
        "QPushButton {color:#e9a81d;background-color:#484848;border-color:#e9a81d; width:160px;}" +
        "QPushButton:hover {background-color:#e9a81d;}" +
        _BUTTON_PRESSED
)
WORD_AREA = (
        "QLineEdit {color:#aaa;background-color:#212121;border-radius:16px;padding:2px;font-size:35px;" +
        "font-weight:bold;letter-spacing:4px;max-height:52px;}"
)
STATUS = (
        TEXT_FIELD +
        "QTextEdit {color:#bdbdbd;font-size:14px;font-weight:bold;max-width:160px;max-height:100px;" +
        "border-bottom:none;border-bottom-left-radius:0;border-bottom-right-radius:0;}"
)
_STATUS_BUTTON = (
        "QPushButton {margin:0;min-height:26px;color:#757575;font-size:14px;background-color:#212121;" +
        "border:3px solid #181818;border-top:3px solid gray;border-radius: 4px 10px 4px 4px;border-radius:0;" +
        "border-bottom-left-radius:16px;border-bottom-right-radius:16px;}"
)
_STATUS_BUTTON_ENABLED = (
        "QPushButton:hover {color:white;background-color:black;}" +
        "QPushButton:pressed {color:black;background-color:white;}" +
        "QPushButton {color:#f5f5f5;}"
)
_PREVIOUS_BUTTON = "QPushButton {border-bottom-right-radius:0;border-right:1px solid gray;}"
PREVIOUS_BUTTON = (
        _STATUS_BUTTON +
        _STATUS_BUTTON_ENABLED +
        _PREVIOUS_BUTTON
)
PREVIOUS_BUTTON_DISABLED = (
        _STATUS_BUTTON +
        _PREVIOUS_BUTTON
)
_NEXT_BUTTON = "QPushButton {border-bottom-left-radius:0;border-left:2px solid gray;}"
NEXT_BUTTON = (
        _STATUS_BUTTON +
        _STATUS_BUTTON_ENABLED +
        _NEXT_BUTTON
)
NEXT_BUTTON_DISABLED = (
        _STATUS_BUTTON +
        _NEXT_BUTTON
)
MINIMUM_SIZE = QSize(695, 385)
WIDGET_MARGIN = 6
