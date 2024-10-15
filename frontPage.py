from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget
from PySide6.QtGui import QAction
from ui_index import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bus Management")

        self.bus_button.clicked.connect(self.switch_to_buses_page)
        self.routes_button.clicked.connect(self.switch_to_routes_page)
        self.drivers_button.clicked.connect(self.switch_to_drivers_page)

    def switch_to_buses_page(self):
        print("Switching to buses page")
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_routes_page(self):
        print("Switching to routes page")
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_drivers_page(self):
        print("Switching to drivers page")
        self.stackedWidget.setCurrentIndex(2)