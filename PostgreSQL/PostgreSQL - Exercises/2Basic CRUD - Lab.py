#First Problem
SELECT id, CONCAT(first_name, ' ', last_name) AS "Full Name", job_title AS "Job Title" FROM employees;


#Second Problem
SELECT id, CONCAT(first_name, ' ', last_name) AS "full_name", job_title, salary FROM employees
WHERE salary > 1000.00
ORDER BY id;


