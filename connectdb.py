import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('database.sqlite')
c = conn.cursor()

# Create table
c.execute('''
    CREATE TABLE health_data (
        age INTEGER,
        cholesterol_level INTEGER,
        blood_pressure INTEGER
    )
''')

# Open the CSV file and insert its data into the database
with open('dataset20231130.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        c.execute('''
            INSERT INTO health_data (age, cholesterol_level, blood_pressure)
            VALUES (?, ?, ?)
        ''', (row['age'], row['cholesterol level'], row['blood pressure']))

# Commit the changes and close the connection
conn.commit()
conn.close()