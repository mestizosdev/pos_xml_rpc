from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtGui import QCloseEvent, QColor

from views.ui_company import Ui_CompanyWindow
from utils.client import Client


class Company(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompanyWindow()
        self.ui.setupUi(self)

        self.ui.tableCompany.setColumnWidth(0, 90)
        self.ui.tableCompany.setColumnWidth(1, 330)
        #        self.ui.tableCompany.itemClicked.connect(self.click_table)
        db, uid, password = Client.load()
        self.get_companies(db, uid, password)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()

    def setColortoRow(self, table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def get_companies(self, db, uid, password):
        api = Client.api()
        companies = (api
                     .execute_kw(db, uid, password,
                                 'res.company',
                                 'search_read',
                                 [[]],
                                 {'fields': ['id', 'name'],
                                  'limit': 10,
                                  'order': 'id asc'}))

        for c in companies:
            row = self.ui.tableCompany.rowCount()
            self.ui.tableCompany.insertRow(row)
            id = QTableWidgetItem(str(c['id']))
            name = QTableWidgetItem(c['name'])
            self.ui.tableCompany.setItem(row, 0, id)
            self.ui.tableCompany.setItem(row, 1, name)

    def click_table(self):
        print('click_table')
        row = self.ui.tableCompany.currentRow()
        self.setColortoRow(self.ui.tableCompany, row, QColor(125, 125, 125))
