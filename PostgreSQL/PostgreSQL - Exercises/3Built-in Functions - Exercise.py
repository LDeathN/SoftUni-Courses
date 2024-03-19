CREATE VIEW view_river_info AS
SELECT CONCAT('The river', ' ', river_name, ' ', 'flows into the', ' ', outflow, ' ', 'and is', ' ', length, ' ', 'kilometers long.') AS "River Information"
FROM rivers
ORDER BY river_name;


CREATE VIEW view_continents_countries_currencies_details AS
SELECT
    CONCAT(c.continent_name, ': ', c.continent_code) AS continent_details,
    CONCAT(co.country_name, ' - ', co.capital, ' - ', co.area_in_sq_km, ' - ', 'km2') AS country_information,
    CONCAT(cr.description, ' (', cr.currency_code, ')') AS currencies
FROM
    continents c
JOIN countries co ON c.continent_code = co.continent_code
JOIN currencies cr ON co.currency_code = cr.currency_code
ORDER BY
    country_information ASC, currencies ASC;


ALTER TABLE countries
ADD COLUMN capital_code VARCHAR(2) GENERATED ALWAYS AS (SUBSTRING(capital FROM 1 FOR 2)) STORED;


UPDATE currencies
SET description = SUBSTRING(description FROM 5);

SELECT description as "substring" FROM currencies;


SELECT
  (REGEXP_MATCHES("River Information", '\D*([0-9]{1,4})\D*'))[1] AS river_length
FROM
  view_river_info;


SELECT
    REPLACE(mountain_range, 'a', '@') AS "replace_a",
    REPLACE(mountain_range, 'A', '$') AS "replace_A"
FROM
    mountains;


SELECT capital,
TRANSLATE(capital, 'áãåçéíñóú', 'aaaceinou') AS translated_name
FROM countries;


SELECT continent_name,
TRIM(BOTH FROM continent_name) AS "trim"
FROM continents;


SELECT continent_name,
TRIM(BOTH FROM continent_name) AS "trim"
FROM continents;


SELECT
    TRIM('M' FROM peak_name) AS left_trim,
    TRIM('m' FROM peak_name) AS right_trim
FROM
    peaks;


SELECT 
    CONCAT(mountain_range, ' ', peak_name) AS mountain_information,
    LENGTH(CONCAT(mountain_range, ' ', peak_name)) AS characters_length,
    BIT_LENGTH(CONCAT(mountain_range, ' ', peak_name))
FROM mountains
JOIN peaks ON mountains.id = peaks.mountain_id;


SELECT
    population,
    LENGTH(CAST(population AS CHAR(20))) AS length
FROM countries;


SELECT
    peak_name,
    LEFT(peak_name, 4) AS positive_left,
    CASE WHEN LENGTH(peak_name) - 4 > 0 THEN LEFT(peak_name, LENGTH(peak_name) - 4) ELSE '' END AS negative_left
FROM peaks;


SELECT
    peak_name,
    RIGHT(peak_name, 4) AS positive_right,
    CASE WHEN LENGTH(peak_name) - 4 > 0 THEN RIGHT(peak_name, LENGTH(peak_name) - 4) ELSE '' END AS negative_right
FROM peaks;


UPDATE countries
SET iso_code = UPPER(SUBSTRING(country_name, 1, 3))
WHERE iso_code IS NULL;

SELECT * FROM countries;


UPDATE countries
SET country_code = LOWER(REVERSE(country_code));

SELECT * FROM countries;


SELECT CONCAT(elevation, ' ', REPEAT('-', 3), REPEAT('>', 2), ' ', peak_name) AS "Elevation -->> Peak Name"
FROM peaks
WHERE elevation >= 4884;


CREATE TABLE bookings_calculation AS
SELECT booked_for
FROM bookings
WHERE apartment_id = 93;

ALTER TABLE bookings_calculation
ADD COLUMN multiplication NUMERIC,
ADD COLUMN modulo NUMERIC;

UPDATE bookings_calculation
SET
    multiplication = booked_for * 50,
    modulo = booked_for % 50;


SELECT latitude,
ROUND(latitude, 2) AS "round",
TRUNC(latitude, 2) AS "trunc"
FROM apartments;


SELECT longitude,
ABS(longitude) AS "abs"
FROM apartments;


