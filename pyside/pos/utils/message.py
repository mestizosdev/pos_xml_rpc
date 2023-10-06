from PySide6.QtWidgets import QMessageBox


def error(parent, message: str):
    dialog = QMessageBox(parent)
    dialog.setWindowTitle("Error!!!")
    dialog.setText(message)
    dialog.setStandardButtons(QMessageBox.Ok)
    dialog.setIcon(QMessageBox.Critical)
    return dialog


def warning(parent, message: str):
    dialog = QMessageBox(parent)
    dialog.setWindowTitle("Warning!!!")
    dialog.setText(message)
    dialog.setStandardButtons(QMessageBox.Ok)
    dialog.setIcon(QMessageBox.Warning)
    return dialog
