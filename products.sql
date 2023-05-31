CREATE TABLE products (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  description VARCHAR(500) NOT NULL,
  price INT NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO products (name, description, price) VALUES
('Product 1', 'This is a product.', 10),
('Product 2', 'This is another product.', 20),
('Product 3', 'This is a third product.', 30);
