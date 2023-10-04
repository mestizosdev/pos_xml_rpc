import os
from xmlrpc import client

from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QCloseEvent

from views.ui_point_of_sale import Ui_PosWindow


class PontOfSale(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PosWindow()
        self.ui.setupUi(self)
        self.ui.pushAdd.clicked.connect(self.add_row)
        self.ui.tableDetail.insertRow(0)
        self.ui.tableDetail.itemChanged.connect(self.changed)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()

    def add_row(self):
        row_position = self.ui.tableDetail.rowCount()
        self.ui.tableDetail.insertRow(row_position)
        print('Add row')
        server = os.getenv('SERVER')
        db = os.getenv('DB')
        uid = os.getenv('UID')
        password = os.getenv('PASSWORD')
        self.get_product(server, db, uid, password)

    def changed(self):
        print('item Changed')

    def get_product(self, server, db, uid, password):
        api = client.ServerProxy('%s/xmlrpc/2/object' % server)
        companies = (api
                     .execute_kw(db, uid, password,
                                 'product.product',
                                 'search_read',
                                 [[['barcode', '=', '5651234567866']]],
                                 {'limit': 1}))

        for c in companies:
            print(c)
            print(str(c['id']), c['name'])
