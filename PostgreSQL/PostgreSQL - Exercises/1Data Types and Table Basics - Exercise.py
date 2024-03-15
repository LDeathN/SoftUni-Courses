#First Problem
CREATE TABLE minions_info(
id SERIAL PRIMARY KEY,
name VARCHAR(30),
age INTEGER
);


#Second Problem
ALTER TABLE minions_info
ADD code CHAR(4);

ALTER TABLE minions_info
ADD task TEXT;

ALTER TABLE minions_info
ADD salary NUMERIC(8, 3);


#Third Problem
ALTER TABLE minions_info
RENAME COLUMN salary TO banana;


#Fourth Problem
ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN;

ALTER TABLE minions_info
ALTER COLUMN equipped SET NOT NULL;


#Fifth Problem
CREATE TYPE type_mood AS ENUM (
'happy',
'relaxed',
'stressed',
'sad');

ALTER TABLE minions_info
ADD COLUMN mood type_mood;


