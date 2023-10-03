import os
from xmlrpc import client
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QCloseEvent

from views.ui_company import Ui_CompanyWindow


class Company(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompanyWindow()
        self.ui.setupUi(self)
        server = os.getenv('SERVER')
        db = os.getenv('DB')
        uid = os.getenv('UID')
        password = os.getenv('PASSWORD')
        self.get_companies(server, db, uid, password)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()

    def get_companies(self, server, db, uid, password):
        api = client.ServerProxy('%s/xmlrpc/2/object' % server)
        companies = api.execute_kw(db, uid, password,
                                   'res.company',
                                   'search_read',
                                   [[]],
                                   {'fields': ['id', 'name'], 'limit': 10})

        for c in companies:
            print(c)
            print('-', c['id'], c['name'])
