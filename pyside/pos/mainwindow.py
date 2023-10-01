# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_login import Ui_Dialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushLogin.clicked.connect(self.push_login_clicked)

    def push_login_clicked(self):
        login = Login(self)
        value = login.exec()
        print(value)


class Login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept_action)
        self.ui.buttonBox.rejected.connect(self.reject_action)

    def accept_action(self):
        print('accepted')

    def reject_action(self):
        print('rejected')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    widget.push_login_clicked()
    sys.exit(app.exec())
