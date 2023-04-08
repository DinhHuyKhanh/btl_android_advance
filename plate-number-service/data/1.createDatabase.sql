drop database btl_android;
create database btl_android;
use btl_android;

CREATE TABLE IF NOT EXISTS `user_data` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `FullName` VARCHAR(255) NOT NULL,
  `PhoneNumber` VARCHAR(255) NOT NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Password` TEXT NOT NULL,
  `PersonalNumber` VARCHAR(255) UNIQUE,
  `Address` VARCHAR(255),
  `activate` BOOLEAN default 1,
  `Coin` DECIMAL(10,2) DEFAULT 0,
  `BirthDay` DATE DEFAULT NOW(),
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `role` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `RoleName` ENUM('ADMIN','USER') NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `user_has_roles` (
  `roleId` INT UNSIGNED NOT NULL,
  `userId` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`roleId`, `userId`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `number_plate` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `NumberPlate` VARCHAR(255) NOT NULL,
  `ImagePath` TEXT,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `user_has_plates` (
  `UserId` INT UNSIGNED NOT NULL,
  `NumberPlateId` INT UNSIGNED NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `transaction_history` (
  `UserId` INT UNSIGNED NOT NULL,
  `Coin` DECIMAL(10,2),
  `CreatedDate` DATETIME,
  `description` VARCHAR(255)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `gate_history` (
  `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `UserId` INT UNSIGNED NOT NULL,
  `NumberPlate` INT UNSIGNED NOT NULL,
  `CheckInDate` DATETIME,
  `CheckOutDate` DATETIME,
  `ImagePathCheckIn` TEXT,
  `ImagePathCheckOut` TEXT,
  PRIMARY KEY (`Id`),
  INDEX IDX_1(UserId, CheckInDate)
) ENGINE=InnoDB;

