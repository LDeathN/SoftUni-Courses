#First Problem
SELECT t.town_id, t.name AS town_name, a.address_text
FROM towns AS t
LEFT JOIN addresses AS a
ON t.town_id = a.town_id
WHERE t.name LIKE '%San Francisco%'
OR t.name LIKE '%Sofia%'
OR t.name LIKE '%Carnation%'
ORDER BY a.town_id, a.address_id;


#Second Problem
SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name) AS full_name,
d.department_id, d.name AS department_name
FROM employees AS e
JOIN departments AS d
ON e.employee_id = d.manager_id
ORDER BY e.employee_id
LIMIT 5;


