SELECT CONCAT(a.address, ' ', a.address_2) AS apartment_address,
b.booked_for AS nights
FROM apartments AS a
INNER JOIN bookings AS b
ON a.booking_id = b.booking_id
ORDER BY a.apartment_id;


SELECT a.name, a.country, DATE(b.booked_at) AS formatted_date
FROM apartments AS a
LEFT JOIN bookings AS b
ON a.booking_id = b.booking_id
LIMIT 10;


SELECT b.booking_id, DATE(b.starts_at) AS starts_at, b.apartment_id,
CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM bookings AS b
RIGHT JOIN customers AS c
ON b.customer_id = c.customer_id
ORDER BY CONCAT(c.first_name, ' ', c.last_name)
LIMIT 10;


SELECT 
    b.booking_id,
    a.name AS apartment_owner,
    a.apartment_id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM 
    bookings b
FULL JOIN 
    apartments a ON b.booking_id = a.booking_id
FULL JOIN 
    customers c ON b.customer_id = c.customer_id
ORDER BY 
    b.booking_id ASC, 
    apartment_owner ASC, 
    customer_name ASC;


SELECT b.booking_id, b.apartment_id, c.companion_full_name
FROM bookings b
JOIN customers c ON b.customer_id = c.customer_id
WHERE b.apartment_id IS NULL;


SELECT b.apartment_id, b.booked_for, c.first_name, c.country
FROM bookings b
JOIN customers c ON b.customer_id = c.customer_id
WHERE c.job_type LIKE '%Lead%';


SELECT COUNT(*) AS count
FROM customers
WHERE last_name LIKE '%Hahn%';


SELECT name, SUM(b.booked_for) AS sum
FROM apartments a
JOIN bookings b ON a.apartment_id = b.apartment_id
GROUP BY name
ORDER BY name;


SELECT a.country, COUNT(b.booking_id) AS booking_count
FROM apartments a
JOIN bookings b ON a.apartment_id = b.apartment_id
WHERE b.booked_at > '2021-05-18 07:52:09.904+03' AND b.booked_at < '2021-09-17 19:48:02.147+03'  
GROUP BY a.country
ORDER BY COUNT (b.booking_id) DESC;


SELECT m_c.country_code, m.mountain_range, p.peak_name, p.elevation
FROM mountains_countries m_c
JOIN mountains m ON m_c.mountain_id = m.id
JOIN peaks p ON m_c.mountain_id = p.mountain_id
WHERE p.elevation > 2835 AND m_c.country_code = 'BG'
ORDER BY p.elevation DESC;


SELECT m_c.country_code, COUNT(DISTINCT m.mountain_range) AS mountain_range_count
FROM mountains_countries m_c
JOIN mountains m ON m_c.mountain_id = m.id
WHERE m_c.country_code = 'US' OR m_c.country_code = 'RU' OR m_c.country_code = 'BG'
GROUP BY m_c.country_code
ORDER BY mountain_range_count DESC;


SELECT c.country_name, r.river_name
FROM countries c
FULL JOIN countries_rivers c_r ON c_r.country_code = c.country_code
FULL JOIN rivers r ON c_r.river_id = r.id
JOIN continents AS con ON c.continent_code = con.continent_code
WHERE con.continent_name = 'Africa'
ORDER BY c.country_name
LIMIT 5;


SELECT MIN(avg_area) AS min_average_area
FROM (
    SELECT AVG(c.area_in_sq_km) AS avg_area
    FROM countries c
    GROUP BY c.continent_code
) AS continent_avg_areas_alias;


SELECT COUNT(*) AS countries_without_mountains
FROM countries c
LEFT JOIN mountains_countries m_c ON m_c.country_code = c.country_code
WHERE m_c.country_code IS NULL;


CREATE TABLE monasteries (
    id SERIAL PRIMARY KEY,
    monastery_name VARCHAR(255) NOT NULL,
    country_code CHAR(2) NOT NULL
);

INSERT INTO monasteries (monastery_name, country_code) VALUES
('Rila Monastery "St. Ivan of Rila"', 'BG'),
  ('Bachkovo Monastery "Virgin Mary"', 'BG'),
  ('Troyan Monastery "Holy Mother''s Assumption"', 'BG'),
  ('Kopan Monastery', 'NP'),
  ('Thrangu Tashi Yangtse Monastery', 'NP'),
  ('Shechen Tennyi Dargyeling Monastery', 'NP'),
  ('Benchen Monastery', 'NP'),
  ('Southern Shaolin Monastery', 'CN'),
  ('Dabei Monastery', 'CN'),
  ('Wa Sau Toi', 'CN'),
  ('Lhunshigyia Monastery', 'CN'),
  ('Rakya Monastery', 'CN'),
  ('Monasteries of Meteora', 'GR'),
  ('The Holy Monastery of Stavronikita', 'GR'),
  ('Taung Kalat Monastery', 'MM'),
  ('Pa-Auk Forest Monastery', 'MM'),
  ('Taktsang Palphug Monastery', 'BT'),
  ('Sümela Monastery', 'TR');

ALTER TABLE countries
ADD COLUMN three_rivers BOOLEAN DEFAULT false;

UPDATE countries c
SET three_rivers = true
WHERE (
    SELECT COUNT(*)
    FROM rivers r
	JOIN countries_rivers cr ON c.country_code = cr.country_code
    WHERE r.id = cr.river_id
) > 3;

SELECT m.monastery_name AS monastery, c.country_name AS country
FROM monasteries m
JOIN countries c ON m.country_code = c.country_code
WHERE c.three_rivers = false
ORDER BY m.monastery_name;


SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public'
ORDER BY tablename ASC, indexname ASC;


WITH row_number AS (
    SELECT
        c.country_name,
        p.peak_name,
        p.elevation,
        m.mountain_range,
        ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS ranking
    FROM countries c
	LEFT JOIN mountains_countries m_c ON m_c.country_code = c.country_code
    LEFT JOIN mountains m ON m_c.mountain_id = m.id
	LEFT JOIN peaks p ON m.id = p.mountain_id
    
)

-- Select the required columns from the CTE and handle null values and display options
SELECT
    country_name,
    COALESCE(peak_name, '(no highest peak)') AS peak_name,
    COALESCE(elevation, 0) AS elevation,
    CASE
        WHEN peak_name IS NOT NULL THEN COALESCE(mountain_range, '(no mountain)')
        ELSE '(no mountain)'
    END AS mountain_range
FROM row_number

-- Filter the result set to only show the highest peaks for each country
WHERE ranking = 1

-- Order the result set as specified
ORDER BY country_name ASC, elevation DESC;
