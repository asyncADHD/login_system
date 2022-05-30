CREATE TABLE `login_sys`.`user_data_main` (
  `USER_ID` INT NOT NULL AUTO_INCREMENT,
  `First_Name` VARCHAR(45) NOT NULL,
  `Last_Name` VARCHAR(45) NOT NULL,
  `Phone_Number` INT NOT NULL,
  `User_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE INDEX `Phone_Number_UNIQUE` (`Phone_Number` ASC) VISIBLE,
  UNIQUE INDEX `USER_ID_UNIQUE` (`USER_ID` ASC) VISIBLE,
  UNIQUE INDEX `User_Name_UNIQUE` (`User_Name` ASC) VISIBLE);


created First table, I intend to use the user name as a forign key to identify the user. As this will allow me to create privilages for the user asfter the validation stage on the program. 



- SQL command to clear all the test submitions 

delete from login_sys.login_data where UserName like "%test%";