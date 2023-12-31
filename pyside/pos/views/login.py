# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog

from views.ui_login import Ui_Dialog


class Login(QDialog):
    username = ''
    password = ''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accept_action)
        self.ui.buttonBox.rejected.connect(self.reject_action)
        self.ui.txtUsername.setFocus()
        self.ui.txtUsername.setText('admin')
        self.ui.txtPassword.setText('admin')

    def accept_action(self):
        self.username = self.ui.txtUsername.text()
        self.password = self.ui.txtPassword.text()

    def reject_action(self):
        self.username = ''
        self.password = ''
