import logging
import random
from connect import create_connection

from sqlite3 import DatabaseError
from faker import Faker

fake = Faker()

def insert_data(c, sql_expression, data):
    try:
        c.execute(sql_expression, data)
        print(f"Insert data: {data}")
    except DatabaseError as e:
        logging.error(e)
        raise DatabaseError(e)
    finally:
        # c.close()
        pass


def insert_groups(c, sql_expression: str):
    # c = conn.cursor()
    for _ in range(3):
        insert_data(c, sql_expression, (fake.word(),))


def insert_teachers(c, sql_expression: str):
    for _ in range(5):
        insert_data(c, sql_expression, (fake.name(),))
    pass


def insert_teacher_to_subjects(c, sql_expression: str):
    c.execute("""SELECT * FROM teachers""")
    teachers = c.fetchall()
    # print(teachers)
    for _ in range(8):
        teacher_id = random.choice(teachers)[0]
        insert_data(c, sql_expression, (fake.word(), teacher_id))


def insert_students(c, sql_expression: str):
    c.execute("""SELECT id FROM groups""")
    groups = c.fetchall()
    print(groups)
    for _ in range(30):
        group_id = random.choice(groups)[0]
        insert_data(c, sql_expression, (fake.name(), group_id))
        # insert_data(c, sql_expression, (fake.word(), "16"))
        # print(teacher_id)


def insert_grades(c, sql_expression: str):
    c.execute("""SELECT id FROM students""")
    students = c.fetchall()
    c.execute("""SELECT id FROM subjects""")
    subjects = c.fetchall()

    for student in students:
        student_id = student[0]
        for _ in range(random.randint(7, 20)):
            date = fake.date_between(start_date="-1y", end_date="today")
            subject_id = random.choice(subjects)
            insert_data(
                c, sql_expression, (student_id, subject_id, random.randint(1, 5), date)
            )


if __name__ == "__main__":
    sql_insert_groups = """
        INSERT INTO groups (name) VALUES (%s);
        """
    # INSERT INTO users (name, email, password, age) VALUES (%s, %s, %s, %s);

    sql_insert_teachers = """
        INSERT INTO teachers (name) VALUES (%s);
        """

    sql_insert_subjects = """
        INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);
        """

    sql_insert_students = """
        INSERT INTO students (name, group_id) VALUES (%s, %s);
        """

    sql_insert_grades = """
        INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s);
        """

    try:
        print("start connect to database")
        with create_connection() as conn:
            if conn is not None:
                # create projects table
                c = conn.cursor()
                print("connections")
                insert_groups(c, sql_insert_groups)
                insert_teachers(c, sql_insert_teachers)
                insert_teacher_to_subjects(c, sql_insert_subjects)
                insert_students(c, sql_insert_students)
                insert_grades(c, sql_insert_grades)

                conn.commit()

            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        conn.rollback()
        logging.error(err)
