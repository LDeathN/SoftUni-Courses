#First Problem
SELECT title FROM books
WHERE title LIKE 'The%'
ORDER BY id;


#Second Problem
SELECT REPLACE(title, 'The', '***') AS title FROM books
WHERE title LIKE 'The%'
ORDER BY id;


#Third Problem
SELECT id, 
       CAST(0.5 * side * height AS DECIMAL(30, 16)) AS area
FROM triangles
ORDER BY id;


#Fourth Problem
SELECT title, 
       ROUND(cost, 3) AS modified_price
FROM books
ORDER BY id;


#Fifth Problem
SELECT first_name,
       last_name,
       EXTRACT(YEAR FROM born) AS year
FROM authors;


#Sixth Problem
SELECT last_name AS "Last Name",
       TO_CHAR(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors;


