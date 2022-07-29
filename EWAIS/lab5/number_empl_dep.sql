-- Get the number of employees for each department --
SELECT department_id, COUNT(id) AS emp_count FROM employee
group by department_id