-- Schema
DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  birthdate    date NOT NULL,
  address_id   integer references addresses(id)
);

CREATE TABLE addresses (
  id serial PRIMARY KEY,
  line_1 VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  zipcode INT
);

CREATE TABLE classes (
  id serial PRIMARY KEY,
  name VARCHAR(255),
  credits INT
);

CREATE TABLE enrollments (
  id serial PRIMARY KEY,
  student_id INT references students(id),
  class_id INT references classes(id),
  grade VARCHAR(255)
);