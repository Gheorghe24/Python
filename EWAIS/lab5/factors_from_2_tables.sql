-- list the employee name, salary, the name of their department and position --
select emp.name as employee, pos.name as position , dept.name as department, emp.salary as salary, pos.name as position from employee as emp
inner join position as pos 
on pos.id = emp.position_id
inner join department as dept
on dept.id = emp.department_id
order by position asc;