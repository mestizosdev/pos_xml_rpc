from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QCloseEvent

from views.ui_company import Ui_CompanyWindow


class Company(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CompanyWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event: QCloseEvent) -> None:
        super().close()
        self.parent().show()
