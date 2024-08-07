import sqlite3

conn = sqlite3.connect('college.sqlite3')

cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL)
    """)
    conn.commit()

create_table()

def insert(name, email, address):
    cursor.execute("""
    INSERT INTO students(name, email, address)            
    VALUES(?, ?, ?)""", (name, email, address))
    conn.commit()

insert('Sophia', 'sophia@gmail.com', 'ktm')

conn.close()
