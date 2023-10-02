import sys
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    while widget.is_not_login:
        widget.try_login()
    sys.exit(app.exec())
