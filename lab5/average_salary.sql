-- GET the average salary for each department
select department_id, avg(salary) as average_s from employee
group by department_id
order by salary asc;