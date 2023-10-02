from PySide6.QtWidgets import QMessageBox


def error(message):
    dialog = QMessageBox()
    dialog.setWindowTitle("Error!!!")
    dialog.setText(message)
    dialog.setStandardButtons(QMessageBox.Ok)
    dialog.setIcon(QMessageBox.Critical)
    dialog.exec()
