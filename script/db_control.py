import sqlite3

def create_db():
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
            CREATE TABLE IF NOT EXISTS Drivers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                license_number TEXT,
                phone TEXT
            )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Route (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bus_id INTEGER,
            driver_id INTEGER,
            departure_date TEXT,
            distance REAL,
            time TEXT,
            html_report TEXT,
            FOREIGN KEY (bus_id) REFERENCES Buses(id),
            FOREIGN KEY (driver_id) REFERENCES Driver(id)
        )
    ''')
        conn.commit()
        conn.close()

def load_bus():
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, model, number_plate, mileage, service_due_to FROM Buses")
    rows = cursor.fetchall()
    conn.close()
    return rows

def load_driver():
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Drivers")
    rows = cursor.fetchall()
    conn.close()
    return rows

def load_route():
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Route")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_bus(model, number_plate, mileage, service_due_to):
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Buses (model, number_plate, mileage, service_due_to)
        VALUES (?, ?, ?, ?)
    ''', (model, number_plate, mileage, service_due_to))
    conn.commit()
    conn.close()

def add_driver(first_name, last_name, license_number, phone):
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Drivers (first_name, last_name, license_number, phone)
        VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, license_number, phone))
    conn.commit()
    conn.close()

def add_route(bus_id, driver_id, departure_date, distance, time, html_report):
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Route (bus_id, driver_id, departure_date, distance, time, html_report)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (bus_id, driver_id, departure_date, distance, time, html_report))
    conn.commit()
    conn.close()

def delete_bus(bus_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Buses WHERE id = ?
    ''', (bus_id,))
    conn.commit()
    conn.close()

def delete_driver(driver_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Drivers WHERE id = ?
    ''', (driver_id,))
    conn.commit()
    conn.close()

def delete_route(route_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM Route WHERE id = ?
    ''', (route_id,))
    conn.commit()
    conn.close()

def update_bus(bus_id, model, number_plate, mileage, service_due_to):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Buses
        SET model = ?, number_plate = ?, mileage = ?, service_due_to = ?
        WHERE id = ?
    ''', (model, number_plate, mileage, service_due_to, bus_id))
    conn.commit()
    conn.close()

def update_driver(driver_id, first_name, last_name, license_number, phone):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Drivers
        SET first_name = ?, last_name = ?, license_number = ?, phone = ?
        WHERE id = ?
    ''', (first_name, last_name, license_number, phone, driver_id))
    conn.commit()
    conn.close()

