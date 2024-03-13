COMMENT ON SCHEMA ice_cream_shop IS 
    'This schema designs five tables to manage sales, inventory, and
    employees of 32 Flavors';

BEGIN;


DROP TABLE IF EXISTS flavor_of_ice_cream CASCADE;
DROP TABLE IF EXISTS type_of_cone CASCADE;
DROP TABLE IF EXISTS employee CASCADE;
DROP TABLE IF EXISTS employee_timesheet CASCADE;
DROP TABLE IF EXISTS sale CASCADE;


CREATE TABLE flavor_of_ice_cream (
    flavor_id SERIAL PRIMARY KEY,
    flavor VARCHAR(20) 
        UNIQUE 
        NOT NULL
        CHECK (flavor IN (
            'Vanilla',
            'Chocolate',
            'Strawberry',
            'Black Cherry',
            'Pistachio',
            'Mint Chocolate Chip',
            'Orange Sorbet',
            'Raspberry Cheescake'
            )),
    quantity INT 
        NOT NULL
        CHECK (quantity >= 1 AND quantity <= 20),
    dairy_free BOOLEAN 
        NOT NULL,
    cost_per_bucket DECIMAL(4,2) 
        NOT NULL
        CHECK (cost_per_bucket >= 15.00 AND cost_per_bucket <= 30.00),
    price_per_scoop DECIMAL(3,2) 
        NOT NULL
        CHECK (price_per_scoop >= 1.50 AND price_per_scoop <= 3.00)
);

COMMENT ON TABLE flavor_of_ice_cream IS
    'Relation that holds records of flavor of ice cream with these fields:
    - A primary key ID for each flavor that is automatically set
    - The name of the flavor which is unique, cannot be omitted, and 
    must be in the set inventory that the shop holds
    - The quantity in stock of that flavor, with a constrant that there
    must always be at least one bucket of ice cream and at most twenty
    to prevent spoiling
    - A true/false value if the flavor is dairy free or not
    - The cost per bucket that the store pays the wholesaler
    - The price per scoop that the store will then charge customers';


CREATE TABLE type_of_cone (
    cone_id SERIAL PRIMARY KEY,
    cone VARCHAR(20) 
        NOT NULL
        CHECK (cone IN (
            'Waffle',
            'Sugar',
            'Cake'
        )),
    quantity INT 
        NOT NULL
        CHECK (quantity >= 1 AND quantity <= 15),
    gluten_free BOOLEAN 
        NOT NULL,
    cost_per_box DECIMAL(4,2)
        NOT NULL
        CHECK (cost_per_box >= 20.00 AND cost_per_box <= 40.00),
    price_per_cone DECIMAL(3,2)
        NOT NULL
        CHECK (price_per_cone >= 2.00 AND price_per_cone <= 4.00)
);

COMMENT ON TABLE type_of_cone IS
    'Relation that holds records of each type of cone with the following fields:
    - A primary key ID for each type that is automatically generated
    - The name of the type of cone that must not be omitted and must be in the
    stores normal inventory that they stock
    - The quantity in stock of that type of cone that cannot be omitted; the store
    must always have at least one box of cones in stock and cannot go over 15 boxes
    due to expiration concerns
    - A true/false value if the flavor is gluten-free or not
    - The cost per box that the store pays to the wholesaler
    - The price per cone that the store will charge the customer';


CREATE TABLE employee (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(30)
        NOT NULL
        CHECK (name ~ '^[A-Z][A-Za-z \-]'),
    position VARCHAR(50) 
        NOT NULL
        CHECK (position IN (
            'Server',
            'Manager'
        ))
);

COMMENT ON TABLE employee IS
    'Relation that holds records for each employee with the following fields:
    - A primary key ID for each employee that is automatically generated
    - The name of each employee, which must be in Title case and have only
    letters (upper and lowercase), spaces, and hyphens
    - Their position in the store, either a server or a manager';


CREATE TABLE employee_timesheet (
    employee_id INT,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,

    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

COMMENT ON TABLE employee_timesheet IS
    'Relation that holds records for each employee timesheet with
    the following fields:
    - Employee ID that references the employee relation employee id 
    field, establishing a one-to-one connection with each employee record 
    and their respective timesheet
    - A start timestamp that holds the exact date and time
    - An end timestamp that holds the exact date and time';


CREATE TABLE sale (
    sale_id SERIAL PRIMARY KEY,
    flavor_id INT 
        NOT NULL,
    scoop_quantity INT 
        NOT NULL
        CHECK (scoop_quantity >= 1 AND scoop_quantity <= 3),
    cone_id INT 
        NOT NULL,
    cone_quantity INT
        NOT NULL
        CHECK (cone_quantity = 1),
    employee_id INT 
        NOT NULL,
    time_of_sale TIMESTAMP 
        NOT NULL,
    cost_of_sale DECIMAL(4,2) 
        NOT NULL,

    FOREIGN KEY (flavor_id) REFERENCES flavor_of_ice_cream(flavor_id),
    FOREIGN KEY (cone_id) REFERENCES type_of_cone(cone_id),
    FOREIGN KEY (employee_id) REFERENCES employee(employee_id)
);

COMMENT ON TABLE sale IS 
    'Relation that holds the record for each sale that occurs in the shop 
    with the following fields:
    - A primary key ID for the individual sale that is automatically generated
    - The ID of the flavor that was purchased that references the flavor relation
    flavor_id, establishing a many-to-one connection where one flavor can be sold
    many times across many different sales
    - The quantity of the flavors sold, ensuring that at least one scoop is served
    and no more than three scoops are sold on one cone
    - The ID of the cone that was purchased that references the cone relation
    cone_id, establishing a many-to-one connection where one type can be sold many
    times across many different sales
    - The quantity of the cones sold, ensuring that only one cone is sold at a time
    - The ID of the employee that served the transaction that references the employee
    relation employee_id, establishing a many-to-one connection where one employee
    can serve many different customers
    - The date and time of the sale to track when sales are being made for later analysis
    - The cost of each cone sale summing the total amount for later analysis and 
    purchase history analysis';


\COPY flavor_of_ice_cream FROM './data/flavors_of_ice_cream.csv' CSV HEADER;
\COPY type_of_cone FROM './data/types_of_cones.csv' CSV HEADER;
\COPY employee FROM './data/employees.csv' CSV HEADER;
\COPY employee_timesheet FROM './data/employee_timesheets.csv' CSV HEADER;
\COPY sale FROM './data/sales.csv' CSV HEADER;


COMMIT;