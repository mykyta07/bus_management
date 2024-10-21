from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget,  QTableWidgetItem, QDialog, QPushButton, QHBoxLayout
from PySide6.QtGui import QAction, QIcon
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

        # Set column widths
        self.tableWidget.setColumnWidth(0, 150)  # Width for 'model' column
        self.tableWidget.setColumnWidth(1, 150)  # Width for 'number_plate' column
        self.tableWidget.setColumnWidth(2, 100)  # Width for 'mileage' column
        self.tableWidget.setColumnWidth(3, 150)  # Width for 'service_due_to' column
        self.tableWidget.setColumnWidth(4, 150)  # Width for 'buttons' column

        self.tableWidget.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                
                
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

                double_button_widget = DoubleButtonWidget(row_idx, row_data)
                self.tableWidget.setCellWidget(row_idx, 4, double_button_widget)


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

class DoubleButtonWidget(QWidget):
    def __init__(self, row_idx, row_data):
        super().__init__()
        self.row_idx = row_idx
        self.row_data = row_data
        self.init_ui()

    def init_ui(self):
        self.edit_button = QPushButton()
        self.delete_button = QPushButton()
        self.edit_button.setIcon(QIcon(":/icons/edit-3-24.png"))
        self.delete_button.setIcon(QIcon(":/icons/delete-24.png"))
        self.edit_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QPushButton:pressed {
                background-color: #333;
            }
        """)
        self.delete_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 5px 10px;
            }
            QPushButton:pressed {
                background-color: #cc0000;
            }
        """)
        self.edit_button.setMinimumSize(50, 20)  # Minimum size
        self.edit_button.setMaximumSize(50, 20)  # Maximum size
        self.delete_button.setMinimumSize(50, 20)  # Minimum size
        self.delete_button.setMaximumSize(50, 20)

        # Connect buttons to their respective slot methods
        self.edit_button.clicked.connect(self.edit_row)
        self.delete_button.clicked.connect(self.delete_row)

        # Layout to arrange buttons horizontally
        layout = QHBoxLayout()
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def edit_row(self):
        print("Editing row", self.row_idx)

    def delete_row(self):
        print("Deleting row", self.row_idx)
