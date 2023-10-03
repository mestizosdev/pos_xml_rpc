# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'point_of_sale.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_PosWindow(object):
    def setupUi(self, PosWindow):
        if not PosWindow.objectName():
            PosWindow.setObjectName(u"PosWindow")
        PosWindow.resize(800, 600)
        self.centralwidget = QWidget(PosWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableDetail = QTableWidget(self.centralwidget)
        if (self.tableDetail.columnCount() < 5):
            self.tableDetail.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableDetail.setObjectName(u"tableDetail")
        self.tableDetail.setGeometry(QRect(40, 120, 671, 271))
        self.pushAdd = QPushButton(self.centralwidget)
        self.pushAdd.setObjectName(u"pushAdd")
        self.pushAdd.setGeometry(QRect(40, 40, 119, 36))
        PosWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PosWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        PosWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PosWindow)
        self.statusbar.setObjectName(u"statusbar")
        PosWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PosWindow)

        QMetaObject.connectSlotsByName(PosWindow)
    # setupUi

    def retranslateUi(self, PosWindow):
        PosWindow.setWindowTitle(QCoreApplication.translate("PosWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableDetail.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PosWindow", u"barcode", None));
        ___qtablewidgetitem1 = self.tableDetail.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PosWindow", u"name", None));
        ___qtablewidgetitem2 = self.tableDetail.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PosWindow", u"unit_price", None));
        ___qtablewidgetitem3 = self.tableDetail.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PosWindow", u"quantity", None));
        ___qtablewidgetitem4 = self.tableDetail.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PosWindow", u"total", None));
        self.pushAdd.setText(QCoreApplication.translate("PosWindow", u"&Add", None))
    # retranslateUi

