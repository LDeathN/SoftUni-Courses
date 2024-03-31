CREATE TABLE IF NOT EXISTS owners (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(50) NOT NULL,
  phone_number VARCHAR(15) NOT NULL,
  address VARCHAR(50)
);


CREATE TABLE IF NOT EXISTS animal_types (
  "id" SERIAL PRIMARY KEY,
  animal_type VARCHAR(30) NOT NULL
);


CREATE TABLE IF NOT EXISTS cages (
  "id" SERIAL PRIMARY KEY,
  animal_type_id INT NOT NULL,
  CONSTRAINT fk_cages_animal_types
	FOREIGN KEY (animal_type_id) 
	REFERENCES animal_types("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS animals (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(30) NOT NULL,
  birthdate DATE NOT NULL,
  owner_id INT,
  animal_type_id INT NOT NULL,
  CONSTRAINT fk_animals_owners
	FOREIGN KEY (owner_id) 
	REFERENCES owners("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE,
  CONSTRAINT fk_animals_animal_types
	FOREIGN KEY (animal_type_id) 
	REFERENCES animal_types("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS volunteers_departments (
  "id" SERIAL PRIMARY KEY,
  department_name VARCHAR(30) NOT NULL
);


CREATE TABLE IF NOT EXISTS volunteers (
  "id" SERIAL PRIMARY KEY,
  "name" VARCHAR(50) NOT NULL,
  phone_number VARCHAR(15) NOT NULL,
  address VARCHAR(50),
  animal_id INT,
  department_id INT NOT NULL,
  CONSTRAINT fk_volunteers_animals
	FOREIGN KEY (animal_id) 
	REFERENCES animals("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE,
  CONSTRAINT fk_volunteers_volunteers_departments
	FOREIGN KEY (department_id) 
	REFERENCES volunteers_departments("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


CREATE TABLE IF NOT EXISTS animals_cages (
  cage_id INT NOT NULL,
  animal_id INT NOT NULL,
  CONSTRAINT fk_animals_cages_cages
	FOREIGN KEY (cage_id) 
	REFERENCES cages("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE,
  CONSTRAINT fk_animals_cages_animals
	FOREIGN KEY (animal_id) 
	REFERENCES animals("id")
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


INSERT INTO volunteers ("name", phone_number, address, animal_id, department_id)
VALUES
	('Anita Kostova', '0896365412', 'Sofia, 5 Rosa str.', 15, 1),
	('Dimitur Stoev', '0877564223', NULL, 42, 4),
	('Kalina Evtimova', '0896321112', 'Silistra, 21 Breza str.', 9, 7),
	('Stoyan Tomov', '0898564100', 'Montana, 1 Bor str.', 18, 8),
	('Boryana Mileva', '0888112233', NULL, 31, 5);

INSERT INTO animals ("name", birthdate, owner_id, animal_type_id)
VALUES
	('Giraffe', '2018-09-21', 21, 1),
	('Harpy Eagle', '2015-04-17', 15, 3),
	('Hamadryas Baboon', '2017-11-02', NULL, 1),
	('Tuatara', '2021-06-30', 2, 4);


UPDATE animals
SET owner_id = 4
WHERE owner_id IS NULL;


DELETE FROM volunteers
WHERE department_id = 2;

DELETE FROM volunteers_departments
WHERE "id" = 2
RETURNING *;


SELECT name, phone_number, address, animal_id, department_id
FROM volunteers
ORDER BY name, animal_id, department_id;


SELECT a.name, a_t.animal_type, TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM animals a
JOIN animal_types a_t ON a.animal_type_id = a_t.id
ORDER BY name;


SELECT o.name AS owner, COUNT(a.id)
FROM owners o
JOIN animals a ON o.id = a.owner_id
GROUP BY o.name
ORDER BY COUNT(a.id) DESC, o.name
LIMIT 5;


SELECT CONCAT(o.name, ' - ', a.name) AS "Owners - Animals",
o.phone_number AS "Phone Number",
c.id AS "Cage ID"
FROM owners o
JOIN animals a ON o.id = a.owner_id
JOIN animal_types at ON a.animal_type_id = at.id
JOIN animals_cages AS ac ON ac.animal_id = a.id
JOIN cages c ON ac.cage_id = c.id
WHERE at.animal_type = 'Mammals'
ORDER BY o.name, a.name DESC;


SELECT v.name AS volunteers, v.phone_number, 
SUBSTRING(
		v.address, POSITION('Sofia' IN v.address) + 7
	) AS "address"
FROM volunteers v
JOIN volunteers_departments vd ON v.department_id = vd.id
WHERE vd.department_name = 'Education program assistant'
AND v.address LIKE '%Sofia%'
ORDER BY v.name;
