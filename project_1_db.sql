-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema pyproject1_db
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pyproject1_db` ;

-- -----------------------------------------------------
-- Schema pyproject1_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pyproject1_db` DEFAULT CHARACTER SET utf8 ;
USE `pyproject1_db` ;

-- -----------------------------------------------------
-- Table `pyproject1_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pyproject1_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyproject1_db`.`avatars`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pyproject1_db`.`avatars` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `attack` INT NULL,
  `health` INT NULL,
  `str` INT NULL,
  `vit` INT NULL,
  `defense` INT NULL,
  `class` VARCHAR(45) NULL,
  `created_at` VARCHAR(45) NULL,
  `updated_at` VARCHAR(45) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_avatars_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_avatars_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `pyproject1_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pyproject1_db`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pyproject1_db`.`items` (
  `id` INT NOT NULL,
  `itemscol` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
