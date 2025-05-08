from PySide6.QtWidgets import QPushButton

from constants import styles


def toggle_previous_button(button: QPushButton, status: bool):
    button.setEnabled(status)
    style = styles.PREVIOUS_BUTTON if status else styles.PREVIOUS_BUTTON_DISABLED
    button.setStyleSheet(style)


def toggle_next_button(button: QPushButton, status: bool):
    button.setEnabled(status)
    style = styles.NEXT_BUTTON if status else styles.NEXT_BUTTON_DISABLED
    button.setStyleSheet(style)
