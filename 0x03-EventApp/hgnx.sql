-- Prepare the development database on the MySQL server

-- create the development database if it doesn't already exist
 DROP DATABASE IF EXISTS `hgnx_db`;
 CREATE DATABASE IF NOT EXISTS `hgnx_db`;
 USE `hgnx_db`;

-- reduce pasword policy to low
-- SET GLOBAL validate_password.policy=LOW;

-- add new user and set a password
CREATE USER IF NOT EXISTS 'hgnx_dev'@'localhost' IDENTIFIED BY 'hgnx_dev_pwd';

-- grant privileges to users on the new database
GRANT ALL PRIVILEGES ON hgnx_db.* TO 'hgnx_dev'@'localhost';

-- grand select privilege to user on performance_schema
GRANT SELECT ON performance_schema.* TO 'hgnx_dev'@'localhost';

FLUSH PRIVILEGES;
