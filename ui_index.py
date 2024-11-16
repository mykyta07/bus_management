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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDateTimeEdit,
    QHeaderView, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1119, 805)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sidebar_menu = QWidget(self.centralwidget)
        self.sidebar_menu.setObjectName(u"sidebar_menu")
        self.sidebar_menu.setGeometry(QRect(0, 0, 241, 801))
        self.sidebar_menu.setStyleSheet(u"\n"
"background-color: rgb(1,1,1)")
        self.layoutWidget = QWidget(self.sidebar_menu)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 120, 241, 281))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.schedule_button = QPushButton(self.layoutWidget)
        self.schedule_button.setObjectName(u"schedule_button")
        self.schedule_button.setEnabled(True)
        self.schedule_button.setStyleSheet(u"QPushButton:checked{\n"
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
        icon.addFile(u":/icons/calendar-10-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schedule_button.setIcon(icon)
        self.schedule_button.setIconSize(QSize(30, 30))
        self.schedule_button.setCheckable(True)
        self.schedule_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.schedule_button)

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
        icon1 = QIcon()
        icon1.addFile(u":/icons/point-objects-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.routes_button.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/bus-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bus_button.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/user-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.drivers_button.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/settings-4-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/door-8-24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon5)
        self.exit_button.setIconSize(QSize(30, 30))
        self.exit_button.setCheckable(True)
        self.exit_button.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.exit_button)

        self.pushButton_2 = QPushButton(self.sidebar_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(0, 10, 241, 101))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}\n"
"")
        self.main_screen = QWidget(self.centralwidget)
        self.main_screen.setObjectName(u"main_screen")
        self.main_screen.setGeometry(QRect(250, 80, 871, 731))
        self.main_screen.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 851, 711))
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.mainLabel = QLabel(self.main_page)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setGeometry(QRect(320, 10, 151, 71))
        self.mainLabel.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.widget = QWidget(self.main_page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 320, 811, 241))
        self.widget.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.everythingisfine = QLabel(self.widget)
        self.everythingisfine.setObjectName(u"everythingisfine")
        self.everythingisfine.setGeometry(QRect(320, 70, 181, 71))
        self.everythingisfine.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.warningList = QListView(self.widget)
        self.warningList.setObjectName(u"warningList")
        self.warningList.setGeometry(QRect(20, 10, 771, 201))
        self.warningList.setStyleSheet(u"border:none\n"
"")
        self.warningList.raise_()
        self.everythingisfine.raise_()
        self.pushButton = QPushButton(self.main_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 110, 221, 91))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"margin-left: 10px;\n"
"margin-right:10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/bus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(200, 200))
        self.stackedWidget.addWidget(self.main_page)
        self.buses_page = QWidget()
        self.buses_page.setObjectName(u"buses_page")
        self.label_4 = QLabel(self.buses_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 151, 61))
        self.label_4.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_7 = QLabel(self.buses_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 50, 611, 21))
        self.label_7.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(153, 153, 153);")
        self.addBusButton = QPushButton(self.buses_page)
        self.addBusButton.setObjectName(u"addBusButton")
        self.addBusButton.setEnabled(True)
        self.addBusButton.setGeometry(QRect(10, 90, 121, 41))
        self.addBusButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.addBusButton.setCheckable(True)
        self.tableWidget = QTableWidget(self.buses_page)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 140, 851, 571))
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	font-weight:bold;\n"
"}")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.stackedWidget.addWidget(self.buses_page)
        self.routes_page = QWidget()
        self.routes_page.setObjectName(u"routes_page")
        self.label_5 = QLabel(self.routes_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 20, 171, 41))
        self.label_5.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_9 = QLabel(self.routes_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 60, 311, 21))
        self.label_9.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(153, 153, 153);")
        self.mapWidget = QWidget(self.routes_page)
        self.mapWidget.setObjectName(u"mapWidget")
        self.mapWidget.setGeometry(QRect(420, 100, 431, 591))
        self.splitter_2 = QSplitter(self.routes_page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(10, 190, 381, 71))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label_12 = QLabel(self.splitter_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter_2.addWidget(self.label_12)
        self.comboBoxBus = QComboBox(self.splitter_2)
        self.comboBoxBus.setObjectName(u"comboBoxBus")
        self.comboBoxBus.setStyleSheet(u"border:none;\n"
"")
        self.comboBoxBus.setEditable(True)
        self.splitter_2.addWidget(self.comboBoxBus)
        self.splitter_3 = QSplitter(self.routes_page)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setGeometry(QRect(10, 270, 381, 71))
        self.splitter_3.setOrientation(Qt.Vertical)
        self.label_13 = QLabel(self.splitter_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter_3.addWidget(self.label_13)
        self.comboBoxA = QComboBox(self.splitter_3)
        self.comboBoxA.setObjectName(u"comboBoxA")
        self.comboBoxA.setStyleSheet(u"border:none;\n"
"")
        self.comboBoxA.setEditable(True)
        self.comboBoxA.setCurrentText(u"")
        self.splitter_3.addWidget(self.comboBoxA)
        self.splitter_4 = QSplitter(self.routes_page)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(10, 350, 381, 71))
        self.splitter_4.setOrientation(Qt.Vertical)
        self.label_14 = QLabel(self.splitter_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter_4.addWidget(self.label_14)
        self.comboBoxB = QComboBox(self.splitter_4)
        self.comboBoxB.setObjectName(u"comboBoxB")
        self.comboBoxB.setStyleSheet(u"border:none;")
        self.comboBoxB.setEditable(True)
        self.splitter_4.addWidget(self.comboBoxB)
        self.pushButtonRoute = QPushButton(self.routes_page)
        self.pushButtonRoute.setObjectName(u"pushButtonRoute")
        self.pushButtonRoute.setEnabled(True)
        self.pushButtonRoute.setGeometry(QRect(100, 640, 231, 61))
        self.pushButtonRoute.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.pushButtonRoute.setCheckable(True)
        self.splitter = QSplitter(self.routes_page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(10, 110, 381, 71))
        self.splitter.setOrientation(Qt.Vertical)
        self.label_11 = QLabel(self.splitter)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter.addWidget(self.label_11)
        self.comboBoxDriver = QComboBox(self.splitter)
        self.comboBoxDriver.setObjectName(u"comboBoxDriver")
        self.comboBoxDriver.setStyleSheet(u"border:none;\n"
"")
        self.comboBoxDriver.setEditable(True)
        self.splitter.addWidget(self.comboBoxDriver)
        self.pushButtonWayPoints = QPushButton(self.routes_page)
        self.pushButtonWayPoints.setObjectName(u"pushButtonWayPoints")
        self.pushButtonWayPoints.setEnabled(True)
        self.pushButtonWayPoints.setGeometry(QRect(0, 530, 391, 51))
        self.pushButtonWayPoints.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(230, 228, 227);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius:\"10px\"")
        self.pushButtonWayPoints.setCheckable(True)
        self.labelRoute = QLabel(self.routes_page)
        self.labelRoute.setObjectName(u"labelRoute")
        self.labelRoute.setGeometry(QRect(380, 60, 431, 31))
        self.labelCurrentLabel = QLabel(self.routes_page)
        self.labelCurrentLabel.setObjectName(u"labelCurrentLabel")
        self.labelCurrentLabel.setGeometry(QRect(380, 30, 161, 21))
        self.labelCurrentLabel.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.splitter_5 = QSplitter(self.routes_page)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(10, 430, 381, 71))
        self.splitter_5.setOrientation(Qt.Vertical)
        self.label_10 = QLabel(self.splitter_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.splitter_5.addWidget(self.label_10)
        self.dateTimeEdit = QDateTimeEdit(self.splitter_5)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.splitter_5.addWidget(self.dateTimeEdit)
        self.stackedWidget.addWidget(self.routes_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.scheduleTable = QTableWidget(self.schedule_page)
        if (self.scheduleTable.columnCount() < 5):
            self.scheduleTable.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.scheduleTable.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.scheduleTable.setObjectName(u"scheduleTable")
        self.scheduleTable.setGeometry(QRect(0, 300, 851, 411))
        self.label_15 = QLabel(self.schedule_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(370, 0, 121, 41))
        self.label_15.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")
        self.calendarWidget = QCalendarWidget(self.schedule_page)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(130, 40, 581, 171))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.filterButton = QPushButton(self.schedule_page)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setEnabled(True)
        self.filterButton.setGeometry(QRect(360, 240, 121, 51))
        self.filterButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.filterButton.setCheckable(True)
        self.stackedWidget.addWidget(self.schedule_page)
        self.drivers_page = QWidget()
        self.drivers_page.setObjectName(u"drivers_page")
        self.label_6 = QLabel(self.drivers_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 151, 61))
        self.label_6.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_8 = QLabel(self.drivers_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 50, 611, 21))
        self.label_8.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(153, 153, 153);")
        self.addDriverButton = QPushButton(self.drivers_page)
        self.addDriverButton.setObjectName(u"addDriverButton")
        self.addDriverButton.setEnabled(True)
        self.addDriverButton.setGeometry(QRect(10, 90, 121, 41))
        self.addDriverButton.setStyleSheet(u"border:\"none\";\n"
"background-color: rgb(0, 255, 127);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:\"10px\"")
        self.addDriverButton.setCheckable(True)
        self.driverTable = QTableWidget(self.drivers_page)
        if (self.driverTable.columnCount() < 5):
            self.driverTable.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.driverTable.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.driverTable.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.driverTable.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.driverTable.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.driverTable.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.driverTable.setObjectName(u"driverTable")
        self.driverTable.setGeometry(QRect(0, 140, 851, 571))
        self.driverTable.setStyleSheet(u"QHeaderView::section {\n"
"	font-weight:bold;\n"
"}")
        self.driverTable.setAlternatingRowColors(False)
        self.driverTable.setSortingEnabled(False)
        self.driverTable.setColumnCount(5)
        self.driverTable.horizontalHeader().setMinimumSectionSize(49)
        self.driverTable.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.stackedWidget.addWidget(self.drivers_page)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(250, 0, 871, 81))
        self.lineEdit = QLineEdit(self.header)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(580, 30, 281, 31))
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

        self.stackedWidget.setCurrentIndex(0)
        self.comboBoxA.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.schedule_button.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.routes_button.setText(QCoreApplication.translate("MainWindow", u"Routes", None))
        self.bus_button.setText(QCoreApplication.translate("MainWindow", u"Buses", None))
        self.drivers_button.setText(QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bus Managment", None))
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u" Main page", None))
        self.everythingisfine.setText(QCoreApplication.translate("MainWindow", u"Everything is fine", None))
        self.pushButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Buses info", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Welocme to buses information page!", None))
        self.addBusButton.setText(QCoreApplication.translate("MainWindow", u"Add Bus", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Number Plate", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mileage", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Service due to", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Create Route", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Welcome to the page for creating route", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Bus", None))
        self.comboBoxBus.setCurrentText(QCoreApplication.translate("MainWindow", u"Select bus", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Start point", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Finish point", None))
        self.comboBoxB.setCurrentText(QCoreApplication.translate("MainWindow", u"Select current point", None))
        self.pushButtonRoute.setText(QCoreApplication.translate("MainWindow", u"Create ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Driver", None))
        self.comboBoxDriver.setCurrentText(QCoreApplication.translate("MainWindow", u"Select driver", None))
        self.pushButtonWayPoints.setText(QCoreApplication.translate("MainWindow", u"Add way points", None))
        self.labelRoute.setText("")
        self.labelCurrentLabel.setText(QCoreApplication.translate("MainWindow", u"Current route", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start date", None))
        ___qtablewidgetitem5 = self.scheduleTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"From", None));
        ___qtablewidgetitem6 = self.scheduleTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"To", None));
        ___qtablewidgetitem7 = self.scheduleTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Departure", None));
        ___qtablewidgetitem8 = self.scheduleTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Arraival time", None));
        ___qtablewidgetitem9 = self.scheduleTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Drivers info", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Welocme to driver information page!", None))
        self.addDriverButton.setText(QCoreApplication.translate("MainWindow", u"Add driver", None))
        ___qtablewidgetitem10 = self.driverTable.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem11 = self.driverTable.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Second Name", None));
        ___qtablewidgetitem12 = self.driverTable.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"License number", None));
        ___qtablewidgetitem13 = self.driverTable.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem14 = self.driverTable.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hi, Admin!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to Bus Managment", None))
    # retranslateUi

