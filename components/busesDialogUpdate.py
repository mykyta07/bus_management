# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busesDialogUpdate.ui'
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

today_date = QDate.currentDate()

class Ui_busesDialogUpdate(object):
    def setupUi(self, busesDialogUpdate):
        if not busesDialogUpdate.objectName():
            busesDialogUpdate.setObjectName(u"busesDialogUpdate")
        busesDialogUpdate.resize(493, 388)
        busesDialogUpdate.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line = QFrame(busesDialogUpdate)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 581, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(busesDialogUpdate)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 221, 41))
        self.label.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";")
        self.splitter_2 = QSplitter(busesDialogUpdate)
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
        self.splitter = QSplitter(busesDialogUpdate)
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
        self.UpdateBusButton = QPushButton(busesDialogUpdate)
        self.UpdateBusButton.setObjectName(u"UpdateBusButton")
        self.UpdateBusButton.setGeometry(QRect(220, 330, 121, 41))
        self.UpdateBusButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.UpdateBusButton.setCheckable(True)
        self.CancelUpdateButton = QPushButton(busesDialogUpdate)
        self.CancelUpdateButton.setObjectName(u"CancelUpdateButton")
        self.CancelUpdateButton.setGeometry(QRect(360, 330, 121, 41))
        self.CancelUpdateButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(200, 200, 200);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.CancelUpdateButton.setCheckable(True)
        self.splitter_4 = QSplitter(busesDialogUpdate)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 230, 151, 81))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_5 = QLabel(self.splitter_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_4.addWidget(self.label_5)
        self.dateEdit = QDateEdit(self.splitter_4)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDateTime(QDateTime(today_date.addDays(10), QTime(0, 0, 0)))
        self.dateEdit.setMaximumDateTime(QDateTime(QDate(2025, 12, 31), QTime(23, 59, 59)))
        self.dateEdit.setMinimumDateTime(QDateTime(QDate(2024, 9, 14), QTime(0, 0, 0)))
        self.splitter_4.addWidget(self.dateEdit)
        self.splitter_5 = QSplitter(busesDialogUpdate)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(170, 240, 141, 71))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_6 = QLabel(self.splitter_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_5.addWidget(self.label_6)
        self.spinBox = QSpinBox(self.splitter_5)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(1000000)
        self.splitter_5.addWidget(self.spinBox)

        self.retranslateUi(busesDialogUpdate)

        QMetaObject.connectSlotsByName(busesDialogUpdate)
    # setupUi

    def retranslateUi(self, busesDialogUpdate):
        busesDialogUpdate.setWindowTitle(QCoreApplication.translate("busesDialogUpdate", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("busesDialogUpdate", u"Update Bus", None))
        self.label_3.setText(QCoreApplication.translate("busesDialogUpdate", u"Number Plate", None))
        self.label_2.setText(QCoreApplication.translate("busesDialogUpdate", u"Model", None))
        self.UpdateBusButton.setText(QCoreApplication.translate("busesDialogUpdate", u"Update", None))
        self.CancelUpdateButton.setText(QCoreApplication.translate("busesDialogUpdate", u"Cancel", None))
        self.label_5.setText(QCoreApplication.translate("busesDialogUpdate", u"Service due to", None))
        self.label_6.setText(QCoreApplication.translate("busesDialogUpdate", u"Mileage", None))
        self.spinBox.setSpecialValueText("")
        self.spinBox.setSuffix(QCoreApplication.translate("busesDialogUpdate", u" km", None))
        self.spinBox.setPrefix("")
    # retranslateUi

