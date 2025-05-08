import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from constants import styles
from core import main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    app.setStyleSheet(styles.APP)

    main_window.MainWindow()

    sys.exit(app.exec())
