DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS manufacturer;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    active BOOLEAN
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    NAME VARCHAR(255),
    description TEXT,
    category VARCHAR(255),
    stock INT,
    buy_cost INT,
    sell_price INT,
    manufacturer_id INT REFERENCES manufacturer(id),
    sold_out BOOLEAN
);