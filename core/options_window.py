from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QTextEdit, QLineEdit, QVBoxLayout
from constants import styles


class WordOptions(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window

        self.word_area = QLineEdit("y_s")
        self.word_area.setStyleSheet(styles.WORD_AREA)
        self.word_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_area.textChanged.connect(self._on_word_area_text_changed)

        find_button = QPushButton("Find")
        find_button.setCursor(Qt.CursorShape.PointingHandCursor)
        find_button.clicked.connect(self._confirm_word)

        main_layout = QVBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.word_area)
        main_layout.addStretch()
        main_layout.addWidget(find_button, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(main_layout)
        self.setStyleSheet(styles.FIND_BUTTON)
        self.setContentsMargins(styles.WIDGET_MARGIN, styles.WIDGET_MARGIN, styles.WIDGET_MARGIN, styles.WIDGET_MARGIN)
        self.setFixedSize(645, 335)
        self.setWindowTitle("Setup Word to Find")
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

    def _on_word_area_text_changed(self):
        current_text = self.word_area.text()

        new_text_parts = []
        made_change = False
        for char in current_text:
            if char.isspace():
                new_text_parts.append("_")
                made_change = True
            elif char.isalnum():
                upper_char = char.upper()
                new_text_parts.append(upper_char)
                if char != upper_char: made_change = True
            else:
                made_change = True

        new_text = "".join(new_text_parts)

        if new_text != current_text or made_change:
            self.word_area.blockSignals(True)
            self.word_area.setText(new_text)
            self.word_area.blockSignals(False)

    def keyPressEvent(self, event):
        if self.word_area.hasFocus() and \
                (event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter):
            self._confirm_word()
            event.accept()
            return
        super().keyPressEvent(event)

    def _confirm_word(self):
        self.close()
        self.main_window.confirm_close(self.word_area.text())
