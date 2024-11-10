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
            arrival_date TEXT,
            point_a TEXT,
            point_b TEXT,
            distance REAL,
            time TEXT,
            html_report TEXT,
            waypoints TEXT,
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

def load_schedule():
    create_db()
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT Route.id, Route.point_a, Route.point_b, Route.departure_date, Route.arrival_date
        FROM Route
        JOIN Buses ON Route.bus_id = Buses.id
        JOIN Drivers ON Route.driver_id = Drivers.id
    ''')
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

def add_route(bus_id, driver_id, departure_date, arrival_date, point_a, point_b, distance, time, html_report, waypoints):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Route (bus_id, driver_id, departure_date, arrival_date, point_a, point_b, distance, time, html_report, waypoints)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (bus_id, driver_id, departure_date, arrival_date, point_a, point_b, distance, time, html_report, waypoints))
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

def is_driver_busy(driver_id, start_date, end_date):
    """
    Перевіряє, чи зайнятий водій у вказаний період.
    Повертає True, якщо водій зайнятий, інакше - False.
    """
    conn = sqlite3.connect('bus_management.db') 
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) FROM Route
    WHERE driver_id = ?
    AND (
        (departure_date <= ? AND arrival_date >= ?) OR  -- Перетин на початку
        (departure_date <= ? AND arrival_date >= ?) OR  -- Перетин на кінці
        (departure_date >= ? AND arrival_date <= ?)     -- Повністю всередині періоду
    )
    """
    cursor.execute(query, (driver_id, start_date, start_date, end_date, end_date, start_date, end_date))
    
    count = cursor.fetchone()[0]  
    conn.close()  
    
    return count > 0

def is_bus_busy(bus_id, start_date, end_date):
    """
    Перевіряє, чи зайнятий автобус у вказаний період.
    Повертає True, якщо автобус зайнятий, інакше - False.
    """
    conn = sqlite3.connect('bus_management.db')  
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) FROM Route
    WHERE bus_id = ?
    AND (
        (departure_date <= ? AND arrival_date >= ?) OR  -- Перетин на початку
        (departure_date <= ? AND arrival_date >= ?) OR  -- Перетин на кінці
        (departure_date >= ? AND arrival_date <= ?)     -- Повністю всередині періоду
    )
    """
    cursor.execute(query, (bus_id, start_date, start_date, end_date, end_date, start_date, end_date))
    
    count = cursor.fetchone()[0] 
    conn.close()  
    
    return count > 0

def load_route_by_id(route_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Route WHERE id = ?
    ''', (route_id,))
    route = cursor.fetchone()
    conn.close()
    return route

def load_driver_by_id(driver_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Drivers WHERE id = ?
    ''', (driver_id,))
    driver = cursor.fetchone()
    conn.close()
    return driver

def load_bus_by_id(bus_id):
    conn = sqlite3.connect('bus_management.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Buses WHERE id = ?
    ''', (bus_id,))
    bus = cursor.fetchone()
    conn.close()
    return bus



