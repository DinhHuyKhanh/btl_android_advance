use btl_android;

ALTER TABLE `user_data`
ADD `ResetPasswordToken` varchar(255);

drop table if exists `user_has_plates`;

DROP TABLE IF EXISTS `number_plate`;
CREATE TABLE IF NOT EXISTS number_plate(
    `Id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `UserId`  INT NOT NULL,
    `NumberPlate` VARCHAR(255) NOT NULL,
    `ImagePath` TEXT,
    PRIMARY KEY (`Id`)
)ENGINE=InnoDB;


ALTER TABLE `gate_history`
MODIFY  COLUMN  `NumberPlate` VARCHAR(255);


alter table transaction_history
add column Id INT unsigned not null auto_increment primary key;

alter table transaction_history
add column LastCoin Decimal(10,2);

alter table transaction_history
change description Description VARCHAR(255);

alter table gate_history 
add column Coin Decimal(10,2);