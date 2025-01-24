# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_DatasetCheck.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog_DatasetCheck(object):
    def setupUi(self, Dialog_DatasetCheck):
        if not Dialog_DatasetCheck.objectName():
            Dialog_DatasetCheck.setObjectName(u"Dialog_DatasetCheck")
        Dialog_DatasetCheck.resize(414, 109)
        self.label = QLabel(Dialog_DatasetCheck)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 81, 41))

        self.retranslateUi(Dialog_DatasetCheck)

        QMetaObject.connectSlotsByName(Dialog_DatasetCheck)
    # setupUi

    def retranslateUi(self, Dialog_DatasetCheck):
        Dialog_DatasetCheck.setWindowTitle(QCoreApplication.translate("Dialog_DatasetCheck", u"Dataset Check", None))
        self.label.setText(QCoreApplication.translate("Dialog_DatasetCheck", u"Data Check", None))
    # retranslateUi

