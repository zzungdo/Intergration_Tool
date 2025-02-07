# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(490, 348)
        MainWindow.setMinimumSize(QSize(270, 0))
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.actionmade_by = QAction(MainWindow)
        self.actionmade_by.setObjectName(u"actionmade_by")
        self.actionversion = QAction(MainWindow)
        self.actionversion.setObjectName(u"actionversion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setInputMethodHints(Qt.ImhNone)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_preprocess = QLabel(self.centralwidget)
        self.label_preprocess.setObjectName(u"label_preprocess")
        self.label_preprocess.setMaximumSize(QSize(16777215, 20))
        self.label_preprocess.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_preprocess, 1, 0, 1, 1)

        self.btn_FileRename = QPushButton(self.centralwidget)
        self.btn_FileRename.setObjectName(u"btn_FileRename")

        self.gridLayout.addWidget(self.btn_FileRename, 3, 0, 1, 1)

        self.btn_DataFlip = QPushButton(self.centralwidget)
        self.btn_DataFlip.setObjectName(u"btn_DataFlip")

        self.gridLayout.addWidget(self.btn_DataFlip, 2, 0, 1, 1)

        self.label_drawing = QLabel(self.centralwidget)
        self.label_drawing.setObjectName(u"label_drawing")
        self.label_drawing.setMaximumSize(QSize(16777215, 20))
        self.label_drawing.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_drawing, 1, 2, 1, 1)

        self.btn_PolygonDraw = QPushButton(self.centralwidget)
        self.btn_PolygonDraw.setObjectName(u"btn_PolygonDraw")

        self.gridLayout.addWidget(self.btn_PolygonDraw, 3, 2, 1, 1)

        self.btn_ImageView = QPushButton(self.centralwidget)
        self.btn_ImageView.setObjectName(u"btn_ImageView")

        self.gridLayout.addWidget(self.btn_ImageView, 2, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)

        self.btn_DataAnalysis = QPushButton(self.centralwidget)
        self.btn_DataAnalysis.setObjectName(u"btn_DataAnalysis")

        self.gridLayout.addWidget(self.btn_DataAnalysis, 2, 3, 1, 1)

        self.btn_DataCheck = QPushButton(self.centralwidget)
        self.btn_DataCheck.setObjectName(u"btn_DataCheck")

        self.gridLayout.addWidget(self.btn_DataCheck, 3, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 490, 22))
        self.Menu_help = QMenu(self.menubar)
        self.Menu_help.setObjectName(u"Menu_help")
        self.Menu_help.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.Menu_help.menuAction())
        self.Menu_help.addAction(self.actionversion)
        self.Menu_help.addAction(self.actionmade_by)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Select Frunction", None))
        self.actionmade_by.setText(QCoreApplication.translate("MainWindow", u"made by", None))
        self.actionversion.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.label_preprocess.setText(QCoreApplication.translate("MainWindow", u"PreProcessing", None))
        self.btn_FileRename.setText(QCoreApplication.translate("MainWindow", u"File Rename", None))
#if QT_CONFIG(tooltip)
        self.btn_DataFlip.setToolTip(QCoreApplication.translate("MainWindow", u"Dataset\uc744 \uc88c\uc6b0\ubc18\uc804 \ud569\ub2c8\ub2e4.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_DataFlip.setStatusTip(QCoreApplication.translate("MainWindow", u"Dataset \uc88c\uc6b0\ubc18\uc804", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_DataFlip.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_DataFlip.setText(QCoreApplication.translate("MainWindow", u"Flip", None))
        self.label_drawing.setText(QCoreApplication.translate("MainWindow", u"Drawing", None))
        self.btn_PolygonDraw.setText(QCoreApplication.translate("MainWindow", u"Polygon", None))
        self.btn_ImageView.setText(QCoreApplication.translate("MainWindow", u"Image View", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Inspection", None))
        self.btn_DataAnalysis.setText(QCoreApplication.translate("MainWindow", u"Dataset Analysis", None))
        self.btn_DataCheck.setText(QCoreApplication.translate("MainWindow", u"Dataset Check", None))
        self.Menu_help.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

