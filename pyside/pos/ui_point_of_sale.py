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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_PosWindow(object):
    def setupUi(self, PosWindow):
        if not PosWindow.objectName():
            PosWindow.setObjectName(u"PosWindow")
        PosWindow.resize(800, 600)
        self.centralwidget = QWidget(PosWindow)
        self.centralwidget.setObjectName(u"centralwidget")
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
    # retranslateUi

