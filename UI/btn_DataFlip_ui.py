# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_DataFlip.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)
from Resources import resources_rc

class Ui_Dialog_DataFlip(object):
    def setupUi(self, Dialog_DataFlip):
        if not Dialog_DataFlip.objectName():
            Dialog_DataFlip.setObjectName(u"Dialog_DataFlip")
        Dialog_DataFlip.setEnabled(True)
        Dialog_DataFlip.resize(701, 945)
        Dialog_DataFlip.setModal(False)
        self.gridLayout_3 = QGridLayout(Dialog_DataFlip)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.image_label = QLabel(Dialog_DataFlip)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)

        self.image_textEdit = QTextEdit(Dialog_DataFlip)
        self.image_textEdit.setObjectName(u"image_textEdit")
        self.image_textEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.image_textEdit, 1, 1, 1, 1)

        self.gt_textEdit = QTextEdit(Dialog_DataFlip)
        self.gt_textEdit.setObjectName(u"gt_textEdit")
        self.gt_textEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.gt_textEdit, 0, 1, 1, 1)

        self.output_label = QLabel(Dialog_DataFlip)
        self.output_label.setObjectName(u"output_label")
        self.output_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.output_label, 2, 0, 1, 1)

        self.output_textEdit = QTextEdit(Dialog_DataFlip)
        self.output_textEdit.setObjectName(u"output_textEdit")
        self.output_textEdit.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.output_textEdit, 2, 1, 1, 1)

        self.image_width_label = QLabel(Dialog_DataFlip)
        self.image_width_label.setObjectName(u"image_width_label")
        self.image_width_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.image_width_label, 3, 0, 1, 1)

        self.image_fileOpen = QPushButton(Dialog_DataFlip)
        self.image_fileOpen.setObjectName(u"image_fileOpen")
        self.image_fileOpen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.image_fileOpen, 1, 2, 1, 1)

        self.image_width_textEdit = QTextEdit(Dialog_DataFlip)
        self.image_width_textEdit.setObjectName(u"image_width_textEdit")

        self.gridLayout.addWidget(self.image_width_textEdit, 3, 1, 1, 1)

        self.gt_label = QLabel(Dialog_DataFlip)
        self.gt_label.setObjectName(u"gt_label")
        self.gt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.gt_label, 1, 0, 1, 1)

        self.gt_fileOpen = QPushButton(Dialog_DataFlip)
        self.gt_fileOpen.setObjectName(u"gt_fileOpen")
        self.gt_fileOpen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.gt_fileOpen, 0, 2, 1, 1)

        self.output_fileOpen = QPushButton(Dialog_DataFlip)
        self.output_fileOpen.setObjectName(u"output_fileOpen")
        self.output_fileOpen.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.gridLayout.addWidget(self.output_fileOpen, 2, 2, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.btn_run = QPushButton(Dialog_DataFlip)
        self.btn_run.setObjectName(u"btn_run")
        self.btn_run.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_2.addWidget(self.btn_run, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.before_label = QLabel(Dialog_DataFlip)
        self.before_label.setObjectName(u"before_label")
        font = QFont()
        font.setPointSize(15)
        self.before_label.setFont(font)
        self.before_label.setFrameShape(QFrame.Shape.NoFrame)
        self.before_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.before_label)

        self.ex_label_1 = QLabel(Dialog_DataFlip)
        self.ex_label_1.setObjectName(u"ex_label_1")
        self.ex_label_1.setPixmap(QPixmap(u":/test/KR_20211209_DAY_WALK_FRONT_140_N09027_0458.jpg"))
        self.ex_label_1.setScaledContents(True)
        self.ex_label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.ex_label_1)

        self.label_2 = QLabel(Dialog_DataFlip)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.label = QLabel(Dialog_DataFlip)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(17)
        self.label.setFont(font2)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(-3)

        self.gridLayout_3.addWidget(self.label, 2, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.after_label = QLabel(Dialog_DataFlip)
        self.after_label.setObjectName(u"after_label")
        self.after_label.setFont(font)
        self.after_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.after_label)

        self.ex_label_2 = QLabel(Dialog_DataFlip)
        self.ex_label_2.setObjectName(u"ex_label_2")
        self.ex_label_2.setPixmap(QPixmap(u":/test/KR_20211209_DAY_WALK_FRONT_140_N09027_0458_flip.jpg"))
        self.ex_label_2.setScaledContents(True)
        self.ex_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.ex_label_2)

        self.label_3 = QLabel(Dialog_DataFlip)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 2, 2, 1, 1)

        QWidget.setTabOrder(self.gt_textEdit, self.gt_fileOpen)
        QWidget.setTabOrder(self.gt_fileOpen, self.image_textEdit)
        QWidget.setTabOrder(self.image_textEdit, self.image_fileOpen)
        QWidget.setTabOrder(self.image_fileOpen, self.output_textEdit)
        QWidget.setTabOrder(self.output_textEdit, self.output_fileOpen)

        self.retranslateUi(Dialog_DataFlip)

        QMetaObject.connectSlotsByName(Dialog_DataFlip)
    # setupUi

    def retranslateUi(self, Dialog_DataFlip):
        Dialog_DataFlip.setWindowTitle(QCoreApplication.translate("Dialog_DataFlip", u"Flip_Dialog", None))
        self.image_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"GT Path", None))
        self.image_textEdit.setPlaceholderText(QCoreApplication.translate("Dialog_DataFlip", u"Image path", None))
        self.gt_textEdit.setPlaceholderText(QCoreApplication.translate("Dialog_DataFlip", u"GT path", None))
        self.output_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"Output Path", None))
        self.output_textEdit.setPlaceholderText(QCoreApplication.translate("Dialog_DataFlip", u"Output Path", None))
#if QT_CONFIG(tooltip)
        self.image_width_label.setToolTip(QCoreApplication.translate("Dialog_DataFlip", u"Image Width", None))
#endif // QT_CONFIG(tooltip)
        self.image_width_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"Image Width", None))
        self.image_fileOpen.setText(QCoreApplication.translate("Dialog_DataFlip", u"Open", None))
        self.image_width_textEdit.setPlaceholderText(QCoreApplication.translate("Dialog_DataFlip", u"GT \uc88c\uc6b0 \ubc18\uc804\uc744 \uc704\ud574 Image Width\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.gt_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"Image Path", None))
        self.gt_fileOpen.setText(QCoreApplication.translate("Dialog_DataFlip", u"Open", None))
        self.output_fileOpen.setText(QCoreApplication.translate("Dialog_DataFlip", u"Open", None))
        self.btn_run.setText(QCoreApplication.translate("Dialog_DataFlip", u"RUN", None))
        self.before_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"\uc2e4\ud589 \uc804", None))
        self.ex_label_1.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog_DataFlip", u"person,0,98,53,316", None))
        self.label.setText(QCoreApplication.translate("Dialog_DataFlip", u"\u2192", None))
        self.after_label.setText(QCoreApplication.translate("Dialog_DataFlip", u"\uc2e4\ud589 \ud6c4", None))
        self.ex_label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog_DataFlip", u"person,1867,98,1920,316", None))
    # retranslateUi

