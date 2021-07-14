-- Create the database hbtn_0d_2.
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;
-- Create the user "user_0d_2" with select privilege in "hbtn_0d_2".
CREATE USER user_0d_2 IF NOT EXISTS IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT PRIVILEGES ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
