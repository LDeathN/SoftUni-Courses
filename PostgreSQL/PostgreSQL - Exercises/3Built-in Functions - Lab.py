#First Problem
SELECT title FROM books
WHERE title LIKE 'The%'
ORDER BY id;


#Second Problem
SELECT REPLACE(title, 'The', '***') AS title FROM books
WHERE title LIKE 'The%'
ORDER BY id;


