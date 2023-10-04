# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'company.ui'
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
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_CompanyWindow(object):
    def setupUi(self, CompanyWindow):
        if not CompanyWindow.objectName():
            CompanyWindow.setObjectName(u"CompanyWindow")
        CompanyWindow.resize(800, 600)
        self.centralwidget = QWidget(CompanyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableCompany = QTableWidget(self.centralwidget)
        if (self.tableCompany.columnCount() < 2):
            self.tableCompany.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableCompany.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableCompany.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableCompany.setObjectName(u"tableCompany")
        self.tableCompany.setGeometry(QRect(120, 110, 511, 171))
        self.tableCompany.setGridStyle(Qt.SolidLine)
        CompanyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CompanyWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        CompanyWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CompanyWindow)
        self.statusbar.setObjectName(u"statusbar")
        CompanyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CompanyWindow)

        QMetaObject.connectSlotsByName(CompanyWindow)
    # setupUi

    def retranslateUi(self, CompanyWindow):
        CompanyWindow.setWindowTitle(QCoreApplication.translate("CompanyWindow", u"Company", None))
        ___qtablewidgetitem = self.tableCompany.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CompanyWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableCompany.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CompanyWindow", u"name", None));
    # retranslateUi

