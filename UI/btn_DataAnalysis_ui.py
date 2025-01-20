# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_DataAnalysis.ui'
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

class Ui_Dialog_DataAnalysis(object):
    def setupUi(self, Dialog_DataAnalysis):
        if not Dialog_DataAnalysis.objectName():
            Dialog_DataAnalysis.setObjectName(u"Dialog_DataAnalysis")
        Dialog_DataAnalysis.resize(400, 300)
        self.label = QLabel(Dialog_DataAnalysis)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 110, 171, 61))

        self.retranslateUi(Dialog_DataAnalysis)

        QMetaObject.connectSlotsByName(Dialog_DataAnalysis)
    # setupUi

    def retranslateUi(self, Dialog_DataAnalysis):
        Dialog_DataAnalysis.setWindowTitle(QCoreApplication.translate("Dialog_DataAnalysis", u"Dataset Analysis", None))
        self.label.setText(QCoreApplication.translate("Dialog_DataAnalysis", u"Data Analysis", None))
    # retranslateUi

