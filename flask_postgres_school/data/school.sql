-- Create table schema for each data type - if they exist, drop and recreate
-- TODO: Fix issues with foreign key constraints
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id serial PRIMARY KEY,
    subject VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    subject INT references subjects(id) NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id serial PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    subject INT references subjects(id) NOT NULL
);

-- Copy data from CSV files into tables
COPY subjects FROM '/Users/tom/projects/code-platoon-assignments/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;

COPY students FROM '/Users/tom/projects/code-platoon-assignments/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

COPY teachers FROM '/Users/tom/projects/code-platoon-assignments/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

-- Update sequence positions after hardcoded id values
SELECT setval('subjects_id_seq', (SELECT MAX(id) FROM subjects));
SELECT setval('students_id_seq', (SELECT MAX(id) FROM students));
SELECT setval('teachers_id_seq', (SELECT MAX(id) FROM teachers));