# Write your MySQL query statement below
select employee_id, 
salary * (employee_id % 2 != 0) * (name not like 'M%') as bonus 
from Employees order by employee_id;