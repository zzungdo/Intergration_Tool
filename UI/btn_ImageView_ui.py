# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'btn_ImageView.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow_ImageView(object):
    def setupUi(self, MainWindow_ImageView):
        if not MainWindow_ImageView.objectName():
            MainWindow_ImageView.setObjectName(u"MainWindow_ImageView")
        MainWindow_ImageView.resize(1502, 661)
        MainWindow_ImageView.setMinimumSize(QSize(1410, 0))
        self.action1st_GT = QAction(MainWindow_ImageView)
        self.action1st_GT.setObjectName(u"action1st_GT")
        self.action1st_Image_2 = QAction(MainWindow_ImageView)
        self.action1st_Image_2.setObjectName(u"action1st_Image_2")
        self.action2nd_GT = QAction(MainWindow_ImageView)
        self.action2nd_GT.setObjectName(u"action2nd_GT")
        self.action2nd_Image_2 = QAction(MainWindow_ImageView)
        self.action2nd_Image_2.setObjectName(u"action2nd_Image_2")
        self.actionasd = QAction(MainWindow_ImageView)
        self.actionasd.setObjectName(u"actionasd")
        self.actionOutput_Path = QAction(MainWindow_ImageView)
        self.actionOutput_Path.setObjectName(u"actionOutput_Path")
        self.centralwidget = QWidget(MainWindow_ImageView)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tableWidget_Path1_FileList = QTableWidget(self.splitter)
        self.tableWidget_Path1_FileList.setObjectName(u"tableWidget_Path1_FileList")
        self.tableWidget_Path1_FileList.setMinimumSize(QSize(150, 0))
        self.tableWidget_Path1_FileList.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_Path1_FileList.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_Path1_FileList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Path1_FileList.setTabKeyNavigation(False)
        self.tableWidget_Path1_FileList.setProperty(u"showDropIndicator", True)
        self.tableWidget_Path1_FileList.setDragDropOverwriteMode(False)
        self.tableWidget_Path1_FileList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_Path1_FileList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.splitter.addWidget(self.tableWidget_Path1_FileList)
        self.tableWidget_Path1_FileList.horizontalHeader().setVisible(True)
        self.tableWidget_Path1_FileList.horizontalHeader().setStretchLastSection(True)
        self.label_ImageView_1 = QLabel(self.splitter)
        self.label_ImageView_1.setObjectName(u"label_ImageView_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ImageView_1.sizePolicy().hasHeightForWidth())
        self.label_ImageView_1.setSizePolicy(sizePolicy)
        self.label_ImageView_1.setMinimumSize(QSize(500, 600))
        self.label_ImageView_1.setStyleSheet(u"border: 1px solid black;\n"
"")
        self.label_ImageView_1.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_ImageView_1)
        self.label_ImageView_2 = QLabel(self.splitter)
        self.label_ImageView_2.setObjectName(u"label_ImageView_2")
        sizePolicy.setHeightForWidth(self.label_ImageView_2.sizePolicy().hasHeightForWidth())
        self.label_ImageView_2.setSizePolicy(sizePolicy)
        self.label_ImageView_2.setMinimumSize(QSize(500, 600))
        self.label_ImageView_2.setStyleSheet(u"border: 1px solid black;\n"
"")
        self.label_ImageView_2.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_ImageView_2)
        self.tableWidget_Path2_FileList = QTableWidget(self.splitter)
        self.tableWidget_Path2_FileList.setObjectName(u"tableWidget_Path2_FileList")
        self.tableWidget_Path2_FileList.setMinimumSize(QSize(150, 0))
        self.tableWidget_Path2_FileList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_Path2_FileList.setTabKeyNavigation(False)
        self.tableWidget_Path2_FileList.setDragDropOverwriteMode(False)
        self.tableWidget_Path2_FileList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_Path2_FileList.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.splitter.addWidget(self.tableWidget_Path2_FileList)
        self.tableWidget_Path2_FileList.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.VGroupBox_BboxOnOff = QGroupBox(self.centralwidget)
        self.VGroupBox_BboxOnOff.setObjectName(u"VGroupBox_BboxOnOff")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.VGroupBox_BboxOnOff.sizePolicy().hasHeightForWidth())
        self.VGroupBox_BboxOnOff.setSizePolicy(sizePolicy1)
        self.VGroupBox_BboxOnOff.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.VGroupBox_BboxOnOff)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rBtn_BboxOff = QRadioButton(self.VGroupBox_BboxOnOff)
        self.rBtn_BboxOff.setObjectName(u"rBtn_BboxOff")
        self.rBtn_BboxOff.setChecked(True)

        self.verticalLayout_2.addWidget(self.rBtn_BboxOff)

        self.rBtn_BboxOn = QRadioButton(self.VGroupBox_BboxOnOff)
        self.rBtn_BboxOn.setObjectName(u"rBtn_BboxOn")

        self.verticalLayout_2.addWidget(self.rBtn_BboxOn)


        self.gridLayout.addWidget(self.VGroupBox_BboxOnOff, 3, 0, 1, 1)

        self.VGroupBox_Info = QGroupBox(self.centralwidget)
        self.VGroupBox_Info.setObjectName(u"VGroupBox_Info")
        sizePolicy1.setHeightForWidth(self.VGroupBox_Info.sizePolicy().hasHeightForWidth())
        self.VGroupBox_Info.setSizePolicy(sizePolicy1)
        self.VGroupBox_Info.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.VGroupBox_Info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cBox_classname = QCheckBox(self.VGroupBox_Info)
        self.cBox_classname.setObjectName(u"cBox_classname")

        self.verticalLayout_3.addWidget(self.cBox_classname)

        self.cBox_score = QCheckBox(self.VGroupBox_Info)
        self.cBox_score.setObjectName(u"cBox_score")

        self.verticalLayout_3.addWidget(self.cBox_score)


        self.gridLayout.addWidget(self.VGroupBox_Info, 4, 0, 1, 1)

        self.VGroupBox_View = QGroupBox(self.centralwidget)
        self.VGroupBox_View.setObjectName(u"VGroupBox_View")
        sizePolicy1.setHeightForWidth(self.VGroupBox_View.sizePolicy().hasHeightForWidth())
        self.VGroupBox_View.setSizePolicy(sizePolicy1)
        self.VGroupBox_View.setMaximumSize(QSize(150, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.VGroupBox_View)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rBtn_Dual = QRadioButton(self.VGroupBox_View)
        self.rBtn_Dual.setObjectName(u"rBtn_Dual")
        self.rBtn_Dual.setChecked(True)

        self.verticalLayout_5.addWidget(self.rBtn_Dual)

        self.rBtn_1stPath = QRadioButton(self.VGroupBox_View)
        self.rBtn_1stPath.setObjectName(u"rBtn_1stPath")

        self.verticalLayout_5.addWidget(self.rBtn_1stPath)

        self.rBtn_2ndPath = QRadioButton(self.VGroupBox_View)
        self.rBtn_2ndPath.setObjectName(u"rBtn_2ndPath")

        self.verticalLayout_5.addWidget(self.rBtn_2ndPath)


        self.gridLayout.addWidget(self.VGroupBox_View, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(17, 414, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        MainWindow_ImageView.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow_ImageView)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1502, 22))
        self.menuOpen = QMenu(self.menubar)
        self.menuOpen.setObjectName(u"menuOpen")
        self.menu1st_Image = QMenu(self.menuOpen)
        self.menu1st_Image.setObjectName(u"menu1st_Image")
        self.menu2nd_Path = QMenu(self.menuOpen)
        self.menu2nd_Path.setObjectName(u"menu2nd_Path")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow_ImageView.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow_ImageView)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow_ImageView.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOpen.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menuOpen.addAction(self.menu1st_Image.menuAction())
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.menu2nd_Path.menuAction())
        self.menuOpen.addSeparator()
        self.menuOpen.addAction(self.actionOutput_Path)
        self.menu1st_Image.addAction(self.action1st_GT)
        self.menu1st_Image.addSeparator()
        self.menu1st_Image.addAction(self.action1st_Image_2)
        self.menu2nd_Path.addAction(self.action2nd_GT)
        self.menu2nd_Path.addSeparator()
        self.menu2nd_Path.addAction(self.action2nd_Image_2)

        self.retranslateUi(MainWindow_ImageView)

        QMetaObject.connectSlotsByName(MainWindow_ImageView)
    # setupUi

    def retranslateUi(self, MainWindow_ImageView):
        MainWindow_ImageView.setWindowTitle(QCoreApplication.translate("MainWindow_ImageView", u"MainWindow", None))
        self.action1st_GT.setText(QCoreApplication.translate("MainWindow_ImageView", u"GT", None))
        self.action1st_Image_2.setText(QCoreApplication.translate("MainWindow_ImageView", u"Image", None))
        self.action2nd_GT.setText(QCoreApplication.translate("MainWindow_ImageView", u"GT", None))
        self.action2nd_Image_2.setText(QCoreApplication.translate("MainWindow_ImageView", u"Image", None))
        self.actionasd.setText(QCoreApplication.translate("MainWindow_ImageView", u"asd", None))
        self.actionOutput_Path.setText(QCoreApplication.translate("MainWindow_ImageView", u"Output Path", None))
        self.label_ImageView_1.setText(QCoreApplication.translate("MainWindow_ImageView", u"Path 1 Image", None))
        self.label_ImageView_2.setText(QCoreApplication.translate("MainWindow_ImageView", u"Path 2 Image", None))
        self.VGroupBox_BboxOnOff.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"Bounding Box On/Off", None))
        self.rBtn_BboxOff.setText(QCoreApplication.translate("MainWindow_ImageView", u"Off", None))
        self.rBtn_BboxOn.setText(QCoreApplication.translate("MainWindow_ImageView", u"On", None))
        self.VGroupBox_Info.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"Information", None))
        self.cBox_classname.setText(QCoreApplication.translate("MainWindow_ImageView", u"Classname", None))
        self.cBox_score.setText(QCoreApplication.translate("MainWindow_ImageView", u"Confidence Score", None))
        self.VGroupBox_View.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"View", None))
#if QT_CONFIG(tooltip)
        self.rBtn_Dual.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.rBtn_Dual.setText(QCoreApplication.translate("MainWindow_ImageView", u"Dual", None))
        self.rBtn_1stPath.setText(QCoreApplication.translate("MainWindow_ImageView", u"1st Path Single", None))
        self.rBtn_2ndPath.setText(QCoreApplication.translate("MainWindow_ImageView", u"2nd Path Single", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow_ImageView", u"Previous", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow_ImageView", u"Next", None))
        self.menuOpen.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"Open", None))
        self.menu1st_Image.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"1st Path", None))
        self.menu2nd_Path.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"2nd Path", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow_ImageView", u"\ub2e8\ucd95\ud0a4", None))
#if QT_CONFIG(tooltip)
        self.statusbar.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip(QCoreApplication.translate("MainWindow_ImageView", u"Status Bar", None))
#endif // QT_CONFIG(statustip)
    # retranslateUi

