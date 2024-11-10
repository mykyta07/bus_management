# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'routeInfoDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
    QSplitter, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(825, 552)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.mapWidget = QWidget(Dialog)
        self.mapWidget.setObjectName(u"mapWidget")
        self.mapWidget.setGeometry(QRect(450, 130, 351, 401))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 10, 221, 41))
        self.label_5.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")
        self.labelCurrentLabel = QLabel(Dialog)
        self.labelCurrentLabel.setObjectName(u"labelCurrentLabel")
        self.labelCurrentLabel.setGeometry(QRect(540, 80, 161, 21))
        self.labelCurrentLabel.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 70, 441, 391))
        self.splitter.setOrientation(Qt.Vertical)
        self.labelRoute = QLabel(self.splitter)
        self.labelRoute.setObjectName(u"labelRoute")
        self.splitter.addWidget(self.labelRoute)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_11)
        self.label_12 = QLabel(self.splitter)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_12)
        self.label_13 = QLabel(self.splitter)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_13)
        self.label_14 = QLabel(self.splitter)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_14)
        self.label_15 = QLabel(self.splitter)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_15)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Route information", None))
        self.labelCurrentLabel.setText(QCoreApplication.translate("Dialog", u"Route overview", None))
        self.labelRoute.setText("")
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Driver", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Bus", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Departure date:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Arrival", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Time in road", None))
    # retranslateUi

