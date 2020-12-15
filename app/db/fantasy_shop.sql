DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    category VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    NAME VARCHAR(255),
    description TEXT,
    category VARCHAR(255),
    buy_cost INT,
    sell_price INT,
    manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
    stock INT,
    sold_out BOOLEAN,
    low_stock BOOLEAN
);