-- Creates a database, sets a password, creates a user, and grants privileges
-- Creates hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user:hbnb_test with password 'hbnb_test_pwd'
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privileges to hbnb_test on database: hbnb_test_db
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants the SELECT privilege to hbnb_test on database: performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
