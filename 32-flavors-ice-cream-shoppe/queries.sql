-- Number of employee hours worked per store
SELECT total AS "Hours per Store"
    FROM
        (
            SELECT SUM(hours) AS total
                FROM employee_timesheet
                WHERE store_id = 1
            UNION ALL
            SELECT SUM(hours) AS total
                FROM employee_timesheet
                WHERE store_id = 2
            UNION ALL
            SELECT SUM(hours) AS total
                FROM employee_timesheet
                WHERE store_id = 3
        ) AS src;

-- Number of purchases per store
SELECT total AS "Purchases per Store"
    FROM
    (
        SELECT COUNT(sale_id) AS total
            FROM sale
            WHERE store_id = 1
        UNION ALL
        SELECT COUNT(sale_id) AS total
            FROM sale
            WHERE store_id = 2
        UNION ALL
        SELECT COUNT(sale_id) AS total
            FROM sale
            WHERE store_id = 3
    ) AS src;

-- Profit per store from customer purchases
SELECT total AS "Profit per Store"
    FROM
    (
        SELECT SUM(cost_of_sale) AS total
            FROM sale
            WHERE store_id = 1
        UNION ALL
        SELECT SUM(cost_of_sale) AS total
            FROM sale
            WHERE store_id = 2
        UNION ALL
        SELECT SUM(cost_of_sale) AS total
            FROM sale
            WHERE store_id = 3
    ) AS src;