-- Script that creates the database hbtn_0d_usa and the table cities
-- cities description:
--   id INT unique, auto generated, not null, primary key
--   state_id INT not null, foreign key referencing states(id)
--   name VARCHAR(256) not null
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table cities already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
