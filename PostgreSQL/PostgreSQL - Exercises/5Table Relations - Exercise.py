CREATE TABLE products (
    product_name VARCHAR(100) NOT NULL,
	id INT GENERATED ALWAYS AS IDENTITY
);

INSERT INTO products (product_name) VALUES
    ('Broccoli'),
    ('Shampoo'),
    ('Toothpaste'),
    ('Candy');
	
ALTER TABLE products
ADD PRIMARY KEY (id);


ALTER TABLE products
DROP CONSTRAINT IF EXISTS products_pkey;


CREATE TABLE passports (
    id INT GENERATED ALWAYS AS IDENTITY (START WITH 100 INCREMENT BY 1),
    nationality VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO passports (nationality)
VALUES
('N34FG21B'),
('K65LO4R7'),
('ZE657QP2');


CREATE TABLE people(
id SERIAL PRIMARY KEY,
first_name VARCHAR(50),
salary DECIMAL(10, 2),
passport_id INT,
CONSTRAINT fk_people_passports
FOREIGN KEY (passport_id)
REFERENCES passports(id)
);

INSERT INTO people (first_name, salary, passport_id) VALUES
('Roberto', 43300.0000, 101),
    ('Tom', 56100.0000, 102),
    ('Yana', 60200.0000, 100);


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE models (
    id INT GENERATED ALWAYS AS IDENTITY (START WITH 1000 INCREMENT BY 1),
	PRIMARY KEY (id),
	model_name VARCHAR(100),
    manufacturer_id INT,
    CONSTRAINT fk_models_manufacturers
    FOREIGN KEY (manufacturer_id)
    REFERENCES manufacturers (id)
);

CREATE TABLE production_years (
    id SERIAL PRIMARY KEY,
    established_on DATE,
    manufacturer_id INT,
    CONSTRAINT fk_production_years_manufacturers
    FOREIGN KEY (manufacturer_id)
    REFERENCES manufacturers (id)
);

INSERT INTO manufacturers (name)
VALUES
('BMW'),
('Tesla'),
('Lada');

INSERT INTO models (model_name, manufacturer_id)
VALUES
('X1', 1),
('i6', 1),
('Model S', 2),
('Model X', 2),
('Model 3', 2),
('Nova', 3);

INSERT INTO production_years (established_on, manufacturer_id)
VALUES
('1916-03-01', 1),
('2003-01-01', 2),
('1966-05-01', 3);


CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	date DATE NOT NULL
);

CREATE TABLE photos(
	id SERIAL PRIMARY KEY,
	url VARCHAR(255) NOT NULL,
    place VARCHAR(100) NOT NULL,
    customer_id INT,
	CONSTRAINT fk_photos_customers
	FOREIGN KEY (customer_id)
	REFERENCES customers(id)
);

INSERT INTO customers (name, date)
VALUES
('Bella', '2022-03-25'),
('Philip', '2022-07-05');

INSERT INTO photos (url, place, customer_id)
VALUES
('bella_1111.com', 'National Theatre', 1),
('bella_1112.com', 'Largo', 1),
('bella_1113.com', 'The View Restaurant', 1),
('philip_1121.com', 'Old Town', 2),
('philip_1122.com', 'Rowing Canal', 2),
('philip_1123.com', 'Roman Theater', 2);


CREATE TABLE students(
	id SERIAL PRIMARY KEY,
	student_name VARCHAR(100) NOT NULL
);

CREATE TABLE exams(
	id INT GENERATED ALWAYS AS IDENTITY (START WITH 101 INCREMENT BY 1),
	PRIMARY KEY (id),
	exam_name VARCHAR(100) NOT NULL
);

CREATE TABLE study_halls(
	id SERIAL PRIMARY KEY,
	study_hall_name VARCHAR(100) NOT NULL,
	exam_id INT,
	CONSTRAINT fk_study_halls_exams FOREIGN KEY (exam_id) REFERENCES exams(id)
);

CREATE TABLE students_exams(
	student_id INT,
	exam_id INT,
	CONSTRAINT fk_students_exams_students FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT fk_students_exams_exams FOREIGN KEY (exam_id) REFERENCES exams(id)
);

INSERT INTO students(student_name)
VALUES
('Mila'),
('Toni'),
('Ron');

INSERT INTO exams(exam_name)
VALUES
('Python Advanced'),
('Python OOP'),
('PostgreSQL');

INSERT INTO study_halls(study_hall_name, exam_id)
VALUES
('Open Source Hall', 102),
('Inspiration Hall', 101),
('Creative Hall', 103),
('Masterclass Hall', 103),
('Information Security Hall', 103);

INSERT INTO students_exams(student_id, exam_id)
VALUES
(1, 101),
(1, 102),
(2, 101),
(3, 103),
(2, 102),
(2, 103);


CREATE TABLE item_types(
	id SERIAL PRIMARY KEY,
	item_type_name VARCHAR(50)
);

CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	item_name VARCHAR(50),
	item_type_id INT,
	CONSTRAINT fk_items_item_types
	FOREIGN KEY (item_type_id)
	REFERENCES item_types(id)
);

CREATE TABLE cities(
	id SERIAL PRIMARY KEY,
	city_name VARCHAR(50)
);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(50),
	birthday VARCHAR(50),
	city_id INT,
	CONSTRAINT fk_customers_cities
	FOREIGN KEY (city_id)
	REFERENCES cities(id)
);

CREATE TABLE orders(
	id SERIAL PRIMARY KEY,
	customer_id INT,
	CONSTRAINT fk_orders_customers
	FOREIGN KEY (customer_id)
	REFERENCES customers(id)
);

CREATE TABLE order_items(
	order_id INT,
	item_id INT,
	CONSTRAINT fk_order_items_orders
	FOREIGN KEY (order_id)
	REFERENCES orders(id),
	CONSTRAINT fk_order_items_items
	FOREIGN KEY (item_id)
	REFERENCES items(id)
);


CREATE TABLE item_types(
	id SERIAL PRIMARY KEY,
	item_type_name VARCHAR(50)
);

CREATE TABLE items(
	id SERIAL PRIMARY KEY,
	item_name VARCHAR(50),
	item_type_id INT,
	CONSTRAINT fk_items_item_types
	FOREIGN KEY (item_type_id)
	REFERENCES item_types(id)
);

CREATE TABLE cities(
	id SERIAL PRIMARY KEY,
	city_name VARCHAR(50)
);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
	customer_name VARCHAR(50),
	birthday VARCHAR(50),
	city_id INT,
	CONSTRAINT fk_customers_cities
	FOREIGN KEY (city_id)
	REFERENCES cities(id)
);

CREATE TABLE orders(
	id SERIAL PRIMARY KEY,
	customer_id INT,
	CONSTRAINT fk_orders_customers
	FOREIGN KEY (customer_id)
	REFERENCES customers(id)
);

CREATE TABLE order_items(
	order_id INT,
	item_id INT,
	CONSTRAINT fk_order_items_orders
	FOREIGN KEY (order_id)
	REFERENCES orders(id),
	CONSTRAINT fk_order_items_items
	FOREIGN KEY (item_id)
	REFERENCES items(id)
);


SELECT m.mountain_range, p.peak_name, p.elevation
FROM mountains AS m
JOIN peaks AS p
ON p.mountain_id = m.id
WHERE m.mountain_range LIKE '%Rila%'
ORDER BY p.elevation DESC;


SELECT COUNT(*)
FROM countries AS c
LEFT JOIN countries_rivers AS cr
ON c.country_code = cr.country_code
WHERE cr IS NULL;
