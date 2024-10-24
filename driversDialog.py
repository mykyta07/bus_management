# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'driversDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSplitter,
    QWidget)

class Ui_driversDialog(object):
    def setupUi(self, driversDialog):
        if not driversDialog.objectName():
            driversDialog.setObjectName(u"driversDialog")
        driversDialog.resize(488, 484)
        driversDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter_2 = QSplitter(driversDialog)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 140, 451, 81))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label_3 = QLabel(self.splitter_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_2.addWidget(self.label_3)
        self.lineEdit_2 = QLineEdit(self.splitter_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"")
        self.splitter_2.addWidget(self.lineEdit_2)
        self.line = QFrame(driversDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 581, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton = QPushButton(driversDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 420, 121, 41))
        self.pushButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.pushButton.setCheckable(True)
        self.pushButton_2 = QPushButton(driversDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(350, 420, 121, 41))
        self.pushButton_2.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(200, 200, 200);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.pushButton_2.setCheckable(True)
        self.label = QLabel(driversDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 221, 41))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.splitter = QSplitter(driversDialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 70, 451, 71))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_2)
        self.lineEdit = QLineEdit(self.splitter)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")
        self.splitter.addWidget(self.lineEdit)
        self.splitter_3 = QSplitter(driversDialog)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(10, 230, 451, 81))
        self.splitter_3.setOrientation(Qt.Vertical)
        self.label_4 = QLabel(self.splitter_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_3.addWidget(self.label_4)
        self.lineEdit_3 = QLineEdit(self.splitter_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"")
        self.splitter_3.addWidget(self.lineEdit_3)
        self.splitter_4 = QSplitter(driversDialog)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 320, 451, 81))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_4.addWidget(self.label_5)
        self.lineEdit_4 = QLineEdit(self.splitter_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"")
        self.splitter_4.addWidget(self.lineEdit_4)

        self.retranslateUi(driversDialog)

        QMetaObject.connectSlotsByName(driversDialog)
    # setupUi

    def retranslateUi(self, driversDialog):
        driversDialog.setWindowTitle(QCoreApplication.translate("driversDialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("driversDialog", u"Second Name", None))
        self.pushButton.setText(QCoreApplication.translate("driversDialog", u"Submit", None))
        self.pushButton_2.setText(QCoreApplication.translate("driversDialog", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("driversDialog", u"Add new driver", None))
        self.label_2.setText(QCoreApplication.translate("driversDialog", u"First Name", None))
        self.label_4.setText(QCoreApplication.translate("driversDialog", u"License number", None))
        self.label_5.setText(QCoreApplication.translate("driversDialog", u"Phone", None))
    # retranslateUi

