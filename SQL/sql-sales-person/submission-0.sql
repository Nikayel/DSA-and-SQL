-- Write your query below
--- OMIT using NOT IN 
SELECT name FROM sales_person
WHERE sales_id NOT IN 
-- SELECT All Sales PEOPLE who made a sale with th ecompany CRIMSON
    (SELECT o.sales_id FROM orders o
    LEFT JOIN company c ON o.com_id = c.com_id
    WHERE c.name = 'CRIMSON')