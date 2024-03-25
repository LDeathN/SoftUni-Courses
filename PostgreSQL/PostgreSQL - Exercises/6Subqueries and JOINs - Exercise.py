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


