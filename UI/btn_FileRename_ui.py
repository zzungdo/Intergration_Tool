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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Dialog_FileRename(object):
    def setupUi(self, Dialog_FileRename):
        if not Dialog_FileRename.objectName():
            Dialog_FileRename.setObjectName(u"Dialog_FileRename")
        Dialog_FileRename.resize(563, 536)
        Dialog_FileRename.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Dialog_FileRename)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.rBtn_rear = QRadioButton(Dialog_FileRename)
        self.rBtn_rear.setObjectName(u"rBtn_rear")

        self.gridLayout.addWidget(self.rBtn_rear, 4, 3, 1, 1)

        self.rBtn_front = QRadioButton(Dialog_FileRename)
        self.rBtn_front.setObjectName(u"rBtn_front")

        self.gridLayout.addWidget(self.rBtn_front, 4, 2, 1, 1)

        self.rBtn_rename = QRadioButton(Dialog_FileRename)
        self.rBtn_rename.setObjectName(u"rBtn_rename")
        self.rBtn_rename.setChecked(True)

        self.gridLayout.addWidget(self.rBtn_rename, 4, 1, 1, 1)

        self.textEdit_string = QTextEdit(Dialog_FileRename)
        self.textEdit_string.setObjectName(u"textEdit_string")

        self.gridLayout.addWidget(self.textEdit_string, 5, 1, 1, 3)

        self.textEdit_output_path = QTextEdit(Dialog_FileRename)
        self.textEdit_output_path.setObjectName(u"textEdit_output_path")

        self.gridLayout.addWidget(self.textEdit_output_path, 3, 1, 1, 3)

        self.pbth_output_path = QPushButton(Dialog_FileRename)
        self.pbth_output_path.setObjectName(u"pbth_output_path")

        self.gridLayout.addWidget(self.pbth_output_path, 3, 4, 1, 1)

        self.label_option = QLabel(Dialog_FileRename)
        self.label_option.setObjectName(u"label_option")

        self.gridLayout.addWidget(self.label_option, 4, 0, 1, 1)

        self.label_output_path = QLabel(Dialog_FileRename)
        self.label_output_path.setObjectName(u"label_output_path")

        self.gridLayout.addWidget(self.label_output_path, 3, 0, 1, 1)

        self.pbtn_input_path2 = QPushButton(Dialog_FileRename)
        self.pbtn_input_path2.setObjectName(u"pbtn_input_path2")

        self.gridLayout.addWidget(self.pbtn_input_path2, 2, 4, 1, 1)

        self.textEdit_input_path2 = QTextEdit(Dialog_FileRename)
        self.textEdit_input_path2.setObjectName(u"textEdit_input_path2")

        self.gridLayout.addWidget(self.textEdit_input_path2, 2, 1, 1, 3)

        self.textEdit_input_path1 = QTextEdit(Dialog_FileRename)
        self.textEdit_input_path1.setObjectName(u"textEdit_input_path1")

        self.gridLayout.addWidget(self.textEdit_input_path1, 1, 1, 1, 3)

        self.label_string = QLabel(Dialog_FileRename)
        self.label_string.setObjectName(u"label_string")

        self.gridLayout.addWidget(self.label_string, 5, 0, 1, 1)

        self.pbtn_input_path1 = QPushButton(Dialog_FileRename)
        self.pbtn_input_path1.setObjectName(u"pbtn_input_path1")

        self.gridLayout.addWidget(self.pbtn_input_path1, 1, 4, 1, 1)

        self.label_input_path1 = QLabel(Dialog_FileRename)
        self.label_input_path1.setObjectName(u"label_input_path1")

        self.gridLayout.addWidget(self.label_input_path1, 1, 0, 1, 1)

        self.label_input_path2 = QLabel(Dialog_FileRename)
        self.label_input_path2.setObjectName(u"label_input_path2")

        self.gridLayout.addWidget(self.label_input_path2, 2, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbtn_run = QPushButton(Dialog_FileRename)
        self.pbtn_run.setObjectName(u"pbtn_run")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtn_run.sizePolicy().hasHeightForWidth())
        self.pbtn_run.setSizePolicy(sizePolicy)
        self.pbtn_run.setMinimumSize(QSize(0, 50))
        self.pbtn_run.setMaximumSize(QSize(16777215, 16777215))
        self.pbtn_run.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.pbtn_run, 0, Qt.AlignHCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(Dialog_FileRename)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy1)
        self.progressBar.setMinimumSize(QSize(300, 0))
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_4)

        QWidget.setTabOrder(self.textEdit_input_path1, self.pbtn_input_path1)
        QWidget.setTabOrder(self.pbtn_input_path1, self.textEdit_output_path)
        QWidget.setTabOrder(self.textEdit_output_path, self.pbth_output_path)
        QWidget.setTabOrder(self.pbth_output_path, self.rBtn_rename)
        QWidget.setTabOrder(self.rBtn_rename, self.rBtn_front)
        QWidget.setTabOrder(self.rBtn_front, self.rBtn_rear)
        QWidget.setTabOrder(self.rBtn_rear, self.textEdit_string)

        self.retranslateUi(Dialog_FileRename)

        QMetaObject.connectSlotsByName(Dialog_FileRename)
    # setupUi

    def retranslateUi(self, Dialog_FileRename):
        Dialog_FileRename.setWindowTitle(QCoreApplication.translate("Dialog_FileRename", u"File_Rename_Dialog", None))
        self.rBtn_rear.setText(QCoreApplication.translate("Dialog_FileRename", u"\ud30c\uc77c\uba85 \ub4a4\uc5d0 \ucd94\uac00", None))
        self.rBtn_front.setText(QCoreApplication.translate("Dialog_FileRename", u"\ud30c\uc77c\uba85 \uc55e\uc5d0 \ucd94\uac00", None))
        self.rBtn_rename.setText(QCoreApplication.translate("Dialog_FileRename", u"\ud30c\uc77c\uba85 \ubcc0\uacbd", None))
        self.pbth_output_path.setText(QCoreApplication.translate("Dialog_FileRename", u"Open", None))
        self.label_option.setText(QCoreApplication.translate("Dialog_FileRename", u"Option", None))
        self.label_output_path.setText(QCoreApplication.translate("Dialog_FileRename", u"Output Data Path", None))
        self.pbtn_input_path2.setText(QCoreApplication.translate("Dialog_FileRename", u"Open", None))
        self.label_string.setText(QCoreApplication.translate("Dialog_FileRename", u"Replace string", None))
        self.pbtn_input_path1.setText(QCoreApplication.translate("Dialog_FileRename", u"Open", None))
        self.label_input_path1.setText(QCoreApplication.translate("Dialog_FileRename", u"Primary Input Path", None))
        self.label_input_path2.setText(QCoreApplication.translate("Dialog_FileRename", u"Secondary Input Path", None))
        self.pbtn_run.setText(QCoreApplication.translate("Dialog_FileRename", u"RUN", None))
    # retranslateUi

