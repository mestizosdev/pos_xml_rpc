# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtWidgets import QMainWindow
from xmlrpc import client
from dotenv_vault import load_dotenv
from utils import message

load_dotenv()
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from login import Login
from views.point_of_sale import PontOfSale


class MainWindow(QMainWindow):
    is_not_login = True
    common = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.pushConnect.clicked.connect(self.test_odoo_server)
        self.ui.actionPoint_of_Sale.triggered.connect(self.open_pos)
        server = os.getenv('SERVER')
        try:
            self.common = client.ServerProxy("%s/xmlrpc/2/common" % server)
            print(self.common.version())
        except ConnectionError:
            message.error(f'Error connect to {server}')
            sys.exit()

    def try_login(self):
        login = Login(self)
        value = login.exec()
        if value == 1:
            if login.username == '' or login.password == '':
                self.is_not_login = True
                return
            else:
                uid = self.common.authenticate(os.getenv('DB'), login.username, login.password, {})
                if not uid:
                    self.is_not_login = True
                    return
                server = os.getenv('SERVER')
                self.ui.statusbar.showMessage(f'Connected to {server} with {login.username}', 6000)
        else:
            self.close()
            sys.exit()

        self.is_not_login = False

    def close_app(self):
        self.close()

    def open_pos(self):
        pos = PontOfSale(self)
        pos.show()
        self.hide()
