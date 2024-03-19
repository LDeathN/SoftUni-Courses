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


