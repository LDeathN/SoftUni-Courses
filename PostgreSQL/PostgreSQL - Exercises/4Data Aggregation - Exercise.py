SELECT COUNT(id) AS count
FROM wizard_deposits;


SELECT SUM(deposit_amount) AS total_amount
FROM wizard_deposits;


SELECT ROUND(AVG(magic_wand_size), 3) AS average_magic_wand_size
FROM wizard_deposits;


SELECT MIN(deposit_charge) AS minimum_deposit_charge
FROM wizard_deposits;


