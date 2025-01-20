# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(488, 340)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 30, 411, 231))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_1 = QPushButton(self.gridLayoutWidget)
        self.btn_1.setObjectName(u"btn_1")

        self.gridLayout.addWidget(self.btn_1, 0, 0, 1, 1)

        self.btn_2 = QPushButton(self.gridLayoutWidget)
        self.btn_2.setObjectName(u"btn_2")

        self.gridLayout.addWidget(self.btn_2, 0, 1, 1, 1)

        self.btn_3 = QPushButton(self.gridLayoutWidget)
        self.btn_3.setObjectName(u"btn_3")

        self.gridLayout.addWidget(self.btn_3, 1, 0, 1, 1)

        self.btn_4 = QPushButton(self.gridLayoutWidget)
        self.btn_4.setObjectName(u"btn_4")

        self.gridLayout.addWidget(self.btn_4, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 488, 22))
        self.Menu_help = QMenu(self.menubar)
        self.Menu_help.setObjectName(u"Menu_help")
        self.Menu_help.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.Menu_help.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"Image Flip", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"btn2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"btn3", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"btn4", None))
        self.Menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
    # retranslateUi

