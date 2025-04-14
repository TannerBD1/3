CREATE DATABASE `credentialsDB` ;
USE credentialsDB;
CREATE TABLE `users` (
     `id` int(11) NOT NULL AUTO_INCREMENT,
     `username` VARCHAR(256) DEFAULT NULL,
     `hashedpwd` VARCHAR(256) DEFAULT NULL,
     `pwdsalt` VARCHAR(256) DEFAULT NULL,
     PRIMARY KEY (`id`)
) ENGINE=InnoDB;

GRANT ALL ON credentialsDB.users TO 'admin'@'localhost' identified by 'heggett'; 


INSERT INTO contactsTable (id, username) values(null, 'heggett');
