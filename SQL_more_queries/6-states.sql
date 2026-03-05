-- Script that creates the database hbtn_0d_usa and the table states
-- states description:
--   id INT unique, auto generated, not null, primary key
--   name VARCHAR(256) not null
-- If the database hbtn_0d_usa already exists, the script should not fail
-- If the table states already exists, the script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
