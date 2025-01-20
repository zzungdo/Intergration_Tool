# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_FileRename.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog_FileRename(object):
    def setupUi(self, Dialog_FileRename):
        if not Dialog_FileRename.objectName():
            Dialog_FileRename.setObjectName(u"Dialog_FileRename")
        Dialog_FileRename.resize(400, 300)
        self.formLayout = QFormLayout(Dialog_FileRename)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog_FileRename)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)


        self.retranslateUi(Dialog_FileRename)

        QMetaObject.connectSlotsByName(Dialog_FileRename)
    # setupUi

    def retranslateUi(self, Dialog_FileRename):
        Dialog_FileRename.setWindowTitle(QCoreApplication.translate("Dialog_FileRename", u"File_Rename_Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_FileRename", u"File Rename", None))
    # retranslateUi

