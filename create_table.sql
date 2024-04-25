drop table if exists groups;
-- Створення таблиці груп
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) not NULL
);

drop table if exists students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    group_id INTEGER REFERENCES groups(id)
);


drop table if exists teachers;
-- Створення таблиці викладачів
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

drop table if exists subjects;
-- Створення таблиці предметів із вказівкою викладача
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150),
    teacher_id INTEGER REFERENCES teachers(id)
);

drop table if exists grades;
-- Створення таблиці оцінок з вказівкою студента, предмету, оцінки та дати
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id),
    grade INTEGER check (grade >= 0 and grade <=100),
    date DATE not null
);