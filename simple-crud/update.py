from server import db, c

update_tbl = """
    UPDATE students
    SET age = 19 WHERE age <= 18
"""

c.execute(update_tbl)
db.commit()
db.close()