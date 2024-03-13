-- Scenario 1
SELECT engine_name 
    FROM gaming_engine;
-- Scenario 2
SELECT SUM(quantity) AS "Total Quantity" 
    FROM game;
-- Scenario 3
SELECT game_title 
    FROM game 
    WHERE price > 30.00;
-- Scenario 4
SELECT game_title, quantity 
    FROM game 
    WHERE quantity < 10;
-- Scenario 5
SELECT COUNT(genre_game_id) 
    FROM genre_game;
-- Scenario 6
SELECT action_figure_title 
    FROM action_figure 
    WHERE (price >= 20.00 AND price <= 50.00);
-- Scenario 7
SELECT poster_title, price 
    FROM poster 
    WHERE (quantity >= 15 AND quantity <= 30);
-- Scenario 8
SELECT employee_name, position
    FROM employee
    WHERE salary > 40000.00;
-- Scenario 9
SELECT COUNT(social_security_id)
    FROM social_security;
-- Scenario 10
SELECT start_time, end_time
    FROM shift;
-- Scenario 11
SELECT employee_name, salary
    FROM shift
    INNER JOIN employee ON shift.employee_id = employee.employee_id;
-- Scenario 12
SELECT *
    FROM action_figure
    WHERE quantity < 5;
-- Scenario 13
SELECT game_title
    FROM game
    WHERE game_title LIKE '%Warzone%';
-- Scenario 14
SELECT COUNT(genre_id)
    FROM genre;
-- Scenario 15
SELECT action_figure_title AS name, quantity
    FROM action_figure
    WHERE price > 75.00;
-- Scenario 16
SELECT employee_name AS name
    FROM employee
    WHERE position = 'IT Specialist';
-- Scenario 17
SELECT game_title AS name
    FROM game
    WHERE quantity > 25;
-- Scenario 18
SELECT SUM(totalHours) AS "Total"
    FROM 
    (
        SELECT SUM(quantity) AS totalHours FROM game
        UNION ALL
        SELECT SUM(quantity) AS totalHours FROM action_figure
        UNION ALL
        SELECT SUM(quantity) AS totalHours FROM poster
    ) AS src;
-- Scenario 19
SELECT ssn, employee_name
    FROM social_security
    INNER JOIN employee ON social_security.employee_id = employee.employee_id;
-- Scenario 20
SELECT poster_title AS "name", quantity
    FROM poster
    WHERE (price >= 10.00 AND price <= 15.00);
-- Scenario 21
SELECT poster_title AS "name", quantity
    FROM poster
    WHERE (price <= 8.00);
-- Scenario 22
SELECT employee_name, salary
    FROM employee
    WHERE position IN ('Marketing Coordinator', 'Finance Analyst');
-- Scenario 23
SELECT SUM(quantity)
    FROM action_figure;
-- Scenario 24
SELECT game_title AS "name", quantity
    FROM game
    WHERE (quantity >= 15 AND quantity <= 30);
-- Scenario 25
SELECT employee_name AS "name", salary
    FROM shift
    INNER JOIN employee ON shift.employee_id = employee.employee_id
    WHERE (start_time > '2024-01-01');
-- Scenario 26
SELECT game_title AS "name", price
    FROM game
    WHERE (price < 20.00);
-- Scenario 27
SELECT SUM(quantity) AS "Total"
    FROM action_figure
    WHERE (price >= 25.00 AND price <= 30.00);
-- Scenario 28
SELECT employee_name AS "name", position
    FROM shift
    INNER JOIN employee ON shift.employee_id = employee.employee_id
    WHERE (start_time <= '2024-03-07 13:00:00');
-- Scenario 29
SELECT action_figure_title AS "name", quantity
    FROM action_figure
    WHERE (quantity > 10);
-- Scenario 30
SELECT poster_title AS "name", quantity
    FROM poster
    WHERE (quantity > 25);
-- Scenario 31
SELECT COUNT(shift_id) AS "Total Shifts"
    FROM shift;
-- Scenario 32
SELECT employee_name AS "name", position
    FROM shift
    INNER JOIN employee ON shift.employee_id = employee.employee_id
    WHERE (start_time > '2024-02-01' AND start_time < '2024-03-07 13:00:00');
-- Scenario 33
SELECT game_title AS "name"
    FROM game
    WHERE quantity < 20;
-- Scenario 34
SELECT action_figure_title AS "name", quantity
    FROM action_figure
    WHERE price > 23.00;
-- Scenario 35
SELECT SUM(quantity)
    FROM poster;