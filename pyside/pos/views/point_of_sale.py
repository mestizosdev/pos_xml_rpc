from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtGui import QCloseEvent

from utils import message
from utils.client import Client
from views.ui_point_of_sale import Ui_PosWindow


class PontOfSale(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PosWindow()
        self.ui.setupUi(self)
        self.ui.txtBarcode.setFocus()
        self.ui.pushAdd.clicked.connect(self.add_row)
        self.ui.pushRemove.clicked.connect(self.remove_row)
        self.ui.txtBarcode.returnPressed.connect(self.get_product)
        self.ui.tableDetail.itemChanged.connect(self.item_changed)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()

    def item_changed(self, item):
        if item.column() == 3:
            print(item.text())

    def add_row(self):
        self.get_product()

    def remove_row(self):
        row = self.ui.tableDetail.currentRow()
        self.ui.tableDetail.removeRow(row)

    def get_product(self):
        api = Client.api()
        db, uid, password = Client.load()
        exist_product = False

        barcode = self.ui.txtBarcode.text()
        products = (api
                    .execute_kw(db, uid, password,
                                'product.product',
                                'search_read',
                                [[['barcode', '=', barcode]]],
                                {'limit': 1}))

        row = self.ui.tableDetail.rowCount()
        for p in products:
            exist_product = True
            print(products)
            self.ui.tableDetail.insertRow(row)
            self.ui.tableDetail.setItem(row, 0, QTableWidgetItem(str(p['id'])))
            self.ui.tableDetail.setItem(row, 1, QTableWidgetItem(p['name']))
            self.ui.tableDetail.setItem(row, 2, QTableWidgetItem(str(1.00)))
            self.ui.tableDetail.setItem(row, 3, QTableWidgetItem(str(2)))
            self.ui.tableDetail.setItem(row, 4, QTableWidgetItem(str(2)))

        if not exist_product:
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Error!!!")
            dialog.setText('Product not found')
            dialog.setStandardButtons(QMessageBox.Ok)
            dialog.setIcon(QMessageBox.Warning)
            dialog.show()
            # message.error('Product not found')

        self.ui.txtBarcode.setText('')
        self.ui.txtBarcode.setFocus()
        self.ui.tableDetail.resizeColumnsToContents()
        print(self.ui.tableDetail.hasFocus())

