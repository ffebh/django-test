CREATE DATABASE monitor;
USE monitor;
CREATE TABLE `einsatze` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`strasse` VARCHAR(40),
	`ort` VARCHAR(20),
	`schlagwort` VARCHAR(80),
	`alarmzeit` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`einsatzmittel` VARCHAR(5000),
	`lon` VARCHAR(20),
	`lat` VARCHAR(20),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB;
CREATE USER 'user'@'localhost' identified BY 'passwort';
GRANT ALL PRIVILEGES ON monitor.einsaetze TO 'alarmdisplay'@'localhost';
FLUSH PRIVILEGES;
