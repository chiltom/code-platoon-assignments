COMMENT ON SCHEMA game_store IS 
    'This schema covers the operation of a game store,
    concerned with data regarding the inventory of games
    and game information, posters, and action figures. 
    The store is also concerned with storing employee
    information here is well.';


BEGIN;

DROP TABLE IF EXISTS action_figure CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS game CASCADE;
DROP TABLE IF EXISTS gaming_engine CASCADE;
DROP TABLE IF EXISTS genre_game CASCADE;
DROP TABLE IF EXISTS genre CASCADE;
DROP TABLE IF EXISTS poster CASCADE;
DROP TABLE IF EXISTS shift CASCADE;
DROP TABLE IF EXISTS social_security CASCADE;


CREATE TABLE action_figure (
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

COMMENT ON TABLE action_figure IS 
    'Relation that holds records of each action figure with: 
    - An id that automatically generates as a primary key
    - The title of the item with a unique constraint and a check 
    constraint to ensure the name is in Title case and only has 
    letters, integers, spaces, and hyphens 
    -The quantity in stock with a check constraint ensuring there 
    is always at least one and no more than 30 
    - The price with a check constraint ensuring that the price is
    no less than ten dollars and no more than 100.';


CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(30)
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

COMMENT ON TABLE employee IS 
    'Relation that holds records of each employee with:
    - An id that automatically generates as a primary key
    - The employee name with a check constraint to ensure
    that it is in title case and includes only letters and
    spaces
    - The employee position with a check constraint to ensure
    that it is one of the positions that the company offers
    - The employee salary with a check constraint ensuring
    that the employee does not make less than 16.66 an hour
    but no more than 31.25 an hour.';


CREATE TABLE gaming_engine (
    engine_id SERIAL PRIMARY KEY,
    engine_name VARCHAR(30)
        UNIQUE
        NOT NULL
        CHECK (engine_name ~ '^[A-Z][A-Za-z0-9 \-]+$')
);

COMMENT ON TABLE gaming_engine IS 
    'Relation that holds records of each gaming engine with:
    - An engine id that is automatically generated as the primary key
    - The engine name with a unique constraint and a check constraint
    ensuring that the name of the engine is in title case and has only
    letters, numbers, spaces, and hyphens.';


CREATE TABLE game (
    id SERIAL PRIMARY KEY,
    engine_id INT NOT NULL,
    game_title VARCHAR(30) 
        UNIQUE 
        NOT NULL
        CHECK (game_title ~ '^[A-Z][A-Za-z0-9 \-:''\\]+$'),
    quantity INT 
        NOT NULL
        CHECK (quantity >= 1 AND quantity <= 50),
    price DECIMAL(4,2) 
        NOT NULL
        CHECK (price >= 10.00 AND price <= 60.00),
    
    FOREIGN KEY (engine_id) REFERENCES gaming_engine(engine_id)
);

COMMENT ON TABLE game IS 
    'Relation that holds records of each game with:
    - An id that is automatically generated as the primary key
    - The title of the game with a unique constraint and a
    check constraint ensuring that it is in title case and has
    only letters, integers, spaces, and hyphens
    - The quantity of the games in stock with a check constraint
    to ensure that at least one game is always in stock but no more
    than fifty at a time are sitting in the store
    - The price of the game with a check constraint ensuring that
    the game is at least making ten dollars but not being sold
    for more than sixty dollars.';


CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(20)
        UNIQUE
        NOT NULL
        CHECK (genre_name ~ '^[A-Z][A-Za-z \-]+$')
);

COMMENT ON TABLE genre IS 
    'Relation that holds records of each genre with:
    - A genre id that is automatically generated as the primary key
    - The genre name with a unique constraint and a check constraint
    ensuring that it is in title case and consists of only letters
    spaces and hyphens.';


CREATE TABLE genre_game (
    id SERIAL PRIMARY KEY,
    game_id INT NOT NULL,
    genre_id INT NOT NULL,
    FOREIGN KEY (game_id) REFERENCES game(id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

COMMENT ON TABLE genre_game IS 
    'Relation that holds records of each game and genre with:
    - An id that is automatically generated as the primary key
    - The game_id associated with the record as a foreign key,
    referenced to the game relation id field
    - The genre_id associated with the record as a foreign key,
    referenced to the genre relation genre id field';


CREATE TABLE poster (
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

COMMENT ON TABLE poster IS 
    'Relation that holds records of each poster with:
    - An id that is automatically generated as the primary key
    - A poster title with a unique constraint and a check constraint
    to ensure that it is in title case and it only contains letters,
    integers, spaces, and hyphens
    - The quantity with a check constraint ensuring that there is
    always at least one poster and no more than thirty sitting
    - The price of each poster with a check constraint to ensure that
    they are not sold for less than six dollars but also not sold for
    more than twenty dollars.';


CREATE TABLE shift (
    id SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    employee_id INT NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

COMMENT ON TABLE shift IS 
    'Relation that holds records of each employee shift with:
    - An id that is automatically generated as the primary key
    - The start time
    - The end time
    - The employee id as a foreign key with a reference to the 
    id field in the employee table.';


CREATE TABLE social_security (
    id SERIAL PRIMARY KEY,
    employee_id INT NOT NULL,
    ssn VARCHAR(11) 
        UNIQUE
        NOT NULL
        CHECK (ssn ~ '^\d{3}-\d{2}-\d{4}$'),
    FOREIGN KEY (employee_id) REFERENCES employee(id)
);

COMMENT ON TABLE social_security IS 
    'Relation that holds records of each social security number with:
    - An id that is automatically generated as the primary key
    - The employee id associated with the ssn as a foreign key with a
    reference to the employee relation id field
    - The ssn of the employee with a unique constraint and a check
    constraint ensuring that the ssn is in proper format.';


\COPY action_figure FROM './data/action_figure.csv' CSV HEADER;
\COPY employee FROM './data/employee.csv' CSV HEADER;
\COPY gaming_engine FROM './data/gaming_engine.csv' CSV HEADER;
\COPY game FROM './data/game.csv' CSV HEADER;
\COPY genre FROM './data/genre.csv' CSV HEADER;
\COPY genre_game FROM './data/genre_game.csv' CSV HEADER;
\COPY poster FROM './data/poster.csv' CSV HEADER;
\COPY shift FROM './data/shifts.csv' CSV HEADER;
\COPY social_security FROM './data/social_security.csv' CSV HEADER;


COMMIT;