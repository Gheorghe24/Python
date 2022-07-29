-- Get the number of employees from a certain department 
SELECT department_id, COUNT(id) AS employee_count FROM employee
WHERE department_id = 11
GROUP BY department_id;