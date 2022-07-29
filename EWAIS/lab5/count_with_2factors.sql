-- get the number of emplyoyees with a certain id and position
select department_id, position_id, count(id) as emp_c from employee
where position_id = 333 and department_id = 33