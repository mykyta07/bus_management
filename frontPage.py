from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget,  QTableWidgetItem, QDialog
from PySide6.QtGui import QAction
from busesDialog import Ui_busesDialog
from ui_index import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bus Management")

        self.bus_button.clicked.connect(self.switch_to_buses_page)
        self.routes_button.clicked.connect(self.switch_to_routes_page)
        self.drivers_button.clicked.connect(self.switch_to_drivers_page)
        self.addBusButton.clicked.connect(self.open_add_bus_dialog)
        self.load_buses_data()

    def switch_to_buses_page(self):
        print("Switching to buses page")
        self.stackedWidget.setCurrentIndex(0)
        self.load_buses_data()
    
    def switch_to_routes_page(self):
        print("Switching to routes page")
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_drivers_page(self):
        print("Switching to drivers page")
        self.stackedWidget.setCurrentIndex(2)

    def open_add_bus_dialog(self):
        dialog = BusesDialog(self)
        dialog.exec()
        self.load_buses_data()

    def init_db(self):
        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Buses (
                id INTEGER PRIMARY KEY,
                model TEXT,
                number_plate TEXT,
                mileage INTEGER,
                service_due_to TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def load_buses_data(self):
        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT model, number_plate, mileage, service_due_to FROM Buses")
        rows = cursor.fetchall()
        conn.close()

        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                print(f"Setting item at ({row_idx}, {col_idx}): {col_data}")  # Debugging print statement
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

class BusesDialog(QDialog, Ui_busesDialog):
    def __init__(self, parent=None):
        super(BusesDialog, self).__init__(parent)
        self.setupUi(self)  # This is how you set up the UI

        self.pushButton.clicked.connect(self.submit_data)
        self.pushButton_2.clicked.connect(self.reject)

    def submit_data(self):
        model = self.lineEdit.text()
        number_plate = self.lineEdit_2.text()
        mileage = self.spinBox.value()
        service_due_to = self.dateEdit.date().toString("yyyy-MM-dd")

        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Buses (model, number_plate, mileage, service_due_to)
            VALUES (?, ?, ?, ?)
        ''', (model, number_plate, mileage, service_due_to))
        conn.commit()
        conn.close()

        self.accept()