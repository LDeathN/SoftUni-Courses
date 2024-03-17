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
