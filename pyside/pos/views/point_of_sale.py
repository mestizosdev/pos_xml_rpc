from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QCloseEvent

from utils.client import Client
from views.ui_point_of_sale import Ui_PosWindow


class PontOfSale(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PosWindow()
        self.ui.setupUi(self)
        self.ui.pushAdd.clicked.connect(self.add_row)
        self.ui.pushRemove.clicked.connect(self.remove_row)
        # self.ui.tableDetail.insertRow(0)
        self.ui.tableDetail.itemChanged.connect(self.item_changed)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()

    def add_row(self):
        db, uid, password = Client.load()
        self.get_product(db, uid, password)

    def remove_row(self):
        row = self.ui.tableDetail.currentRow()
        self.ui.tableDetail.removeRow(row)

    def item_changed(self):
        print('item Changed')

    def get_product(self, db, uid, password):
        api = Client.api()
        products = (api
                    .execute_kw(db, uid, password,
                                'product.product',
                                'search_read',
                                [[['barcode', '=', '5651234567866']]],
                                {'limit': 1}))

        row = self.ui.tableDetail.rowCount()
        for p in products:
            self.ui.tableDetail.insertRow(row)
            self.ui.tableDetail.setItem(row, 0, QTableWidgetItem(str(p['id'])))
            self.ui.tableDetail.setItem(row, 1, QTableWidgetItem(p['name']))
