# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marker_dialogOQRBqs.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLineEdit, QRadioButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Marker_filter(object):
    def setupUi(self, Marker_filter):
        if not Marker_filter.objectName():
            Marker_filter.setObjectName(u"Marker_filter")
        Marker_filter.resize(395, 281)
        self.okay_buttonBox = QDialogButtonBox(Marker_filter)
        self.okay_buttonBox.setObjectName(u"okay_buttonBox")
        self.okay_buttonBox.setGeometry(QRect(280, 250, 101, 32))
        self.okay_buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.okay_buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.textBrowser = QTextBrowser(Marker_filter)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 20, 241, 31))
        self.yes_radioButton = QRadioButton(Marker_filter)
        self.yes_radioButton.setObjectName(u"yes_radioButton")
        self.yes_radioButton.setGeometry(QRect(280, 25, 92, 20))
        self.no_radioButton = QRadioButton(Marker_filter)
        self.no_radioButton.setObjectName(u"no_radioButton")
        self.no_radioButton.setGeometry(QRect(340, 25, 92, 20))
        self.no_radioButton.setChecked(True)
        self.startsWith_lineEdit = QLineEdit(Marker_filter)
        self.startsWith_lineEdit.setObjectName(u"startsWith_lineEdit")
        self.startsWith_lineEdit.setGeometry(QRect(30, 130, 241, 22))
        self.EndsWith_lineEdit = QLineEdit(Marker_filter)
        self.EndsWith_lineEdit.setObjectName(u"EndsWith_lineEdit")
        self.EndsWith_lineEdit.setGeometry(QRect(30, 200, 241, 22))
        self.textBrowser_2 = QTextBrowser(Marker_filter)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(30, 90, 241, 31))
        self.textBrowser_3 = QTextBrowser(Marker_filter)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(30, 160, 241, 31))

        self.retranslateUi(Marker_filter)
        self.okay_buttonBox.accepted.connect(Marker_filter.accept)
        self.okay_buttonBox.rejected.connect(Marker_filter.reject)

        QMetaObject.connectSlotsByName(Marker_filter)
    # setupUi

    def retranslateUi(self, Marker_filter):
        Marker_filter.setWindowTitle(QCoreApplication.translate("Marker_filter", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Marker_filter", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Look out for a specific marker for the text?</p></body></html>", None))
        self.yes_radioButton.setText(QCoreApplication.translate("Marker_filter", u"Yes", None))
        self.no_radioButton.setText(QCoreApplication.translate("Marker_filter", u"No", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Marker_filter", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Starts with:</p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Marker_filter", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ends with:</p></body></html>", None))
    # retranslateUi

