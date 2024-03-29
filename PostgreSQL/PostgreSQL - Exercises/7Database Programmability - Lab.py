#First Problem
CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
DECLARE e_count INT;
BEGIN
SELECT COUNT(employee_id) INTO e_count
FROM employees AS e
JOIN addresses AS a ON a.address_id = e.address_id
JOIN towns AS t ON t.town_id = a.town_id
WHERE t.name = town_name;
RETURN e_count;
END;
$$ LANGUAGE plpgsql;


#Second Problem
CREATE PROCEDURE sp_increase_salaries(department_name varchar(50))
LANGUAGE plpgsql
AS $$
BEGIN
UPDATE employees AS e
SET salary = salary * 1.05
WHERE e.department_id = (
SELECT department_id FROM departments WHERE name = department_name);
END; $$;


#Third Problem
CREATE PROCEDURE sp_increase_salary_by_id(id INT)
LANGUAGE plpgsql
AS $$
BEGIN
IF (SELECT COUNT(employee_id) FROM employees WHERE employee_id = id) != 1 THEN
ROLLBACK;
ELSE
UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
END IF;
COMMIT;
END; $$;


