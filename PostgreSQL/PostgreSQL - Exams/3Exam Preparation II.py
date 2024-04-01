CREATE TABLE addresses(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE categories(
	id SERIAL PRIMARY KEY,
	name VARCHAR(10) NOT NULL
);

CREATE TABLE clients(
	id SERIAL PRIMARY KEY,
	full_name VARCHAR(50) NOT NULL,
	phone_number VARCHAR(20) NOT NULL
);

CREATE TABLE drivers(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30) NOT NULL,
	age INT NOT NULL,
	rating NUMERIC(3, 2) DEFAULT 5.5,
	CONSTRAINT drivers_age_check CHECK (age > 0)
);

CREATE TABLE cars(
	id SERIAL PRIMARY KEY,
	make VARCHAR(20) NOT NULL,
	model VARCHAR(20),
	"year" INT NOT NULL DEFAULT 0,
	mileage INT DEFAULT 0,
	"condition" CHAR(1) NOT NULL,
	category_id INT NOT NULL,
	CONSTRAINT cars_year_check CHECK ("year" > 0),
	CONSTRAINT cars_mileage_check CHECK (mileage > 0),
	CONSTRAINT fk_cars_categories
	FOREIGN KEY (category_id)
	REFERENCES categories(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE courses(
	id SERIAL PRIMARY KEY,
	from_address_id INT NOT NULL,
	"start" TIMESTAMP NOT NULL,
	bill NUMERIC(10, 2) DEFAULT 10,
	car_id INT NOT NULL,
	client_id INT NOT NULL,
	CONSTRAINT courses_bill_check CHECK (bill > 0),
	CONSTRAINT fk_courses_addresses
	FOREIGN KEY (from_address_id)
	REFERENCES addresses(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_courses_cars
	FOREIGN KEY (car_id)
	REFERENCES cars(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_courses_clients
	FOREIGN KEY (client_id)
	REFERENCES clients(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);

CREATE TABLE cars_drivers(
	car_id INT NOT NULL,
	driver_id INT NOT NULL,
	CONSTRAINT fk_cars_drivers_cars
	FOREIGN KEY (car_id)
	REFERENCES cars(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
	CONSTRAINT fk_cars_drivers_drivers
	FOREIGN KEY (driver_id)
	REFERENCES drivers(id)
	ON DELETE CASCADE
	ON UPDATE CASCADE
);


INSERT INTO clients (full_name, phone_number)
SELECT
    CONCAT(d.first_name, ' ', d.last_name) AS full_name,
    CONCAT('(088) 9999', (d.id * 2)) AS phone_number
FROM drivers d
WHERE d.id BETWEEN 10 AND 20;


UPDATE cars
SET "condition" = 'C'
WHERE (mileage >= 800000 OR mileage IS NULL)
AND "year" <= 2010
AND make NOT LIKE '%Mercedes-Benz%';


DELETE FROM clients
WHERE length(full_name) > 3
AND id NOT IN (SELECT client_id FROM courses);


SELECT make, model, condition
FROM cars
ORDER BY id;


SELECT d.first_name, d.last_name, c.make, c.model, c.mileage
FROM drivers d
JOIN cars_drivers cd ON d.id = cd.driver_id
JOIN cars c ON c.id = cd.car_id
WHERE c.mileage IS NOT NULL
ORDER BY c.mileage DESC, d.first_name;


