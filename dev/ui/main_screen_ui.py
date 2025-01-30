# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_screenFepFhC.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExport = QAction(MainWindow)
        self.actionExport.setObjectName(u"actionExport")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.mainTableWidget = QTableWidget(self.centralwidget)
        if (self.mainTableWidget.columnCount() < 3):
            self.mainTableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.mainTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.mainTableWidget.setObjectName(u"mainTableWidget")
        self.mainTableWidget.setGeometry(QRect(10, 0, 771, 601))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuf = QMenu(self.menubar)
        self.menuf.setObjectName(u"menuf")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuf.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menuf.addAction(self.actionOpen)
        self.menuf.addAction(self.actionSave)
        self.menuf.addAction(self.actionExport)
        self.menuf.addSeparator()
        self.menuf.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.actionExport.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        ___qtablewidgetitem = self.mainTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Source Text", None));
        ___qtablewidgetitem1 = self.mainTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Finished Text", None));
        ___qtablewidgetitem2 = self.mainTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Completion status", None));
        self.menuf.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi

