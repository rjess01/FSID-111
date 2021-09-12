CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- Creating some default test users:
INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "Chris",
     "Daming",
     "Reading"
 );

 INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "John",
     "Doe",
     "Knitting"
 );

 INSERT INTO user (
    first_name,
    last_name,
    hobbies
 ) VALUES (
     "Jane",
     "Doe",
     "Riding a Bike"
 );

 UPDATE user (
     first_name,
     last_name,
     hobbies
 )