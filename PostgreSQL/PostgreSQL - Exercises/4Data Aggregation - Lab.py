#First Problem
SELECT department_id,
COUNT(department_id) AS "employee_count"
FROM employees
GROUP BY department_id
ORDER BY department_id;


#Second Problem
SELECT "department_id",
COUNT("salary") AS "employee_count"
FROM "employees"
GROUP BY "department_id"
ORDER BY "department_id";


#Third Problem
SELECT "department_id",
SUM("salary") AS "total_salaries"
FROM "employees"
GROUP BY "department_id"
ORDER BY "department_id";


#Fourth Problem
SELECT "department_id",
MAX(salary) AS "max_salary"
FROM "employees"
GROUP BY "department_id"
ORDER BY "department_id";


#Fifth Problem
SELECT "department_id",
MIN(salary) AS "min_salary"
FROM "employees"
GROUP BY "department_id"
ORDER BY "department_id";


#Sixth Problem
SELECT "department_id",
AVG(salary) AS "avg_salary"
FROM "employees"
GROUP BY "department_id"
ORDER BY "department_id";


#Seventh Problem
SELECT "department_id",
SUM("salary") AS "total_salaries"
FROM "employees"
GROUP BY "department_id"
HAVING SUM(salary) < 4200
ORDER BY "department_id";


#Eight Problem
SELECT id, first_name, last_name,
TRUNC(salary, 2) AS salary,
department_id,
CASE department_id
WHEN 1 THEN 'Management'
WHEN 2 THEN 'Kitchen Staff'
WHEN 3 THEN 'Service Staff'
ELSE 'Other'
END AS department_name
FROM employees ORDER BY id;
