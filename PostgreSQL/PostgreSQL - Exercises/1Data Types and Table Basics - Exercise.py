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


#Sixth Problem
ALTER TABLE minions_info
ALTER COLUMN age SET DEFAULT 0,
ALTER COLUMN name SET DEFAULT '',
ALTER COLUMN code SET DEFAULT '';


#Seventh Problem
ALTER TABLE minions_info
ADD CONSTRAINT unique_constraint UNIQUE (id, email),
ADD CONSTRAINT banana_check CHECK (banana > 0);


#Eigth Problem
ALTER TABLE minions_info
ALTER COLUMN task TYPE VARCHAR(150);


#Ninth Problem
ALTER TABLE minions_info
ALTER COLUMN equipped DROP NOT NULL;


#Tenth Problem
ALTER TABLE minions_info
DROP COLUMN age;


#Eleventh Problem
CREATE TABLE minions_birthdays (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
date_of_birth DATE NOT NULL,
age INTEGER NOT NULL,
present VARCHAR(100),
party TIMESTAMP with TIME ZONE NOT NULL
);

ALTER TABLE minions_birthdays
ADD CONSTRAINT unique_id_constraint UNIQUE (id);


#Twelfth Problem
INSERT INTO minions_info (name, code, task, banana, email, equipped, mood)
VALUES
    ('Mark', 'GKYA', 'Graphing Points', 3265.265, 'mark@minion.com', false, 'happy'),
    ('Mel', 'HSK', 'Science Investigation', 54784.996, 'mel@minion.com', true, 'stressed'),
    ('Bob', 'HF', 'Painting', 35.652, 'bob@minion.com', true, 'happy'),
    ('Darwin', 'EHND', 'Create a Digital Greeting', 321.958, 'darwin@minion.com', false, 'relaxed'),
    ('Kevin', 'KMHD', 'Construct with Virtual Blocks', 35214.789, 'kevin@minion.com', false, 'happy'),
    ('Norbert', 'FEWB', 'Testing', 3265.500, 'norbert@minion.com', true, 'sad'),
    ('Donny', 'L', 'Make a Map', 8.452, 'donny@minion.com', true, 'happy');


#Thirteenth Problem
SELECT name, task, email, banana FROM minions_info;


#Fourteenth Problem
TRUNCATE TABLE minions_info;


#Fifteenth Problem
DROP TABLE minions_birthdays;
