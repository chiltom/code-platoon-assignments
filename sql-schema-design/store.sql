DROP TABLE IF EXISTS action_figures;

CREATE TABLE action_figures (
    id SERIAL PRIMARY KEY,
    action_figure_title VARCHAR(50) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(4, 2) NOT NULL
);

\COPY action_figures FROM './data/action_figure.csv' CSV HEADER;

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(30) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL,
    salary DECIMAL(8,2) NOT NULL
);

\COPY employees FROM './data/employee.csv' CSV HEADER;

DROP TABLE IF EXISTS games;

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    game_title VARCHAR(30) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(4,2) NOT NULL
);

\COPY games FROM './data/game.csv' CSV HEADER;

DROP TABLE IF EXISTS posters;

CREATE TABLE posters (
    id SERIAL PRIMARY KEY,
    poster_title VARCHAR(30) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(4,2)
);

\COPY posters FROM './data/poster.csv' CSV HEADER;