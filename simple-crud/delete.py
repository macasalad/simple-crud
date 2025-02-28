from server import db, c

delete_tbl = "DELETE FROM students WHERE first_name != 'Hannah'"

c.execute(delete_tbl)
db.commit()
db.close()