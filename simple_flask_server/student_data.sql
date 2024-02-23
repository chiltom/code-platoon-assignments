-- Drop students table if it already exists
 DROP TABLE IF EXISTS students;
-- Create students table shema
 CREATE TABLE students (
    id serial PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    grade CHAR(1)
 );

-- Insert student data into table
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (1, 'John', 'Doe', 18, 'A');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (2, 'Jane', 'Smith', 19, 'B');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (3, 'Bob', 'Johnson', 20, 'C');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (4, 'Emily', 'Williams', 18, 'A');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (5, 'Michael', 'Brown', 19, 'B');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (6, 'Samantha', 'Davis', 22, 'A');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (7, 'Oliver', 'Jones', 20, 'B');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (8, 'Sophia', 'Miller', 21, 'A');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (9, 'Ethan', 'Wilson', 19, 'C');
 INSERT INTO students (id, first_name, last_name, age, grade) VALUES (10, 'Isabella', 'Moore', 22, 'B');

-- Manually reset the sequence of the id primary key to the max value of id
-- because we hardcoded ID for the value insertion
SELECT setval('students_id_seq', (SELECT MAX(id) FROM students));