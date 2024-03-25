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


