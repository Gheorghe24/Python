-- list the employee name, salary, the name of their position --
select emp.name as employee, pos.name as position , emp.salary as salary from employee as emp
inner join position as pos 
on pos.id = emp.position_id
order by salary desc;