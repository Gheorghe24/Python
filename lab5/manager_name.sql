-- List the employees name and the name of their manager --
SELECT manager.name AS manager_name, emp.name AS employee_name FROM employee 
AS emp
INNER JOIN employee AS manager ON emp.manager_id = manager.id
ORDER BY manager_name ASC;