from PySide6.QtCore import Qt, Signal, QDate, QUrl, QBuffer, QByteArray, QIODevice, QDateTime, QStringListModel
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget,  QTableWidgetItem, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from components.busesDialog import Ui_busesDialog
from ui_index import Ui_MainWindow
from components.busesDialogUpdate import Ui_busesDialogUpdate
from components.driversDialog import Ui_driversDialog
from components.driversDialogUpdate import Ui_driversDialogUpdate
from components.multiSelectDialog import MultiSelectDialog
from components.routeInfoDialog import Ui_Dialog as routeInfoDialog
from script.db_control import *
from script.api import plot_route
import sqlite3
import requests
import json

points = ["Kyiv", "Lviv", "Odesa", "Lutsk", "Zhytomyr"]

current_date_time = QDateTime.currentDateTime()

with open("key.txt", "r") as file:
    api_key = file.read().strip()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Bus Management")
        self.init_db()

        self.check_bus_service_due_to()

        self.bus_button.clicked.connect(self.switch_to_buses_page)
        self.routes_button.clicked.connect(self.switch_to_routes_page)
        self.drivers_button.clicked.connect(self.switch_to_drivers_page)
        self.addBusButton.clicked.connect(self.open_add_bus_dialog)
        self.addDriverButton.clicked.connect(self.open_add_driver_dialog)
        self.pushButtonRoute.clicked.connect(self.create_routes)
        self.pushButtonWayPoints.clicked.connect(self.open_waypoints_dialog)
        self.schedule_button.clicked.connect(self.switch_to_schedule_page)
        self.filterButton.clicked.connect(self.filter_routes)
        self.pushButton_2.clicked.connect(self.switch_to_main_page)

        self.dateTimeEdit.setDateTime(current_date_time.addDays(10))
        self.dateTimeEdit.setMinimumDateTime(current_date_time)

        self.labelRoute.setText("Select start point --> Select finish point")
        self.labelRoute.setStyleSheet("font-size: 20px; font-weight: bold; ")
        
        self.selected_items = []

        self.load_buses_data()
        self.load_driver_data()
        self.load_route_data()
        

        self.comboBoxA.addItems(points)
        self.comboBoxB.addItems(points)
        self.comboBoxA.setCurrentText('Select start point')
        self.comboBoxB.setCurrentText('Select finish point')

        self.comboBoxA.currentIndexChanged.connect(self.route_label_changed)
        self.comboBoxB.currentIndexChanged.connect(self.route_label_changed)

        

    def switch_to_main_page(self):
        self.check_bus_service_due_to()
        self.stackedWidget.setCurrentIndex(0)


    def switch_to_buses_page(self):
        print("Switching to buses page")
        self.stackedWidget.setCurrentIndex(1)
        self.load_buses_data()
    
    def switch_to_routes_page(self):
        print("Switching to routes page")
        self.stackedWidget.setCurrentIndex(2)
    
    def switch_to_drivers_page(self):
        print("Switching to drivers page")
        self.stackedWidget.setCurrentIndex(4)
        self.load_driver_data()

    def switch_to_schedule_page(self):
        print("Switching to schedule page")
        self.stackedWidget.setCurrentIndex(3)
        self.load_route_data()

    def open_add_bus_dialog(self):
        dialog = BusesDialog(self)
        dialog.exec()
        self.load_buses_data()

    def open_add_driver_dialog(self):
        dialog = DriversDialog(self)
        dialog.exec()
        self.load_driver_data()

    def init_db(self):
        create_db()

    def load_buses_data(self):
        rows = load_bus()

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
        

        self.comboBoxBus.clear()
        for row in rows:
            bus_id = row[0]
            bus_model = row[1]
            self.comboBoxBus.addItem(bus_model, bus_id)  
    
    def load_driver_data(self):
        rows = load_driver()

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

        self.comboBoxDriver.clear()
        for row in rows:
            driver_id = row[0]
            driver_name = row[1] + ' ' + row[2]
            self.comboBoxDriver.addItem(driver_name, driver_id)

    def check_bus_service_due_to(self):
        conn = sqlite3.connect("bus_management.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, model, number_plate, service_due_to FROM Buses")
        overdue_buses = []

        for row in cursor.fetchall():
            bus_id, model, number_plate, service_due_to = row
            service_due_date = service_due_to
        
            if service_due_date < current_date_time.toString("yyyy-MM-dd"):
                self.everythingisfine.setVisible(False)
                overdue_buses.append(f"Service is out of date for bus {model} with number plate {number_plate}")

        model = QStringListModel()
        model.setStringList(overdue_buses)
        self.warningList.setModel(model)
        print(overdue_buses)  


    def load_route_data(self):

        self.scheduleTable.setColumnWidth(0, 150)
        self.scheduleTable.setColumnWidth(1, 150)
        self.scheduleTable.setColumnWidth(2, 150)
        self.scheduleTable.setColumnWidth(3, 150)
        self.scheduleTable.setColumnWidth(4, 150)

        rows = load_schedule()

        self.scheduleTable.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data[1:]):
                self.scheduleTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

                double_button_widget = DoubleButtonWidgetRoute(row_idx, row_data)
                double_button_widget.info_clicked.connect(self.load_route_data)
                double_button_widget.delete_clicked.connect(self.load_route_data)
                self.scheduleTable.setCellWidget(row_idx, 4, double_button_widget)

    def open_waypoints_dialog(self):
        dialog = MultiSelectDialog(points)
        if dialog.exec() == QDialog.Accepted:
            self.selected_items = dialog.get_selected_items()
            self.route_label_changed()
           
    def route_label_changed(self):
        waypoints_string = " "
        if self.selected_items:
            waypoints_string = f"--> {' --> '.join(self.selected_items)} "
        labelText = f"{self.comboBoxA.currentText()} {waypoints_string} --> {self.comboBoxB.currentText()}"
        self.labelRoute.setText(labelText)
        print(labelText)

    def create_routes(self):
        load_bus()
        load_driver()

        driver_id = self.comboBoxDriver.currentData()
        bus_id = self.comboBoxBus.currentData()
        point_a = self.comboBoxA.currentText()
        point_b = self.comboBoxB.currentText()
        start_date = self.dateTimeEdit.dateTime().toString("yyyy-MM-dd HH:mm")
        way_points = []

        bus_info = load_bus_by_id(driver_id)

        service_due_to = bus_info[4]

        if not driver_id:
            QMessageBox.warning(self, "Input Error", "Please select a driver.")
        elif not bus_id:
            QMessageBox.warning(self, "Input Error", "Please select a bus.")
        elif not point_a:
            QMessageBox.warning(self, "Input Error", "Please select start point.")
        elif not point_b:
            QMessageBox.warning(self, "Input Error", "Please select finish point.")
        elif not start_date:
            QMessageBox.warning(self, "Input Error", "Please select a start date.")
        elif point_a == point_b:
            QMessageBox.warning(self, "Input Error", "Start and Finish cannot be the same.")
        elif service_due_to < current_date_time.toString("yyyy-MM-dd"):
            QMessageBox.warning(self, "Input Error", "The selected bus is not available for this route. Because it is out of service.")
        else:

            cities = self.selected_items
            self.selected_items = []

            
            if point_a == "Kyiv":
                cordinates_a_lat, cordinates_a_lng = 50.4501, 30.523
            elif point_a == "Lviv":
                cordinates_a_lat, cordinates_a_lng = 49.8397, 24.0297
            elif point_a == "Odesa":
                cordinates_a_lat, cordinates_a_lng = 46.4825, 30.7233
            elif point_a == "Lutsk":
                cordinates_a_lat, cordinates_a_lng = 50.7472, 25.3254
            elif point_a == "Zhytomyr":
                cordinates_a_lat, cordinates_a_lng = 50.2547, 28.6587
            
            if point_b == "Kyiv":
                cordinates_b_lat, cordinates_b_lng = 50.4501, 30.523
            elif point_b == "Lviv":
                cordinates_b_lat, cordinates_b_lng = 49.8397, 24.0297
            elif point_b == "Odesa":
                cordinates_b_lat, cordinates_b_lng = 46.4825, 30.7233
            elif point_b == "Lutsk":
                cordinates_b_lat, cordinates_b_lng = 50.7472, 25.3254
            elif point_b == "Zhytomyr":
                cordinates_b_lat, cordinates_b_lng = 50.2547, 28.6587


            for city in cities:
                if city == "Kyiv":
                    way_points.append([50.4501, 30.523])
                elif city == "Lviv":
                    way_points.append([49.8397, 24.0297])
                elif city == "Odesa":
                    way_points.append([46.4825, 30.7233])
                elif city == "Lutsk":
                    way_points.append([50.7472, 25.3254])
                elif city == "Zhytomyr":
                    way_points.append([50.2547, 28.6587])
            

            distance, time, points = plot_route(api_key, cordinates_a_lat, cordinates_a_lng, cordinates_b_lat, cordinates_b_lng, way_points)

            arraival_date = self.dateTimeEdit.dateTime().addSecs(time).toString("yyyy-MM-dd HH:mm")

            if is_driver_busy(driver_id, start_date, arraival_date):
                QMessageBox.warning(self, "Scheduling Error", "The selected driver is already assigned to a route in this period.")
                return
            if is_bus_busy(bus_id, start_date, arraival_date):
                QMessageBox.warning(self, "Scheduling Error", "The selected bus is already assigned to a route in this period.")
                return

            html_content = generate_html(api_key, cordinates_a_lat, cordinates_a_lng, cordinates_b_lat, cordinates_b_lng, way_points)

            if not self.mapWidget.layout():
                layout = QVBoxLayout(self.mapWidget)
                self.mapWidget.setLayout(layout)
            else:
                layout = self.mapWidget.layout()

            for i in reversed(range(layout.count())):
                widget_to_remove = layout.itemAt(i).widget()
                if isinstance(widget_to_remove, QWebEngineView):
                    layout.removeWidget(widget_to_remove)
                    widget_to_remove.deleteLater()  

            web_view = QWebEngineView()

            buffer = QBuffer()
            buffer.setData(QByteArray(html_content.encode()))
            buffer.open(QIODevice.ReadOnly)

            web_view.setHtml(buffer.readAll().data().decode())

            cities_json = json.dumps(cities)

            layout.addWidget(web_view)

            print(cities_json)
            add_route(bus_id, driver_id, start_date, arraival_date, point_a, point_b, distance, time, html_content, cities_json)


    def filter_routes(self):
        """Фільтрує таблицю, залишаючи тільки рядки з вибраною датою."""
        selected_date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")

        for row in range(self.scheduleTable.rowCount()):

            row_date_time = self.scheduleTable.item(row, 2).text()

            row_date = row_date_time.split(" ")[0]

            if row_date == selected_date:
                self.scheduleTable.setRowHidden(row, False)
            else:
                self.scheduleTable.setRowHidden(row, True)



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

        add_bus(model, number_plate, mileage, service_due_to)

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

        add_driver(first_name, second_name, license_number, phone)

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

class DoubleButtonWidgetRoute(QWidget):
    def __init__(self, row_idx, row_data):
        super().__init__()
        self.row_idx = row_idx
        self.row_data = row_data
        self.init_ui()
    
    info_clicked = Signal(int)  
    delete_clicked = Signal(int)  

    def init_ui(self):
        self.info_button = QPushButton()
        self.delete_button = QPushButton()
        self.info_button.setIcon(QIcon(":/icons/info-32.png"))
        self.delete_button.setIcon(QIcon(":/icons/delete-24.png"))
        self.info_button.setStyleSheet("""
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
        self.info_button.setMinimumSize(50, 20)  
        self.info_button.setMaximumSize(50, 20)  
        self.delete_button.setMinimumSize(50, 20)  
        self.delete_button.setMaximumSize(50, 20)

        self.info_button.clicked.connect(self.info_dialog_open)
        self.delete_button.clicked.connect(self.delete_row)

        layout = QHBoxLayout()
        layout.addWidget(self.info_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def info_dialog_open(self):
        route_id = self.row_data[0]  # Extract route ID
        dialog = RouteinfoDialog(route_id)  # Pass route ID to dialog
        dialog.exec()

    def delete_row(self):
        reply = QMessageBox.question(self, 'Delete Record',
                                     "Are you sure you want to delete this record?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            conn = sqlite3.connect('bus_management.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Route WHERE id = ?", (self.row_data[0],))
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
            delete_driver(self.row_data[0])
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

        update_bus(self.row_data[0], model, number_plate, mileage, service_due_to)

        self.accept()  

class RouteinfoDialog(QDialog, routeInfoDialog):
    def __init__(self, route_id, parent=None):
        super(RouteinfoDialog, self).__init__(parent)
        self.setupUi(self)
        self.route_id = route_id

        route = load_route_by_id(self.route_id)
        driver_id = route[2]
        bus_id = route[1]

        html_route = route[9]

        driver = load_driver_by_id(driver_id)
        bus = load_bus_by_id(bus_id)

        self.label_11.setText(f"Driver: {driver[1]} {driver[2]}")
        self.label_12.setText(f"Bus: {bus[1]} {bus[2]}")
        self.label_13.setText(f"Departure Date: {route[3]}")
        self.label_14.setText(f"Arrival Date: {route[4]}")
        self.label_15.setText(f"Time in road: {seconds_to_hours_minutes(int(route[8]))}")
        self.labelRoute.setStyleSheet("font-size: 16px; font-weight: bold;")

        waypoints = json.loads(route[10])

        
        waypoints_string = " "
        if waypoints != []:
                waypoints_string = f"--> {' --> '.join(waypoints)} "
        labelText = f"{route[5]} {waypoints_string} --> {route[6]}"
        self.labelRoute.setText(labelText)



        if not self.mapWidget.layout():
                layout = QVBoxLayout(self.mapWidget)
                self.mapWidget.setLayout(layout)
        else:
                layout = self.mapWidget.layout()

        for i in reversed(range(layout.count())):
                widget_to_remove = layout.itemAt(i).widget()
                if isinstance(widget_to_remove, QWebEngineView):
                    layout.removeWidget(widget_to_remove)
                    widget_to_remove.deleteLater()  

        web_view = QWebEngineView()

        buffer = QBuffer()
        buffer.setData(QByteArray(html_route.encode()))
        buffer.open(QIODevice.ReadOnly)

        web_view.setHtml(buffer.readAll().data().decode())

        layout.addWidget(web_view)

def seconds_to_hours_minutes(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours} hours {minutes} minutes"


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

        update_driver(self.row_data[0], first_name, second_name, license_number, phone)

        self.accept()

def generate_html(api_key, origin_lat, origin_lng, dest_lat, dest_lng, waypoints=None):

    waypoints_param = ""
    if waypoints:
        waypoints_param = "&waypoints=" + "|".join([f"{lat},{lng}" for lat, lng in waypoints])


    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Google Maps Route</title>
        <style>
        html, body {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}
        iframe {{
            width: 100%;
            height: 100%;
            border: 0;
        }}
        </style>
    </head>
    <body>
        <iframe
        width="100%"
        height="100%"
        frameborder="0" style="border:0"
        src="https://www.google.com/maps/embed/v1/directions?key={api_key}&origin={origin_lat},{origin_lng}&destination={dest_lat},{dest_lng}&mode=driving{waypoints_param}&zoom=7"
        allowfullscreen>
        </iframe>
    </body>
    </html>
    """
    return html_content


