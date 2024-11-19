import sqlite3

# Підключення до бази даних (створення файлу, якщо його не існує)
conn = sqlite3.connect('bus_management.db')
cursor = conn.cursor()

# Створення таблиць
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

# Дані для заповнення таблиць
buses_data = [
    (1, "Mercedes-Benz Sprinter", "AB1234CD", 120000, "2025-05-01"),
    (2, "Ford Transit", "XY5678EF", 80000, "2025-03-15"),
    (3, "Volkswagen Crafter", "GH9012IJ", 95000, "2025-07-10"),
    (4, "Renault Master", "KL3456MN", 110000, "2025-04-20"),
    (5, "Peugeot Boxer", "OP7890QR", 70000, "2025-08-30"),
    (6, "Citroën Jumper", "ST1234UV", 85000, "2025-06-05"),
    (7, "Iveco Daily", "WX5678YZ", 140000, "2025-01-12"),
    (8, "Fiat Ducato", "AB3456CD", 60000, "2025-09-01"),
    (9, "Hyundai H350", "EF7890GH", 75000, "2025-10-25"),
    (10, "Toyota HiAce", "IJ1234KL", 130000, "2025-11-15")
]

drivers_data = [
    ("John", "Doe", "D12345678", "+123456789"),
    ("Jane", "Smith", "D87654321", "+987654321"),
    ("Robert", "Johnson", "D23456789", "+112233445"),
    ("Emily", "Davis", "D34567890", "+223344556"),
    ("Michael", "Brown", "D45678901", "+334455667"),
    ("Sarah", "Jones", "D56789012", "+445566778"),
    ("William", "Garcia", "D67890123", "+556677889"),
    ("Linda", "Martinez", "D78901234", "+667788990"),
    ("James", "Rodriguez", "D89012345", "+778899001"),
    ("Elizabeth", "Hernandez", "D90123456", "+889900112")
]

# Додавання записів у таблиці
cursor.executemany('''
    INSERT INTO Buses (id, model, number_plate, mileage, service_due_to)
    VALUES (?, ?, ?, ?, ?)
''', buses_data)

cursor.executemany('''
    INSERT INTO Drivers (first_name, last_name, license_number, phone)
    VALUES (?, ?, ?, ?)
''', drivers_data)

# Збереження змін і закриття підключення
conn.commit()
conn.close()

print("Таблиці успішно заповнені.")
