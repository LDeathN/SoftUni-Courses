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


