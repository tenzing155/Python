# import sqlite3

# conn = sqlite3.connect('college.sqlite3')
# cursor = conn.cursor()

# def create_table():
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS students(
#     student_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL,
#     address TEXT NOT NULL)
#     """)
#     conn.commit()

# create_table()

# def insert(name, email, address):
#     cursor.execute("""
#     INSERT INTO students(name, email, address)            
#     VALUES(?, ?, ?)""", (name, email, address))
#     conn.commit()

# insert('ram', 'ram123@gmail.com', 'ktm')

# def show():
#     cursor.execute("""SELECT * FROM students""")
#     data = cursor.fetchall()
#     print(data)

# # def update(student_id, name, address):
# #     cursor.execute("""UPDATE students SET name=?, address=? WHERE student_id=?""", (name, address, student_id))
# #     conn.commit()
# #     print("Data updated successfully.")

# # update(1, "Hari", "ktm")

# # def delete(student_id):
# #     cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
# #     conn.commit()
# #     print("Data deleted successfully.")

# # delete(1)

# show()

# conn.close()
