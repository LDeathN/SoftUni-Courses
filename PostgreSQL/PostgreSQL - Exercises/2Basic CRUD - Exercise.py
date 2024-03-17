SELECT * FROM cities
ORDER BY id;


SELECT CONCAT(name, ' ', state) AS cities_information, area AS area_km2 FROM cities
ORDER BY id;


SELECT DISTINCT name, area AS area_km2 FROM cities
ORDER BY name DESC;


SELECT id, CONCAT(first_name, ' ', last_name) AS full_name, job_title FROM employees
ORDER BY first_name 
LIMIT 50;


SELECT id AS id, CONCAT(first_name, ' ', middle_name, ' ', last_name) AS full_name, hire_date FROM employees
ORDER BY hire_date 
OFFSET 9 ROWS;


SELECT id, CONCAT(number, ' ', street) AS address, city_id FROM addresses
WHERE id >= 20;


SELECT CONCAT(number, ' ', street) AS address, city_id FROM addresses
WHERE city_id % 2 = 0 AND city_id > 0
ORDER BY city_id;


SELECT name, start_date, end_date FROM projects
WHERE start_date >= '2016-06-01 07:00:00'
AND end_date < '2023-06-04 00:00:00'
ORDER BY start_date;


SELECT number, street FROM addresses
WHERE id BETWEEN 50 AND 100
OR number < 1000;


SELECT employee_id, project_id FROM employees_projects
WHERE employee_id IN (200, 250)
AND project_id NOT IN (50, 100);
