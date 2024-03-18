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


