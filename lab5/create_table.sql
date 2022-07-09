CREATE DATABASE company;
USE company;
 
CREATE TABLE department (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) DEFAULT NULL,
  location VARCHAR(100) DEFAULT NULL,
  PRIMARY KEY (id)
);
 
CREATE TABLE POSITION (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) DEFAULT NULL,
  description VARCHAR(200) DEFAULT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY name_UNIQUE (name)
);
 
CREATE TABLE employee (
  id INT NOT NULL AUTO_INCREMENT,
  department_id INT DEFAULT NULL,
  position_id INT DEFAULT NULL,
  manager_id INT DEFAULT NULL,
  name VARCHAR(50) DEFAULT NULL,
  salary DECIMAL(10,2) DEFAULT NULL,
  hire_date datetime DEFAULT NULL,
  PRIMARY KEY (id),
  KEY fk_employee_department_idx (department_id),
  KEY fk_employee_position_idx (position_id),
  KEY fk_employee_manager_idx (manager_id),
  CONSTRAINT fk_employee_department FOREIGN KEY (department_id) REFERENCES department (id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_employee_manager FOREIGN KEY (manager_id) REFERENCES employee (id) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_employee_position FOREIGN KEY (position_id) REFERENCES POSITION (id) ON DELETE CASCADE ON UPDATE CASCADE
); 