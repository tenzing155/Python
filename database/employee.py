import sqlite3

conn = sqlite3.connect('employee.sqlite3')
cursor = conn.cursor()

def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age TEXT NOT NULL,
    gender TEXT NOT NULL
    )                       
    """)
    conn.commit()

create_table()

def insert():
    cursor.execute("""
    INSERT INTO employee(name, age, gender)
    VALUES(?, ?, ?)""", ("ram", "18", "male"))
    conn.commit()

insert()

def update_employee(employee_id, name, age, gender):
    cursor.execute("""
    UPDATE employee
    SET name = ?, age = ?, gender = ?
    WHERE employee_id = ?""", (name, age, gender, employee_id))
    conn.commit()

update_employee(1, "hari", "20", "male")

# def delete_table():
#     cursor.execute("DROP TABLE IF EXISTS employee")
#     conn.commit()

conn.close()
