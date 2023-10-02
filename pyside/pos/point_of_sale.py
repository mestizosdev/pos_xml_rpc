from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QCloseEvent

from ui_point_of_sale import Ui_PosWindow


class PontOfSale(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PosWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event: QCloseEvent) -> None:
        super()
        self.parent().show()
