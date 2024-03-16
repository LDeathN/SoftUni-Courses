#First Problem
SELECT id, CONCAT(first_name, ' ', last_name) AS "Full Name", job_title AS "Job Title" FROM employees;


#Second Problem
SELECT id, CONCAT(first_name, ' ', last_name) AS "full_name", job_title, salary FROM employees
WHERE salary > 1000.00
ORDER BY id;


#Third Problem
SELECT * FROM employees
WHERE department_id = 4 AND salary >= 1000
ORDER BY id;


#Fourth Problem
INSERT INTO employees(first_name, last_name, job_title, department_id, salary)
VALUES 
('Samantha', 'Young',' Housekeeping', 4, 900),
('Roger', 'Palmer', 'Waiter', 3, 928.33);

SELECT * FROM employees;


#Fifth Problem
UPDATE employees
SET salary = salary + 100
WHERE job_title = 'Manager';

SELECT * FROM employees
WHERE job_title = 'Manager';


