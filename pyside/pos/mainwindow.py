# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from login import Login


class MainWindow(QMainWindow):
    is_not_login = True

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushLogin.clicked.connect(self.push_login_clicked)

    def push_login_clicked(self):
        login = Login(self)
        value = login.exec()
        if value == 1:
            print(login.username)
            print(login.password)
            if login.username == '':
                login.exec()
                self.is_not_login = True
                return

        self.is_not_login = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    while widget.is_not_login:
        if widget.is_not_login == True:
            widget.push_login_clicked()
    sys.exit(app.exec())
