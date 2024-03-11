/* 
    This schema aims to create four tables to manage sales, 
    inventory, and employees of 32 Flavors. Each table holds 
    a specific purpose, and the three separate tables are all
    related by the sales table.
*/

/*
    Table which holds the different flavors of ice cream all with:
    - A primary key ID for each flavor
    - The name of the flavor (unique so no repeats)
    - The quantity in stock of that flavor
    - A true/false value if the flavor is dairy free or not
*/
DROP TABLE IF EXISTS buckets_of_ice_cream;

CREATE TABLE buckets_of_ice_cream (
    id SERIAL PRIMARY KEY,
    flavor VARCHAR(20) UNIQUE NOT NULL,
    quantity INT NOT NULL,
    dairy_free BOOLEAN NOT NULL
);

-- Mock data for ice cream flavors
\COPY buckets_of_ice_cream FROM './data/buckets_of_ice_cream.csv' CSV HEADER;

/*
    Table which holds the different types of cones all with:
    - A primary key ID for each type
    - The name of the type of cone (not unique for gluten-free variants)
    - The quantity in stock of that type
    - A true/false value if the flavor is gluten-free or not
*/
DROP TABLE IF EXISTS boxes_of_cones;

CREATE TABLE boxes_of_cones (
    id SERIAL PRIMARY KEY,
    cone VARCHAR(20) NOT NULL,
    quantity INT NOT NULL,
    gluten_free BOOLEAN NOT NULL
);

-- Mock data for ice cream flavors
\COPY boxes_of_cones FROM './data/boxes_of_cones.csv' CSV HEADER;


/*
    Table which holds the data for all employees of 32 flavors with:
    - A primary key ID for each employee
    - The name of each employee, unique so no employee is doubly-entered
    - The position in the shop that they serve in
    - The amount of hours they have worked
*/

DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL,
    hours INT NOT NULL
);

-- Mock data for employees
\COPY employees FROM './data/employees.csv' CSV HEADER;


/*
    Table which holds the data for each sale that occurs in the shop with:
    - A primary key ID for the individual sale
    - The ID of the flavor that was purchased
    - The quantity of the flavors sold
    - The ID of the cone that was purchased
    - The quantity of the cones sold of that flavor
    - The ID of the employee that served the transaction
*/

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    flavor_id INT NOT NULL,
    flavor_quantity INT NOT NULL,
    cone_id INT NOT NULL,
    cone_quantity INT NOT NULL,
    employee_id INT NOT NULL
);

-- Mock data for sales
\COPY sales FROM './data/sales.csv' CSV HEADER;