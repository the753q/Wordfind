import re
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCharFormat, QColor, QTextCursor
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
from constants import styles
from core import options_window, utilities


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        setup_button = QPushButton("Setup")
        setup_button.setCursor(Qt.CursorShape.PointingHandCursor)
        setup_button.clicked.connect(self._show_options_window)

        self.status = QTextEdit()
        self.status.insertPlainText("Paste text...")
        self.status.setReadOnly(True)
        self.status.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)
        self.status.setStyleSheet(styles.STATUS)
        self.status.viewport().setCursor(Qt.CursorShape.ArrowCursor)

        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self._go_to_previous_match)
        utilities.toggle_previous_button(self.previous_button, False)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self._go_to_next_match)
        utilities.toggle_next_button(self.next_button, False)

        status_buttons_layout = QHBoxLayout()
        status_buttons_layout.addWidget(self.previous_button)
        status_buttons_layout.addWidget(self.next_button)
        status_buttons_layout.setSpacing(0)
        status_buttons_layout.setContentsMargins(0, 0, 0, 0)

        status_buttons_panel = QWidget()
        status_buttons_panel.setLayout(status_buttons_layout)

        control_layout = QVBoxLayout()
        control_layout.addWidget(self.status)
        control_layout.addWidget(status_buttons_panel)
        control_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        control_layout.setSpacing(0)
        control_layout.setContentsMargins(0, 0, 0, 0)

        control_panel = QWidget()
        control_panel.setLayout(control_layout)

        button_layout = QVBoxLayout()
        button_layout.addWidget(setup_button)
        button_layout.addStretch()
        button_layout.addWidget(control_panel)
        button_layout.setContentsMargins(styles.WIDGET_MARGIN, 0, 0, 0)

        button_panel = QWidget()
        button_panel.setLayout(button_layout)
        button_panel.setMaximumHeight(styles.MINIMUM_SIZE.height())

        self.text_area = QTextEdit(str(99 ** 9 ** 3) + " yes " + str(99 ** 5 ** 4) + "yes" +
                                   "Sample text for testing: yes, yos, y_s, y s, and not yz s."
                           "y&s? Also YEs46  yess ")
        self.text_area.setStyleSheet(styles.TEXT_FIELD)

        main_layout = QHBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.text_area, stretch=1)
        main_layout.addWidget(button_panel)

        self.setLayout(main_layout)
        self.setStyleSheet(styles.BUTTON)
        self.setMinimumSize(styles.MINIMUM_SIZE)
        self.resize(styles.MINIMUM_SIZE)
        self.setContentsMargins(styles.WIDGET_MARGIN, styles.WIDGET_MARGIN, styles.WIDGET_MARGIN, styles.WIDGET_MARGIN)
        self.setWindowTitle("WordFind")

        self.setup_window = options_window.WordOptions(self)

        self.search_term = "yes"
        self.search_results = []
        self.current_match_index = -1

        self.show()

    def _show_options_window(self):
        self.setup_window.show()

    def _clear_highlights(self):
        self.text_area.moveCursor(QTextCursor.MoveOperation.Start)
        current_text = self.text_area.toPlainText()
        self.text_area.setPlainText(current_text)
        self.text_area.moveCursor(QTextCursor.MoveOperation.Start)
        self.text_area.ensureCursorVisible()

    def _find_word(self):
        utilities.toggle_next_button(self.next_button, False)
        utilities.toggle_previous_button(self.previous_button, False)
        self._clear_highlights()
        self.search_results = []
        self.current_match_index = -1

        highlight_format = QTextCharFormat()
        highlight_format.setForeground(QColor("#e9a81d"))

        escaped_search_term = re.escape(self.search_term)
        pattern_str = escaped_search_term.replace("_", ".")
        regex = re.compile(pattern_str)

        text_content = self.text_area.toPlainText()
        num_found = 0
        for match in regex.finditer(text_content):
            start_pos = match.start()
            self.search_results.append(start_pos)
            num_found += 1

        temp_cursor = self.text_area.textCursor()
        for start_pos in self.search_results:
            temp_cursor.setPosition(start_pos)
            temp_cursor.setPosition(start_pos + len(self.search_term), QTextCursor.MoveMode.KeepAnchor)
            temp_cursor.mergeCharFormat(highlight_format)

        self._update_status_text(f"Found {num_found} instance(s) of '{self.search_term}'.")

        if self.search_results:
            final_cursor_pos = self.text_area.textCursor().selectionEnd()
            temp_cursor.clearSelection()
            temp_cursor.setPosition(final_cursor_pos)
            self.text_area.setTextCursor(temp_cursor)

            self.current_match_index = 0
            self._go_to_match(self.current_match_index)
            utilities.toggle_next_button(self.next_button, True)
            utilities.toggle_previous_button(self.previous_button, True)
        else:
            self.text_area.moveCursor(QTextCursor.MoveOperation.Start)

        self.text_area.ensureCursorVisible()

    def _go_to_match(self, index):
        start_pos = self.search_results[index]
        word_len = len(self.search_term)

        cursor = self.text_area.textCursor()
        cursor.setPosition(start_pos)
        cursor.setPosition(start_pos + word_len, QTextCursor.MoveMode.KeepAnchor)

        self.text_area.setTextCursor(cursor)
        self.text_area.ensureCursorVisible()

    def _go_to_next_match(self):
        self.current_match_index += 1
        if self.current_match_index >= len(self.search_results):
            self.current_match_index = 0

        self._go_to_match(self.current_match_index)

    def _go_to_previous_match(self):
        self.current_match_index -= 1
        if self.current_match_index < 0:
            self.current_match_index = len(self.search_results) - 1

        self._go_to_match(self.current_match_index)

    def _update_status_text(self, message):
        self.status.insertPlainText("\n" + message)
        self.status.ensureCursorVisible()

    def confirm_close(self, word_shell):
        self.search_term = word_shell
        self._find_word()
