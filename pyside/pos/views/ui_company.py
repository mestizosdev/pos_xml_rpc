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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_CompanyWindow(object):
    def setupUi(self, CompanyWindow):
        if not CompanyWindow.objectName():
            CompanyWindow.setObjectName(u"CompanyWindow")
        CompanyWindow.resize(800, 600)
        self.centralwidget = QWidget(CompanyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
    # retranslateUi

