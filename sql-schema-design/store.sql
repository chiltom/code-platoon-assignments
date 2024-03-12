-- Drop tables if they already exist to hold new schema design
DROP TABLE IF EXISTS action_figures CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS games CASCADE;
DROP TABLE IF EXISTS gaming_engines CASCADE;
DROP TABLE IF EXISTS genre_games CASCADE;
DROP TABLE IF EXISTS genres CASCADE;
DROP TABLE IF EXISTS posters CASCADE;
DROP TABLE IF EXISTS shifts CASCADE;
DROP TABLE IF EXISTS social_securities CASCADE;


-- Implement new schema design
CREATE TABLE action_figures (
    id SERIAL PRIMARY KEY,
    action_figure_title VARCHAR(50) 
        UNIQUE 
        NOT NULL
        CHECK (action_figure_title ~ '^[A-Z][A-Za-z0-9 \-]+$'),
    quantity INT 
        NOT NULL
        CHECK (quantity >= 1 AND quantity <= 30),
    price DECIMAL(5, 2) 
        NOT NULL
        CHECK (price >= 10.00 AND price <= 100.00)
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(30) 
        UNIQUE 
        NOT NULL
        CHECK (employee_name ~ '^[A-Z][A-Za-z ]+$'),
    position VARCHAR(50) 
        NOT NULL
        CHECK (position IN (
            'Sales Associate',
            'Store Manager',
            'Inventory Clerk',
            'Customer Service Representative',
            'IT Specialist',
            'Marketing Coordinator',
            'Assistant Manager',
            'Finance Analyst',
            'Security Officer',
            'HR Coordinator'
        )),
    salary DECIMAL(8,2) 
        NOT NULL
        CHECK (salary / 2080 > 16.66 AND salary / 2080 < 31.25)
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    game_title VARCHAR(30) 
        UNIQUE 
        NOT NULL,
    quantity INT 
        NOT NULL,
    price DECIMAL(4,2) 
        NOT NULL
);

CREATE TABLE gaming_engines (
    engine_id SERIAL PRIMARY KEY,
    engine_name VARCHAR(30)
        UNIQUE
        NOT NULL
        CHECK (engine_name ~ '^[A-Z][A-Za-z0-9 \-]+$')
);

CREATE TABLE genre_games (
    id SERIAL PRIMARY KEY,
    game_id INT NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(20)
        UNIQUE
        NOT NULL
        CHECK (genre_name ~ '^[A-Z][A-Za-z \-]+$')
);

CREATE TABLE posters (
    id SERIAL PRIMARY KEY,
    poster_title VARCHAR(30) 
        UNIQUE 
        NOT NULL
        CHECK (poster_title ~ '^[A-Z][A-Za-z0-9 \-]+$'),
    quantity INT 
        NOT NULL
        CHECK (quantity >= 1 AND quantity <= 30),
    price DECIMAL(4,2)
        NOT NULL
        CHECK (price >= 6.00 AND price <= 20.00)
);

CREATE TABLE shifts (
    id SERIAL PRIMARY KEY,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE social_securities (
    id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    ssn INT 
        UNIQUE
        NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);


-- Copy all data from CSV files
\COPY action_figures FROM './data/action_figure.csv' CSV HEADER;
\COPY employees FROM './data/employee.csv' CSV HEADER;
\COPY games FROM './data/game.csv' CSV HEADER;
\COPY gaming_engines FROM './data/gaming_engine.csv' CSV HEADER;
\COPY genre_games FROM './data/genre_game.csv' CSV HEADER;
\COPY genres FROM './data/genre.csv' CSV HEADER;
\COPY posters FROM './data/poster.csv' CSV HEADER;
\COPY shifts FROM './data/shifts.csv' CSV HEADER;
\COPY social_securities FROM './data/social_security.csv' CSV HEADER;