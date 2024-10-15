# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar_menu = QWidget(self.centralwidget)
        self.sidebar_menu.setObjectName(u"sidebar_menu")
        self.sidebar_menu.setGeometry(QRect(0, 0, 241, 801))
        self.sidebar_menu.setStyleSheet(u"\n"
"background-color: rgb(1,1,1)")
        self.label_2 = QLabel(self.sidebar_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 221, 71))
        self.label_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.sidebar_menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 241, 211))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.routes_button = QPushButton(self.layoutWidget)
        self.routes_button.setObjectName(u"routes_button")
        self.routes_button.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/point-objects-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.routes_button.setIcon(icon)
        self.routes_button.setIconSize(QSize(30, 30))
        self.routes_button.setCheckable(True)
        self.routes_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.routes_button)

        self.bus_button = QPushButton(self.layoutWidget)
        self.bus_button.setObjectName(u"bus_button")
        self.bus_button.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/bus-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bus_button.setIcon(icon1)
        self.bus_button.setIconSize(QSize(30, 30))
        self.bus_button.setCheckable(True)
        self.bus_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.bus_button)

        self.drivers_button = QPushButton(self.layoutWidget)
        self.drivers_button.setObjectName(u"drivers_button")
        self.drivers_button.setEnabled(True)
        self.drivers_button.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/user-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.drivers_button.setIcon(icon2)
        self.drivers_button.setIconSize(QSize(30, 30))
        self.drivers_button.setCheckable(True)
        self.drivers_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.drivers_button)

        self.layoutWidget1 = QWidget(self.sidebar_menu)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 690, 241, 111))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settings_button = QPushButton(self.layoutWidget1)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setEnabled(True)
        self.settings_button.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/settings-4-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon3)
        self.settings_button.setIconSize(QSize(30, 30))
        self.settings_button.setCheckable(True)
        self.settings_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.settings_button)

        self.exit_button = QPushButton(self.layoutWidget1)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setEnabled(True)
        self.exit_button.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/door-8-24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon4)
        self.exit_button.setIconSize(QSize(30, 30))
        self.exit_button.setCheckable(True)
        self.exit_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exit_button)

        self.main_screen = QWidget(self.centralwidget)
        self.main_screen.setObjectName(u"main_screen")
        self.main_screen.setGeometry(QRect(250, 80, 871, 731))
        self.main_screen.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 871, 721))
        self.buses_page = QWidget()
        self.buses_page.setObjectName(u"buses_page")
        self.label_4 = QLabel(self.buses_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 300, 121, 81))
        self.label_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.buses_page)
        self.routes_page = QWidget()
        self.routes_page.setObjectName(u"routes_page")
        self.label_5 = QLabel(self.routes_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 300, 131, 81))
        self.label_5.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.routes_page)
        self.drivers_page = QWidget()
        self.drivers_page.setObjectName(u"drivers_page")
        self.label_6 = QLabel(self.drivers_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 300, 141, 81))
        self.label_6.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
        self.stackedWidget.addWidget(self.drivers_page)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(250, 0, 871, 81))
        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(470, 20, 281, 31))
        self.lineEdit.setStyleSheet(u"padding-left:20 px;\n"
"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 181, 31))
        self.label.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 221, 31))
        self.label_3.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(153, 153, 153);\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bus Managment", None))
        self.routes_button.setText(QCoreApplication.translate("MainWindow", u"Routes", None))
        self.bus_button.setText(QCoreApplication.translate("MainWindow", u"Buses", None))
        self.drivers_button.setText(QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Buses Page", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Routes Page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Drivers Page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hi, Admin!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to Bus Managment", None))
    # retranslateUi

