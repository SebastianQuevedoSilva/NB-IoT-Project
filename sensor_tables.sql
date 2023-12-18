--Author: Sebastian Quevedo Silva
--Date: December 17, 2023
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
-- -----------------------------------------------------
-- Schema nb_iot_monitoring_EL5207
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `nb_iot_monitoring_EL5207` DEFAULT CHARACTER SET utf8;
USE `nb_iot_monitoring_EL5207` ;


-- -----------------------------------------------------
-- Table `nb_iot_monitoring_EL5207`.`TemperatureData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nb_iot_monitoring_EL5207`.`TemperatureData` (
  `id` INT NOT NULL AUTO_INCREMENT,
  value FLOAT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `nb_iot_monitoring_EL5207`.`HumidityData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nb_iot_monitoring_EL5207`.`HumidityData` (
  `id` INT NOT NULL AUTO_INCREMENT,
  value FLOAT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `nb_iot_monitoring_EL5207`.`PPMData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nb_iot_monitoring_EL5207`.`PPMData` (
  `id` INT NOT NULL AUTO_INCREMENT,
  value FLOAT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY (`id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `nb_iot_monitoring_EL5207`.`BatteryData`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `nb_iot_monitoring_EL5207`.`BatteryData` (
  `id` INT NOT NULL AUTO_INCREMENT,
  value FLOAT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

CREATE USER 'mqtt_client'@'localhost' IDENTIFIED BY 'mqtt_client';

GRANT ALL ON nb_iot_monitoring_EL5207.* TO cc5002@localhost;
