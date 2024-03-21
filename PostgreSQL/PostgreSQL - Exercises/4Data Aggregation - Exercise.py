SELECT COUNT(id) AS count
FROM wizard_deposits;


SELECT SUM(deposit_amount) AS total_amount
FROM wizard_deposits;


SELECT ROUND(AVG(magic_wand_size), 3) AS average_magic_wand_size
FROM wizard_deposits;


SELECT MIN(deposit_charge) AS minimum_deposit_charge
FROM wizard_deposits;


SELECT MAX(age) AS maximum_age
FROM wizard_deposits;


SELECT deposit_group, 
SUM(deposit_interest) AS deposit_interest
FROM wizard_deposits
GROUP BY deposit_group
ORDER BY deposit_interest DESC;


SELECT magic_wand_creator,
MIN(magic_wand_size) AS minimum_wand_size
FROM wizard_deposits
GROUP BY magic_wand_creator
ORDER BY minimum_wand_size
LIMIT 5;


SELECT
  deposit_group,
  is_deposit_expired,
  FLOOR(AVG(deposit_interest)) AS deposit_interest
FROM
  wizard_deposits
WHERE
  deposit_start_date > '1985-01-01'
GROUP BY
  deposit_group, is_deposit_expired
ORDER BY
  deposit_group DESC, is_deposit_expired ASC;


SELECT last_name,
COUNT(notes) AS notes_with_dumbledore
FROM wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY last_name;


CREATE VIEW view_wizard_deposits_with_expiration_date_before_1983_08_17 AS
SELECT CONCAT(first_name, ' ', last_name) AS "wizard_name",
deposit_start_date AS start_date,
deposit_expiration_date AS expiration_date,
deposit_amount AS amount
FROM wizard_deposits
WHERE deposit_expiration_date <= '1983_08-17'
GROUP BY wizard_name, start_date, expiration_date, amount
ORDER BY deposit_expiration_date;


SELECT
  magic_wand_creator,
  MAX(deposit_amount) AS max_deposit_amount
FROM
  wizard_deposits
GROUP BY
  magic_wand_creator
HAVING
  MAX(deposit_amount) NOT BETWEEN 20000 AND 40000
ORDER BY
  max_deposit_amount DESC
LIMIT 3;


SELECT
  CASE
    WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
    WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
    WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
    WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
    WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
    WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
    ELSE '[61+]'
  END AS age_group,
  COUNT(*) AS wizard_count
FROM
  wizard_deposits
GROUP BY
  age_group
ORDER BY
  age_group ASC;


SELECT
  COUNT(CASE WHEN department_id = 1 THEN 1 END) AS "Engineering",
  COUNT(CASE WHEN department_id = 2 THEN 1 END) AS "Tool_Design",
  COUNT(CASE WHEN department_id = 3 THEN 1 END) AS "Sales",
  COUNT(CASE WHEN department_id = 4 THEN 1 END) AS "Marketing",
  COUNT(CASE WHEN department_id = 5 THEN 1 END) AS "Purchasing",
  COUNT(CASE WHEN department_id = 6 THEN 1 END) AS "Research_and_Development",
  COUNT(CASE WHEN department_id = 7 THEN 1 END) AS "Production"
FROM
  employees;


UPDATE employees
SET
  salary = CASE
             WHEN hire_date < '2015-01-16' THEN salary + 2500
             WHEN hire_date < '2020-03-04' THEN salary + 1500
             ELSE salary
           END,
  job_title = CASE
                WHEN hire_date < '2015-01-16' THEN CONCAT('Senior ', job_title)
                WHEN hire_date < '2020-03-04' THEN CONCAT('Mid-', job_title)
                ELSE job_title
              END;
			  
SELECT first_name, job_title, salary
FROM employees;


SELECT
  job_title,
  CASE
    WHEN AVG(salary) > 45800 THEN 'Good'
    WHEN AVG(salary) BETWEEN 27500 AND 45800 THEN 'Medium'
    ELSE 'Need Improvement'
  END AS category
FROM
  employees
GROUP BY
  job_title
ORDER BY
  category ASC, job_title ASC;


SELECT project_name,
CASE
WHEN start_date IS NULL AND end_date IS NULL THEN 'Ready for development'
WHEN end_date IS NULL THEN 'In Progress'
ELSE 'Done'
END AS project_status
FROM projects
WHERE project_name LIKE '%Mountain%';


