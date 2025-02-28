from server import db, c

update_tbl = """
    INSERT INTO `student_db`.`students`(first_name, last_name, age)
    VALUES
        ("Hannah", "Baniqued", 19),
        ("Hannah", "Lei", 18)
"""

c.execute(update_tbl)
db.commit()
db.close()