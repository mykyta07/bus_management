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
                id INTEGER PRIMARY KEY,
                model TEXT,
                number_plate TEXT,
                mileage INTEGER,
                service_due_to TEXT
            )
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

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

    def get_all_buses(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Fetch all records from the Buses table
        cursor.execute('SELECT * FROM Buses')
        buses = cursor.fetchall()

        # Close the connection
        conn.close()

        return buses

# Script to create the database and add sample data
if __name__ == "__main__":
    # Initialize the database
    db = BusManagementDB()

    # Add sample buses
    db.add_bus("Mercedes-Benz", "ABC123", 50000, "2024-11-01")
    db.add_bus("Volvo", "XYZ456", 75000, "2024-12-15")
    db.add_bus("Scania", "LMN789", 30000, "2025-01-20")

    # Retrieve and display all buses
    buses = db.get_all_buses()
    for bus in buses:
        print(f"ID: {bus[0]}, Model: {bus[1]}, Number Plate: {bus[2]}, Mileage: {bus[3]}, Service Due To: {bus[4]}")
