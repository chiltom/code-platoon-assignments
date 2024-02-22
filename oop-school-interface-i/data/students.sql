-- DROP TABLE IF EXISTS students;

-- CREATE TABLE students (
--     name VARCHAR(10),
--     age INT,
--     role VARCHAR(10),
--     school_id INT,
--     password VARCHAR(10)
-- );

-- COPY students FROM '/Users/tom/projects/code-platoon-assignments/oop-school-interface-i/data/students.csv' DELIMITER ',' CSV HEADER;

-- INSERT INTO students (name, age, role, school_id, password) VALUES ('tom', 24, 'student', 089304, 'xx');



-- SELECT * FROM students;
SELECT name, role FROM students WHERE age < 35;