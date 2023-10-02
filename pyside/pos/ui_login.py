# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 40, 321, 101))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.txtUsername = QLineEdit(self.formLayoutWidget)
        self.txtUsername.setObjectName(u"txtUsername")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtUsername)

        self.lblUsername = QLabel(self.formLayoutWidget)
        self.lblUsername.setObjectName(u"lblUsername")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblUsername)

        self.lblPassword = QLabel(self.formLayoutWidget)
        self.lblPassword.setObjectName(u"lblPassword")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblPassword)

        self.txtPassword = QLineEdit(self.formLayoutWidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtPassword)

#if QT_CONFIG(shortcut)
        self.lblUsername.setBuddy(self.txtUsername)
        self.lblPassword.setBuddy(self.txtPassword)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.lblUsername.setText(QCoreApplication.translate("Dialog", u"&Username:", None))
        self.lblPassword.setText(QCoreApplication.translate("Dialog", u"&Password:", None))
    # retranslateUi

