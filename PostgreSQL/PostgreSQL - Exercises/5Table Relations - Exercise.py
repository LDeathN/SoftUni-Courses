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
