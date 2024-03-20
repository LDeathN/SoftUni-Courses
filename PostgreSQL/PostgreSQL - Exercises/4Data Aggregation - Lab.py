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


