/*
    Script to create schema and copy data from csv files
    for 64 slices pizza shop
*/

DROP TABLE IF EXISTS available_pizzas CASCADE;
DROP TABLE IF EXISTS available_toppings CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS stores CASCADE;
DROP TABLE IF EXISTS drivers CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS deliveries CASCADE;

-- Copy available pizza data from csv file
-- id as primary key
-- name as unique entry

CREATE TABLE available_pizzas (
    pizza_id SERIAL PRIMARY KEY,
    pizza_name VARCHAR(10) UNIQUE NOT NULL,
    pizza_cost INT NOT NULL
);

\COPY available_pizzas FROM './data/available_pizzas.csv' CSV HEADER;


-- Copy available toppings data from csv file
-- id as primary key
-- name as unique entry

CREATE TABLE available_toppings (
    topping_id SERIAL PRIMARY KEY,
    topping_name VARCHAR(50) UNIQUE NOT NULL,
    topping_cost_per_pizza INT NOT NULL
);

\COPY available_toppings FROM './data/available_toppings.csv' CSV HEADER;


-- Copy customers data from csv file
-- id as primary key

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(20) NOT NULL,
    zip VARCHAR(10) NOT NULL,
    country VARCHAR(5) NOT NULL
);

\COPY customers FROM './data/customers.csv' CSV HEADER;


-- Copy stores data from CSV file
-- store_id is primary key

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    location VARCHAR(50) UNIQUE NOT NULL
);

\COPY stores FROM './data/stores.csv' CSV HEADER;


-- Copy drivers data from csv file
-- driver_id is primary key
-- store_id as foreign key referencing stores(store_id)

CREATE TABLE drivers (
    driver_id SERIAL PRIMARY KEY,
    store_id INT NOT NULL,
    full_name VARCHAR(40) NOT NULL,

    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

\COPY drivers FROM './data/drivers.csv' CSV HEADER;


-- Copy orders data from CSV file
-- order_id is primary key
-- customer_id is foreign key referencing customers(customer_id)
-- pizza_type is foreign key referencing available_pizzas(pizza_name)
-- store_id is foreign key referencing stores(store_id)
-- toppings is foreign key referencing available_toppings(topping_id)

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    date DATE NOT NULL,
    pizza_type VARCHAR(10) NOT NULL,
    store_id INT NOT NULL,
    toppings INT,

    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (pizza_type) REFERENCES available_pizzas(pizza_name),
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (toppings) REFERENCES available_toppings(topping_id)
);

\COPY orders FROM './data/orders.csv' CSV HEADER;


-- Copy deliveries data from csv file
-- driver_id as foreign key referencing drivers(driver_id)
-- order_id as foreign key referencing orders(order_id)

CREATE TABLE deliveries (
    driver_id INT NOT NULL,
    order_id INT NOT NULL,
    started_delivery TIME NOT NULL,
    completed_delivery TIME NOT NULL,

    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)

);

\COPY deliveries FROM './data/deliveries.csv' CSV HEADER;

