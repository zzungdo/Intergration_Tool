# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_PloygonDraw.ui'
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

class Ui_Dialog_PolygonDraw(object):
    def setupUi(self, Dialog_PolygonDraw):
        if not Dialog_PolygonDraw.objectName():
            Dialog_PolygonDraw.setObjectName(u"Dialog_PolygonDraw")
        Dialog_PolygonDraw.resize(400, 300)
        self.label = QLabel(Dialog_PolygonDraw)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(149, 135, 131, 31))

        self.retranslateUi(Dialog_PolygonDraw)

        QMetaObject.connectSlotsByName(Dialog_PolygonDraw)
    # setupUi

    def retranslateUi(self, Dialog_PolygonDraw):
        Dialog_PolygonDraw.setWindowTitle(QCoreApplication.translate("Dialog_PolygonDraw", u"Polygon Drawing", None))
        self.label.setText(QCoreApplication.translate("Dialog_PolygonDraw", u"Polygon Drawing", None))
    # retranslateUi

