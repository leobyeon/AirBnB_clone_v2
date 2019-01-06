-- Creates a database, sets a password, creates a user, and grants privileges
-- Creates hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates user:hbnb_dev with password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privileges to hbnb_dev for database: hbnb_dev_db
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants the SELECT privilege to hbnb_dev on database: performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
