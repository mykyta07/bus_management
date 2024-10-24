from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget,  QTableWidgetItem, QDialog, QPushButton, QHBoxLayout, QMessageBox
from PySide6.QtGui import QAction, QIcon
from busesDialog import Ui_busesDialog
from ui_index import Ui_MainWindow
from busesDialogUpdate import Ui_busesDialogUpdate
from driversDialog import Ui_driversDialog
from driversDialogUpdate import Ui_driversDialogUpdate
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
        self.addDriverButton.clicked.connect(self.open_add_driver_dialog)
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
        self.load_driver_data()

    def open_add_bus_dialog(self):
        dialog = BusesDialog(self)
        dialog.exec()
        self.load_buses_data()

    def open_add_driver_dialog(self):
        dialog = DriversDialog(self)
        dialog.exec()
        self.load_driver_data()

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
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Driver (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                license_number TEXT,
                phone TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def load_buses_data(self):
        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, model, number_plate, mileage, service_due_to FROM Buses")
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
            for col_idx, col_data in enumerate(row_data[1:]):
                
                
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

                double_button_widget = DoubleButtonWidget(row_idx, row_data)
                double_button_widget.edit_clicked.connect(self.load_buses_data)
                double_button_widget.delete_clicked.connect(self.load_buses_data)
                self.tableWidget.setCellWidget(row_idx, 4, double_button_widget)
    
    def load_driver_data(self):
        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Drivers")
        rows = cursor.fetchall()
        conn.close()

        # Set column widths
        self.driverTable.setColumnWidth(0, 150)
        self.driverTable.setColumnWidth(1, 150)
        self.driverTable.setColumnWidth(2, 150)
        self.driverTable.setColumnWidth(3, 150)
        self.driverTable.setColumnWidth(4, 150)
        

        self.driverTable.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data[1:]):
                self.driverTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

                double_button_widget = DoubleButtonWidgetDrivers(row_idx, row_data)
                double_button_widget.edit_clicked.connect(self.load_driver_data)
                double_button_widget.delete_clicked.connect(self.load_driver_data)
                self.driverTable.setCellWidget(row_idx, 4, double_button_widget)



class BusesDialog(QDialog, Ui_busesDialog):
    def __init__(self, parent=None):
        super(BusesDialog, self).__init__(parent)
        self.setupUi(self)  

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

class DriversDialog(QDialog, Ui_driversDialog):
    def __init__(self, parent=None):
        super(DriversDialog, self).__init__(parent)
        self.setupUi(self)  

        self.pushButton.clicked.connect(self.submit_data)
        self.pushButton_2.clicked.connect(self.reject)

    def submit_data(self):
        first_name = self.lineEdit.text()
        second_name = self.lineEdit_2.text()
        license_number = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()

        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Drivers (first_name, last_name, license_number, phone)
            VALUES (?, ?, ?, ?)
        ''', (first_name, second_name, license_number, phone))
        conn.commit()
        conn.close()

        self.accept()

class DoubleButtonWidget(QWidget):
    def __init__(self, row_idx, row_data):
        super().__init__()
        self.row_idx = row_idx
        self.row_data = row_data
        self.init_ui()
    
    edit_clicked = Signal(int)  # Signal for edit button clicked
    delete_clicked = Signal(int)  # Signal for delete button clicked

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
        self.edit_button.setMinimumSize(50, 20)  
        self.edit_button.setMaximumSize(50, 20)  
        self.delete_button.setMinimumSize(50, 20)  
        self.delete_button.setMaximumSize(50, 20)

        self.edit_button.clicked.connect(self.edit_row)
        self.delete_button.clicked.connect(self.delete_row)

        layout = QHBoxLayout()
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def edit_row(self):
        dialog = BusesDialogUpdate(self.row_data)  # Передаємо дані автобуса у діалогове вікно
        if dialog.exec():
            self.edit_clicked.emit(self.row_idx)  # Викликаємо сигнал для оновлення таблиці після редагування

    def delete_row(self):
        reply = QMessageBox.question(self, 'Delete Record',
                                     "Are you sure you want to delete this record?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect('bus_management.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Buses WHERE id = ?", (self.row_data[0],))
            conn.commit()
            conn.close() 
            self.delete_clicked.emit(self.row_idx)  


class DoubleButtonWidgetDrivers(DoubleButtonWidget):
    def __init__(self, row_idx, row_data, parent=None):
        super().__init__(row_idx, row_data)
        self.parent = parent

    def edit_row(self):
        dialog = DriversDialogUpdate(self.row_data)
        if dialog.exec():
            self.edit_clicked.emit(self.row_idx)

    def delete_row(self): 
        reply = QMessageBox.question(self, 'Delete Record',
                                     "Are you sure you want to delete this record?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect('bus_management.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Drivers WHERE id = ?", (self.row_data[0],))
            conn.commit()
            conn.close() 
            self.delete_clicked.emit(self.row_idx)
    

class BusesDialogUpdate(QDialog, Ui_busesDialogUpdate):
    def __init__(self, row_data, parent=None):
        super(BusesDialogUpdate, self).__init__(parent)
        self.setupUi(self)
        self.row_data = row_data  


        self.lineEdit.setText(self.row_data[1]) 
        self.lineEdit_2.setText(self.row_data[2]) 
        self.spinBox.setValue(self.row_data[3])  
        self.dateEdit.setDate(QDate.fromString(self.row_data[4], "yyyy-MM-dd"))  # service_due_to

        self.UpdateBusButton.clicked.connect(self.update_data)
        self.CancelUpdateButton.clicked.connect(self.reject)

    def update_data(self):
        model = self.lineEdit.text()
        number_plate = self.lineEdit_2.text()
        mileage = self.spinBox.value()
        service_due_to = self.dateEdit.date().toString("yyyy-MM-dd")

        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Buses 
            SET model = ?, number_plate = ?, mileage = ?, service_due_to = ?
            WHERE id = ?
        ''', (model, number_plate, mileage, service_due_to, self.row_data[0]))
        conn.commit()
        conn.close()

        self.accept()  



class DriversDialogUpdate(QDialog, Ui_driversDialogUpdate):
    def __init__(self, row_data, parent=None):
        super(DriversDialogUpdate, self).__init__(parent)
        self.setupUi(self)
        self.row_data = row_data  


        self.lineEdit.setText(self.row_data[1]) 
        self.lineEdit_2.setText(self.row_data[2]) 
        self.lineEdit_3.setText(self.row_data[3]) 
        self.lineEdit_4.setText(self.row_data[4]) 

        self.pushButton.clicked.connect(self.update_data)
        self.pushButton_2.clicked.connect(self.reject)

    def update_data(self):
        first_name = self.lineEdit.text()
        second_name = self.lineEdit_2.text()
        license_number = self.lineEdit_3.text()
        phone = self.lineEdit_4.text()

        conn = sqlite3.connect('bus_management.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Drivers 
            SET first_name = ?, last_name = ?, license_number = ?, phone = ?
            WHERE id = ?
        ''', (first_name, second_name, license_number, phone, self.row_data[0]))
        conn.commit()
        conn.close()

        self.accept()

