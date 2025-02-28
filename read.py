from server import db, c

read_tbl = "SELECT * FROM students"

c.execute(read_tbl)

students_data = c.fetchall()

for student in students_data:
    print(student)
    
db.commit()
db.close()