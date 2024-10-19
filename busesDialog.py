# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busesDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QSplitter, QWidget)

class Ui_busesDialog(object):
    def setupUi(self, busesDialog):
        if not busesDialog.objectName():
            busesDialog.setObjectName(u"busesDialog")
        busesDialog.resize(471, 474)
        busesDialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line = QFrame(busesDialog)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 581, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(busesDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 221, 41))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.splitter_2 = QSplitter(busesDialog)
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
        self.splitter_3 = QSplitter(busesDialog)
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
        self.splitter = QSplitter(busesDialog)
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
        self.pushButton = QPushButton(busesDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 420, 121, 41))
        self.pushButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.pushButton_2 = QPushButton(busesDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(330, 420, 121, 41))
        self.pushButton_2.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(200, 200, 200);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.splitter_4 = QSplitter(busesDialog)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 320, 151, 81))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_4.addWidget(self.label_5)
        self.dateEdit = QDateEdit(self.splitter_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(2025, 12, 31), QTime(23, 59, 59)))
        self.splitter_4.addWidget(self.dateEdit)
        self.splitter_5 = QSplitter(busesDialog)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(170, 330, 141, 71))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_6 = QLabel(self.splitter_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_5.addWidget(self.label_6)
        self.spinBox = QSpinBox(self.splitter_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000000)
        self.splitter_5.addWidget(self.spinBox)

        self.retranslateUi(busesDialog)

        QMetaObject.connectSlotsByName(busesDialog)
    # setupUi

    def retranslateUi(self, busesDialog):
        busesDialog.setWindowTitle(QCoreApplication.translate("busesDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("busesDialog", u"Add new bus", None))
        self.label_3.setText(QCoreApplication.translate("busesDialog", u"Number Plate", None))
        self.label_4.setText(QCoreApplication.translate("busesDialog", u"Bus model", None))
        self.label_2.setText(QCoreApplication.translate("busesDialog", u"Model", None))
        self.pushButton.setText(QCoreApplication.translate("busesDialog", u"Submit", None))
        self.pushButton_2.setText(QCoreApplication.translate("busesDialog", u"Cancel", None))
        self.label_5.setText(QCoreApplication.translate("busesDialog", u"Service due to", None))
        self.label_6.setText(QCoreApplication.translate("busesDialog", u"Mileage", None))
        self.spinBox.setSpecialValueText("")
        self.spinBox.setSuffix(QCoreApplication.translate("busesDialog", u" km", None))
        self.spinBox.setPrefix("")
    # retranslateUi

