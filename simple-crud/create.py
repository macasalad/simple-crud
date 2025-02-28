from server import db, c

create_tbl = """
    CREATE TABLE `student_db`.`students` (
        `id` INT PRIMARY KEY AUTO_INCREMENT,
        `first_name` VARCHAR(255) NOT NULL,
        `last_name` VARCHAR(255) NOT NULL,
        `age` INT NOT NULL
    )
"""

c.execute(create_tbl)
db.commit()
db.close()