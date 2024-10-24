import sqlite3

class BusManagementDB:
    def __init__(self, db_name='bus_management.db'):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create the Buses table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Buses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                number_plate TEXT,
                mileage INTEGER,
                service_due_to TEXT
            )
        ''')

        # Create the Driver table if it doesn't already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Drivers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                license_number TEXT,
                phone TEXT
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

    # Method to add a bus
    def add_bus(self, model, number_plate, mileage, service_due_to):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Insert a new bus record into the Buses table
        cursor.execute('''
            INSERT INTO Buses (model, number_plate, mileage, service_due_to)
            VALUES (?, ?, ?, ?)
        ''', (model, number_plate, mileage, service_due_to))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    # Method to get all buses
    def get_all_buses(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Fetch all records from the Buses table
        cursor.execute('SELECT * FROM Buses')
        buses = cursor.fetchall()

        # Close the connection
        conn.close()

        return buses

    # Method to add a driver
    def add_driver(self, first_name, last_name, license_number, phone):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Insert a new driver record into the Driver table
        cursor.execute('''
            INSERT INTO Drivers (first_name, last_name, license_number, phone)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, license_number, phone))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

    # Method to get all drivers
    def get_all_drivers(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Fetch all records from the Driver table
        cursor.execute('SELECT * FROM Driver')
        drivers = cursor.fetchall()

        # Close the connection
        conn.close()

        return drivers

# Script to create the database, add sample data, and retrieve the data
if __name__ == "__main__":
    # Initialize the database
    db = BusManagementDB()

    # Add sample buses
    db.add_bus("Mercedes-Benz", "ABC123", 50000, "2024-11-01")
    db.add_bus("Volvo", "XYZ456", 75000, "2024-12-15")
    db.add_bus("Scania", "LMN789", 30000, "2025-01-20")

    # Add sample drivers
    db.add_driver("John", "Doe", "DL12345", "555-1234")
    db.add_driver("Jane", "Smith", "DL54321", "555-5678")
    db.add_driver("Mike", "Johnson", "DL98765", "555-8765")

    