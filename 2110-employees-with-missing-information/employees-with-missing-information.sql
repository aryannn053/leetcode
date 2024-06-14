# Write your MySQL query statement below
select employee_id from (
    select employee_id, name as a1 from Employees
    union all
    select employee_id, salary as a1 from Salaries
) as aaa
    group by employee_id
    having count(a1)<2
    order by employee_id