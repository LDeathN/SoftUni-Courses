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
