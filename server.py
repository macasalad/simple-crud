import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)
c = db.cursor()

create_db = "CREATE DATABASE IF NOT EXISTS student_db"
c.execute(create_db)
c.close()

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "student_db"
)
c = db.cursor()