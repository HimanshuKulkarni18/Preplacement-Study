#MySQL Basics Queries

1. Create Database
CREATE DATABASE company_db;

Use database:

USE company_db;

2. Create Table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

3. Insert Data
INSERT INTO employees (name, age, department, salary)
VALUES
('Rahul', 28, 'IT', 60000),
('Priya', 30, 'HR', 50000),
('Amit', 25, 'IT', 45000);
4. View All Data
SELECT * FROM employees;

5. Select Specific Columns
SELECT name, salary
FROM employees;

6. WHERE Clause
SELECT *
FROM employees
WHERE department = 'IT';

Multiple conditions:

SELECT *
FROM employees
WHERE salary > 50000
AND age < 30;

7. ORDER BY

Ascending:

SELECT *
FROM employees
ORDER BY salary ASC;

Descending:

SELECT *
FROM employees
ORDER BY salary DESC;

8. LIMIT
SELECT *
FROM employees
LIMIT 2;

9. UPDATE Query
UPDATE employees
SET salary = 70000
WHERE id = 1;

10. DELETE Query
DELETE FROM employees
WHERE id = 2;