# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionPoint_of_Sale = QAction(MainWindow)
        self.actionPoint_of_Sale.setObjectName(u"actionPoint_of_Sale")
        self.actionPrinter = QAction(MainWindow)
        self.actionPrinter.setObjectName(u"actionPrinter")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuTransacction = QMenu(self.menubar)
        self.menuTransacction.setObjectName(u"menuTransacction")
        self.menuParameter = QMenu(self.menubar)
        self.menuParameter.setObjectName(u"menuParameter")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTransacction.menuAction())
        self.menubar.addAction(self.menuParameter.menuAction())
        self.menuTransacction.addAction(self.actionPoint_of_Sale)
        self.menuParameter.addAction(self.actionPrinter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Point of Sale for Odoo", None))
        self.actionPoint_of_Sale.setText(QCoreApplication.translate("MainWindow", u"&Point of Sale", None))
        self.actionPrinter.setText(QCoreApplication.translate("MainWindow", u"P&rinter", None))
        self.menuTransacction.setTitle(QCoreApplication.translate("MainWindow", u"&Transacction", None))
        self.menuParameter.setTitle(QCoreApplication.translate("MainWindow", u"&Parameter", None))
    # retranslateUi

